from django.urls import path

from . import views

urlpatterns = [
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/<int:followee_id>/follow", views.follow, name="follow"),
    path("profile/<int:follower_id>/unfollow", views.unfollow, name="unfollow"),
]
