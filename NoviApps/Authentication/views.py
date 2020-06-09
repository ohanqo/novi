# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from NoviApps.Profiles.models import Profile

from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()

            login(request, user)
            return redirect("/")
        else:
            return render(request, "register.html", context={"errors": form.error_messages})

    return render(request, "register.html")


def connect(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    errors = []

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                errors.append('Invalid password or email.')

        else:
            errors = errors.append('Invalid password or email.')

    return render(request, "login.html", context={"errors": errors})


def disconnect(request):
    logout(request)
    return redirect('/')
