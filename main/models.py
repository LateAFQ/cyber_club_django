from django.db import models


class Text_Photo(models.Model):
    about_site = models.TextField(blank=True, default=None)
    image_for_carousel = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, verbose_name='Фото')
    logo = models.ImageField(upload_to='photos', default=None, blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True)

    objects = models.Manager()


class Price(models.Model):
    computer = models.CharField(blank=True, default=None, max_length=100)
    playstation = models.CharField(blank=True, default=None, max_length=100)

    objects = models.Manager()


class Assembly(models.Model):
    vip = models.CharField(blank=True, default=None, max_length=100)
    main = models.CharField(blank=True, default=None, max_length=100)
    ps = models.CharField(blank=True, default=None, max_length=100)

    objects = models.Manager()


class Vacancies(models.Model):
    header = models.CharField(default=None, max_length=100)
    description = models.TextField(default=None, max_length=300)
    images = models.ImageField(upload_to='photos', default=None, verbose_name='Фото')

    objects = models.Manager()