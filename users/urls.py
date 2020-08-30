from django.urls import path

from .views import SignupPageView
# Create your views here.
urlPatters = [
    path('signup/', SignupPageView.as_view(), name='signup'), ]
