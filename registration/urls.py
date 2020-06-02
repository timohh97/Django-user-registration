from django.urls import path
from . import views

urlpatterns = [
    path('', views.validateForm, name="index"),
    path('login/',views.showLogin,name="login")
]

