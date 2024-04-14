from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Text_Photo)
class Text_Image_Admin(admin.ModelAdmin):
    list_display = ('id', 'about_site', 'image_for_carousel', 'logo', 'is_published')
    list_display_links = ('id', 'about_site', 'image_for_carousel')


@admin.register(Price)
class Price_Admin(admin.ModelAdmin):
    list_display = ('id', 'computer', 'playstation')
    list_display_links = ('id', 'computer', 'playstation')


@admin.register(Assembly)
class Assembly_Admin(admin.ModelAdmin):
    list_display = ('id', 'vip', 'main', 'ps')
    list_display_links = ('id', 'vip', 'main')


@admin.register(Vacancies)
class Vacancies_Admin(admin.ModelAdmin):
    list_display = ('id', 'header', 'description', 'images')
    list_display_links = ('id', 'header', 'description', 'images')