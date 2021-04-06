from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    #Creating a form, django has classes which can generate django froms in html.
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # create user
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})