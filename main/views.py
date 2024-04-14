from django.shortcuts import render, get_object_or_404

from main.models import Text_Photo, Price, Assembly, Vacancies

txt_img = get_object_or_404(Text_Photo, pk=1)
carousel = Text_Photo.objects.filter(is_published=True)


# Create your views here.
def page_home(request):
    data = {
        'logo': txt_img,
        'carousel': carousel,
        'about_site': txt_img,
    }
    return render(request, 'main/index.html', context=data)


def page_price(request):
    price = Price.objects.all()
    data = {
        'logo': txt_img,
        'carousel': carousel,
        'about_site': txt_img,
        'price': price,
    }

    return render(request, 'main/price.html', context=data)


def page_assembly(request):
    computers = Assembly.objects.all()

    data = {
        'logo': txt_img,
        'carousel': carousel,
        'about_site': txt_img,
        'computers': computers,
    }

    return render(request, 'main/computers.html', context=data)


def page_vacancies(request):
    vacancies = Vacancies.objects.all()

    data = {
        'logo': txt_img,
        'carousel': carousel,
        'about_site': txt_img,
        'vacancies': vacancies,
    }

    return render(request, 'main/vacancies.html', context=data)