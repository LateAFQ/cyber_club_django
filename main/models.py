from django.db import models
from django.urls import reverse


class Text_Photo(models.Model):
    about_site = models.TextField(blank=True, default=None)
    image_for_carousel = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, verbose_name='Фото')
    logo = models.ImageField(upload_to='photos', default=None, blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Тексты и фото'
        verbose_name_plural = 'текст или фото'


class Price(models.Model):
    computer = models.CharField(blank=True, default=None, max_length=100, verbose_name="компьютеры")
    playstation = models.CharField(blank=True, default=None, max_length=100, verbose_name="плейстейшен")

    objects = models.Manager()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Assembly(models.Model):
    vip = models.CharField(blank=True, default=None, max_length=100)
    main = models.CharField(blank=True, default=None, max_length=100)
    ps = models.CharField(blank=True, default=None, max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Сборка пк'
        verbose_name_plural = 'Сборки пк'


class Vacancies(models.Model):
    header = models.CharField(default=None, max_length=100, verbose_name="заголовок")
    description = models.TextField(default=None, max_length=300, verbose_name="описание")
    images = models.ImageField(upload_to='photos', default=None, verbose_name='Фото')
    flt = models.ForeignKey('Filters', on_delete=models.PROTECT, related_name='filters', verbose_name="фильтры",
                             default=1)

    objects = models.Manager()

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


class Filters(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="фильтр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('filters', kwargs={'fil_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильтр'
        verbose_name_plural = 'Фильтры'