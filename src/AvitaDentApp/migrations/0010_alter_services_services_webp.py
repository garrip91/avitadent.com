# Generated by Django 4.0.3 on 2022-03-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0009_services_services_gallery_services_services_webp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Services_webp',
            field=models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images/webp', verbose_name='WEBP-изображение услуги'),
        ),
    ]