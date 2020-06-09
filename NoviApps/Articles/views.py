# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import ArticleForm
from .models import Article


def index(request):
    return render(request, "index.html", context={"user": request.user})


def show(request, slug):
    article = Article.objects.get(slug=slug)
    is_current_user = article.author.id == request.user.id
    return render(request, "article.html", context={"article": article, "is_current_user": is_current_user})


@login_required(login_url="/login")
def delete(request, slug):
    article = Article.objects.get(slug=slug)

    if article.author_id != request.user.id:
        redirect("/")

    article.delete()
    return redirect("/")


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
                return render(request, "article_new.html", context={"errors": ["This title is not available"]})

            Article(slug=slug, title=title, image=image,
                    body=body, author=request.user).save()
            return render(request, "article_new.html", context={"success": ["Done!"]})
        else:
            errors.append("Form is not valid")

    return render(request, "article_new.html", context={"errors": errors})


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
                return render(request, "article_new.html", context={"errors": ["This title is not available"]})

            article.slug = slug
            article.title = title
            article.image = image
            article.body = body
            article.save()

            return redirect("/")
        else:
            errors.append("Form is not valid")

    return render(request, "article_edit.html", context={"article": article, "errors": errors})
