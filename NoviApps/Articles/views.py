# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import ArticleForm
from .models import Article


def index(request):
    articles = Article.objects.order_by('-id')
    return render(request, "index.html", context={"current_user": request.user, "articles": articles})


def show(request, slug):
    article = Article.objects.get(slug=slug)
    favorites_count = article.favorited_by.count()
    is_current_user = article.author.id == request.user.id

    if request.user.is_authenticated:
        is_following = request.user.profile.is_following(
            article.author.profile)
        has_favorited = request.user.profile.has_favorited(article)
    else:
        is_following = False
        has_favorited = False

    return render(request, "article.html", context={"article": article, "current_user": request.user, "user": article.author,  "is_current_user": is_current_user, "is_following": is_following, "has_favorited": has_favorited, "favorites_count": favorites_count})


@login_required(login_url="/login")
def delete(request, slug):
    article = Article.objects.get(slug=slug)

    if article.author_id != request.user.id:
        redirect("/")

    article.delete()
    return redirect("/")


@login_required(login_url="/login")
def favorite(request, slug):
    article = Article.objects.get(slug=slug)
    profile = request.user.profile

    profile.favorite(article)
    return redirect(f'/article/{slug}')


@login_required(login_url="/login")
def unfavorite(request, slug):
    article = Article.objects.get(slug=slug)
    profile = request.user.profile

    profile.unfavorite(article)
    return redirect(f'/article/{slug}')


@login_required(login_url="/login")
def new(request):
    errors = []

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            body = form.cleaned_data.get('body')
            slug = slugify(title)

            if Article.objects.filter(slug=slug).exists():
                return render(request, "article_new.html", context={"errors": ["This title is not available"], "current_user": request.user})

            Article(slug=slug, title=title, image=image,
                    body=body, author=request.user).save()
            return render(request, "article_new.html", context={"success": ["Done!"], "current_user": request.user})
        else:
            errors.append("Form is not valid")

    return render(request, "article_new.html", context={"errors": errors, "current_user": request.user})


@login_required(login_url="/login")
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    errors = []

    if not article:
        return redirect("/")

    # Only the author can edit his articles
    if article.author_id != request.user.id:
        return redirect("/")

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            body = form.cleaned_data.get('body')
            slug = slugify(title)

            if article.title == title:
                pass
            elif Article.objects.filter(slug=slug).exists():
                return render(request, "article_new.html", context={"errors": ["This title is not available"], "current_user": request.user})

            article.slug = slug
            article.title = title
            article.image = image
            article.body = body
            article.save()

            return redirect("/")
        else:
            errors.append("Form is not valid")

    return render(request, "article_edit.html", context={"article": article, "errors": errors, "current_user": request.user})
