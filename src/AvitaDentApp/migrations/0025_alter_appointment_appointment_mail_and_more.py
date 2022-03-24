# Generated by Django 4.0.3 on 2022-03-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0024_appointment_delete_make_an_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_mail',
            field=models.EmailField(max_length=254, verbose_name='Почта отправителя'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_name',
            field=models.CharField(max_length=50, verbose_name='Ф.И.О. отправителя'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_phone',
            field=models.CharField(max_length=18, verbose_name='Телефон отправителя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Feedback_name',
            field=models.CharField(max_length=50, verbose_name='Ф.И.О. отправителя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Feedback_phone',
            field=models.CharField(max_length=18, verbose_name='Телефон отправителя'),
        ),
    ]