# Generated by Django 5.0.4 on 2024-04-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_assembly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(default=None, max_length=300)),
                ('images', models.ImageField(default=None, upload_to='photos', verbose_name='Фото')),
            ],
        ),
    ]
