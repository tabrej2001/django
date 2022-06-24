from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import RegisterForm

# Create your views here.

def register(request):
    if request.method=='POST':
            #form=UserCreationForm(request.POST) Inbuilt form bnega isse
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,f'Welcome {username}, your account is created ')
                return redirect('login')
    else:
        #form=UserCreationForm() Inbuilt form bnega isse
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form}) 


@login_required
def profilepage(request):
        return render(request,'users/profile.html')
