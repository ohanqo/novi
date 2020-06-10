from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/new", views.new, name="article_new"),
    path("article/<slug:slug>", views.show, name="article_show"),
    path("article/<slug:slug>/edit", views.edit, name="article_edit"),
    path("article/<slug:slug>/delete", views.delete, name="article_delete"),
    path("article/<slug:slug>/favorite",
         views.favorite, name="article_favorite"),
    path("article/<slug:slug>/unfavorite",
         views.unfavorite, name="article_unfavorite"),
]
