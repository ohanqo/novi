# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    image = models.URLField()
    body = models.TextField()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles'
    )


class Comment(models.Model):
    body = models.TextField()

    article = models.ForeignKey(
        'Articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE
    )
