from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.page_home, name='home'),
    path('price/', views.page_price, name='price'),
    path('assembly/', views.page_assembly, name='assembly'),
    path('vacancies/', views.page_vacancies, name='vacancies'),
    path('profile/', views.page_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
