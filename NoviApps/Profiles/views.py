# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import EditProfileForm
from .models import Profile


def profile(request, user_id):
    if request.method == "POST":
        return on_profile_edit(request, user_id)

    if request.user.id == user_id:
        return render(request, "profile_edit.html", context={"user": request.user, "current_user": request.user, "is_current_user": True})

    user = User.objects.get(id=user_id)
    is_following = request.user.profile.is_following(
        user.profile) if request.user.is_authenticated else False

    return render(request, "profile.html", context={"user": user, "current_user": request.user, "is_following": is_following, "is_current_user": False})


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


@login_required(login_url="/login")
def follow(request, followee_id):
    follower = request.user.profile
    followee = Profile.objects.get(user_id=followee_id)

    if follower.id == followee.id:
        redirect("/")

    follower.follow(followee)

    return redirect(f'/profile/{request.user.id}')


@login_required(login_url="/login")
def unfollow(request, follower_id):
    follower = request.user.profile
    followee = Profile.objects.get(user_id=follower_id)

    follower.unfollow(followee)

    return redirect(f'/profile/{request.user.id}')
