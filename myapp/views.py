from django.shortcuts import render, HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404, render
# Create your views here.
def home(request):
    return render(request, './html/index.html')
def about(request):
    return render(request, './html/about.html')
def form(request):
    return render(request, './html/form.html')
def chatbot(request):
    return render(request, './html/chatbot.html')
def gallery(request):
    return render(request, './html/gallery.html')
def home(request):
    posts = Post.objects.all()
    return render(request, './html/index.html', {'posts': posts})
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, './html/post_detail.html', {'post': post})