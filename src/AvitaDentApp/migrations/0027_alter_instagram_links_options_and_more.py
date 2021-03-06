# Generated by Django 4.0.3 on 2022-03-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0026_rename_appointment_mail_appointment_appointment_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagram_links',
            options={'ordering': ['id'], 'verbose_name': 'Наш инстаграм', 'verbose_name_plural': 'Наш инстаграм'},
        ),
        migrations.AlterField(
            model_name='instagram_links',
            name='Instagram_Links_link',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='instagram_links',
            name='Instagram_Links_title',
            field=models.CharField(max_length=200),
        ),
    ]
