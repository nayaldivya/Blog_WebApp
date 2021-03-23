from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#dummy data



#def home(request):
#    return HttpResponse('<h1>Blog Home</h1>')
# Another way (shortcut) to do this is by using render
def home (request):
    # data of posts is sent to home page with context dictionary
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context) #render takes 2 arguments, request and name of template

#def about(request):
#   return HttpResponse('<h1>Blog About</h1>')
def about(request):
    return render(request,'blog/about.html',{'title':'about'})