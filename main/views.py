from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from main.models import Text_Photo, Price, Assembly, Vacancies
from django.views.decorators.cache import cache_page
from .models import Filters




@cache_page(60*15)
# Create your views here.
def page_home(request):
    txt_img = get_object_or_404 (Text_Photo, pk=1)
    carousel = Text_Photo.objects.filter (is_published=True)

    data = {
        'logo': txt_img,
        'carousel': carousel,
        'about_site': txt_img,
    }
    return render(request, 'main/index.html', context=data)


def page_price(request):
    price = Price.objects.all()
    data = {
        'price': price,
    }

    return render(request, 'main/price.html', context=data)


def page_assembly(request):
    computers = Assembly.objects.all()

    data = {
        'computers': computers,
    }

    return render(request, 'main/computers.html', context=data)


@cache_page(60*15)
def page_vacancies(request):
    vacancies = Vacancies.objects.all()
    flt = Filters.objects.all()

    data = {
        'flt': flt,
        'vacancies': vacancies,
    }

    return render(request, 'main/vacancies.html', context=data)


@login_required
def page_profile(request):
    return render(request, 'main/profile.html')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('home')


def show_category(request, fil_slug):
    filters = get_object_or_404(Filters, slug=fil_slug)
    vcs = Vacancies.objects.filter(flt_id=filters.pk)
    flt = Filters.objects.all()

    data = {
        'flt': flt,
        'vacancies': vcs,
    }

    return render(request, 'main/vacancies.html', context=data)


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')