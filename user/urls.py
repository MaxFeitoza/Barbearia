from django.urls import path, include
from user.views import UserCreateView

urlpatterns = [
    path("", UserCreateView.as_view(), name="user-create-view"),
]
