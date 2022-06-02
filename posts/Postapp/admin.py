from django.contrib import admin
from .models import Post,Comment,User
# Register your models here.

class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):

    list_display = ("post_title","author")

    search_fields = ("content", "post_title")

    list_filter = ("date_created",)

    inlines = [CommentAdmin,]

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author.username):
            return True
        return False


admin.site.register(Post,PostAdmin)

class UserAdmin(admin.ModelAdmin):

    list_display = ("name","surname")
    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.username):
            return True
        return False


admin.site.register(User,UserAdmin)