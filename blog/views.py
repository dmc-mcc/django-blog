from django.shortcuts import render
from django.views import generic
from .models import Post

#from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
#    model = Post
#    queryset = Post.objects.filter(author=2)
    queryset = Post.objects.all()
    template_name = "post_list.html"
 #   queryset = Post.objects.all().order_by("created_on")
 #   queryset = Post.objects.filter(status=1)
 

#def my_blog(request):
 #   return HttpResponse("Hello, Blog!")
