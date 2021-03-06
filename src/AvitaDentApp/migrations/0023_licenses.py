# Generated by Django 4.0.3 on 2022-03-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0022_certificates_certificates_a_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Licenses_title', models.CharField(max_length=100, verbose_name='Название изображения Лицензии')),
                ('Licenses_a_href', models.ImageField(blank=True, null=True, upload_to='images/Licenses_images/url', verbose_name='Обычное изображение Лицензии ДЛЯ ССЫЛКИ')),
                ('Licenses_webp', models.ImageField(upload_to='images/Licenses_images/webp', verbose_name='WEBP-изображение Лицензии')),
                ('Licenses_image', models.ImageField(upload_to='images/Licenses_images', verbose_name='Обычное изображение Лицензии')),
            ],
            options={
                'verbose_name': 'Лицензии',
                'verbose_name_plural': 'Лицензии',
                'ordering': ['id'],
            },
        ),
    ]
