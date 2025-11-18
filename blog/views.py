from django.shortcuts import render # type: ignore
from django.views import generic # type: ignore
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/index.html'
    paginate_by = 6