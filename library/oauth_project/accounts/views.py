from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')

def login(request):
    if request.method == "POST":
        auth_id = request.POST.get('auth_id')
        auth_pwd = request.POST.get('auth_pwd')
        user = authenticate(request, username=auth_id, password=auth_pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('accounts:main')