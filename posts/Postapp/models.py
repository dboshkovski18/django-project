from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    content = models.TextField()
    files = models.FileField(null=True, blank=True)
    date_created = models.DateField()
    date_modified = models.DateField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null= True, blank=True)


