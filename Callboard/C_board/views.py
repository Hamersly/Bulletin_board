from django.shortcuts import render
from .models import Advert
from django.views.generic import ListView, DetailView

class AdvertList(ListView):
    # '''Все объявления'''
    model = Advert
    queryset = Advert.objects.all()
    template_name = 'C_board/advert_list.html'


class AdvertDetail(DetailView):
    # '''Подробно об объявлении'''
    model = Advert
    context_object_name = 'advert'
    template_name = 'C_board/advert_detail.html'