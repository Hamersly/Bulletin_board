from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, FilterAdvets, DateAdvets, Advert

@admin.register(Category)


class CategoryAdmin(MPTTModelAdmin):
    # '''Категории'''
    list_display = ('name','id')
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FilterAdvets)


class FilterAdvertsAdmin(admin.ModelAdmin):
    # '''Фильтры'''
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DateAdvets)


class DateAdvetsAdmin(admin.ModelAdmin):
    # '''Срок объявления''
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Advert)


class AdvertAdmin(admin.ModelAdmin):
    # '''Объявления''
    list_display = ('id', 'subject', 'user', 'category', 'filters', 'date', 'price', 'created', 'moderation')
    list_display_links = ('subject',)
    list_filter = ('user', 'category', 'filters', 'date', 'price')
    prepopulated_fields = {'slug': ('user', 'subject')}
