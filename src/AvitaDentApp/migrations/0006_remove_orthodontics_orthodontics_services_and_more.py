# Generated by Django 4.0.3 on 2022-03-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0005_alter_orthodontics_orthodontics_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orthodontics',
            name='Orthodontics_Services',
        ),
        migrations.RemoveField(
            model_name='orthodontics',
            name='Orthodontics_about',
        ),
        migrations.AlterField(
            model_name='orthodontics',
            name='Orthodontics_title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AvitaDentApp.services', verbose_name='Название Ортодонтической УСЛУГИ'),
        ),
    ]
