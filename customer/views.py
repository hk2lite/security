from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Add this
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def home(request):
    return render(request, 'home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'error': 'Password Or Username incorrect'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
