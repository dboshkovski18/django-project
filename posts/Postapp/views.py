from django.shortcuts import render
from .models import Post


# Create your views here.
def posts(request):
    queryset = Post.objects.all()
    context = {"posts": queryset}
    return render(request, 'index.html', context=context)
