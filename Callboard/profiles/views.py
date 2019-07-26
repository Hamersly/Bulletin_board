from django.shortcuts import render
from .models import Profile
from django.views.generic import DetailView

class ProfileDetail(DetailView):
    # '''Профиль пользователя'''
    model = Profile
    template_name = 'profile/user-detail.html'
