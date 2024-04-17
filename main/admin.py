from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Text_Photo)
class Text_Image_Admin(admin.ModelAdmin):
    list_display = ('id', 'image_for_carousel', 'logo', 'is_published', 'brief_info')
    list_display_links = ('id', 'image_for_carousel')
    list_per_page = 5
    list_filter = ['id']

    @admin.display(description="Краткое описание", ordering='about_site')
    def brief_info(self, tp: Text_Photo):
        return f"Описание {len(tp.about_site)} символов."


@admin.register(Price)
class Price_Admin(admin.ModelAdmin):
    list_display = ('id', 'computer', 'playstation')
    list_display_links = ('id', 'computer', 'playstation')
    list_per_page = 5


@admin.register(Assembly)
class Assembly_Admin(admin.ModelAdmin):
    list_display = ('id', 'vip', 'main', 'ps')
    list_display_links = ('id', 'vip', 'main')
    list_per_page = 5


@admin.register(Vacancies)
class Vacancies_Admin(admin.ModelAdmin):
    list_display = ('id', 'header', 'description', 'images')
    list_display_links = ('id', 'header', 'description', 'images')
    list_per_page = 5


@admin.register(Filters)
class Filters_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    list_per_page = 5