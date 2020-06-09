# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import EditProfileForm


def profile(request, user_id):
    if request.method == "POST":
        return on_profile_edit(request, user_id)

    if request.user.id == user_id:
        return render(request, "profile_edit.html", context={"user": request.user, "is_current_user": True})

    user = User.objects.get(id=user_id)
    return render(request, "profile.html", context={"user": user, "is_current_user": False})


def on_profile_edit(request, user_id):
    if not request.user.is_authenticated:
        return render(request, "index.html", context={"errors": ["You need to be logged in order to do this action"]})

    form = EditProfileForm(request.POST)

    if form.is_valid():
        request.user.profile.bio = request.POST['bio']
        request.user.profile.image = request.POST['image']
        request.user.profile.save()

        return render(request, "profile_edit.html", context={"user": request.user, "is_current_user": True})
    else:
        return render(request, "profile_edit.html", context={"user": request.user, "is_current_user": True, "errors": ["Form is not valid"]})
