from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, './html/index.html')
def about(request):
    return render(request, './html/about.html')
def form(request):
    return render(request, './html/form.html')
def chatbot(request):
    return render(request, './html/chatbow.html')
def gallery(request):
    return render(request, './html/gallery.html')