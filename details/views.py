from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import *
from .serializers import *


class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def contacts(request):
    return render(request, 'contacts.html')


@login_required
def events(request):
    return render(request, 'events.html')


@login_required
def gallery(request):
    return render(request, 'gallery.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def association(request):
    return render(request, 'association.html')


# def register(request):
#    if request.method == 'POST':
#        form = UserAdminCreationForm(request.POST)
#        if form.is_valid():
#            new_user = form.save(commit=False)
#            new_user.save()
#            cd = form.cleaned_data
#            user = authenticate(
#                request,
#                username=cd['username'],
#                password=cd['password1'])
#            if user is not None:
#                if user.is_active:
#                    login(request, user)
#                    return render(request, 'home.html')
#                else:
#                    return HttpResponse('Disabled account')
#            else:
#                return HttpResponse('Invalid Login')
#    else:
#        form = UserAdminCreationForm()
#        args = {'form': form}
#        return render(request, 'register.html', args)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'profile.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        form = EditProfileForm()
        user = request.user
        user.full_name = request.POST['full_name']
        user.phone1 = request.POST['phone1']
        user.phone2 = request.POST['phone2']
        user.email = request.POST['email']
        user.status = request.POST['status']
        user.save()
        return redirect('details:profile')
    else:
        form = EditProfileForm()
        return render(request, 'edit.html', {'form': form})
