from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from user_auth.forms import UserRegisterForm


# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        # form = UserRegisterForm(request.POST)
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            request.session.set_expiry(300)
            login(request, user)
            messages.success(request, 'success!')
            return redirect('index')
        # form = UserRegisterForm()
    else: form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)