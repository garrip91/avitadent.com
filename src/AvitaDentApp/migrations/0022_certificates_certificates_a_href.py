# Generated by Django 4.0.3 on 2022-03-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0021_alter_certificates_certificates_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='Certificates_a_href',
            field=models.ImageField(blank=True, null=True, upload_to='images/Certificates_images/url', verbose_name='Обычное изображение Сертификата ДЛЯ ССЫЛКИ'),
        ),
    ]
