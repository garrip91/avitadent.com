# Generated by Django 4.0.3 on 2022-03-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0020_certificates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='Certificates_title',
            field=models.CharField(max_length=100, verbose_name='Название изображения Сертификата'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Gallery_title',
            field=models.CharField(max_length=100, verbose_name='Название изображения галереи'),
        ),
    ]
