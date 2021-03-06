# Generated by Django 4.0.3 on 2022-03-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0008_alter_orthodontics_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='implantology',
            name='Implantology_about',
        ),
        migrations.RemoveField(
            model_name='implantology',
            name='Implantology_implantology',
        ),
        migrations.AddField(
            model_name='implantology',
            name='Implantology_IntegerField',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения'),
        ),
        migrations.AddField(
            model_name='implantology',
            name='Implantology_webp',
            field=models.ImageField(blank=True, null=True, upload_to='images/Implantology_images/webp', verbose_name='WEBP-изображение страницы Имплантология'),
        ),
        migrations.AlterField(
            model_name='implantology',
            name='Implantology_image',
            field=models.ImageField(upload_to='images/Implantology_images', verbose_name='Обычное изображение страницы Имплантология'),
        ),
        migrations.AlterField(
            model_name='implantology',
            name='Implantology_title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AvitaDentApp.services', verbose_name='Название Имплантологической УСЛУГИ'),
        ),
    ]
