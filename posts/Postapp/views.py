from django.shortcuts import render,redirect
from .models import Post,User
from .forms import PostForm

# Create your views here.
def posts(request):
    queryset = Post.objects.exclude(author__username = request.user)
    context = {"posts": queryset}
    return render(request, 'index.html', context=context)


def addPost(request):
    if request.method == "POST":
        form_data = PostForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.author.username = request.user
            post.save()
            return redirect("posts")
    context = {"form" : PostForm}
    return render(request, 'addPost.html', context=context)


def profile(request):
    posts = Post.objects.filter(author__username = request.user)
    print(request.user.username)
    user = User.objects.filter(username__username = request.user.username)
    print(user)
    context = { 'posts' : posts , "user" : user}
    return render(request, 'profile.html', context = context)
