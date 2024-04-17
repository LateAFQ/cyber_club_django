from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Text_Photo)
class Text_Image_Admin(admin.ModelAdmin):
    list_display = ('id', 'image_for_carousel', 'logo', 'is_published', 'brief_info')
    list_display_links = ('id', 'image_for_carousel')
    list_per_page = 5
    list_filter = ['id']
    list_editable = ['logo']

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

    @admin.action (description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        pass


@admin.register(Vacancies)
class Vacancies_Admin(admin.ModelAdmin):
    list_display = ('id', 'header', 'description', 'images')
    list_display_links = ('id', 'header', 'description', 'images')
    list_per_page = 5

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        pass


@admin.register(Filters)
class Filters_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')
    list_per_page = 5