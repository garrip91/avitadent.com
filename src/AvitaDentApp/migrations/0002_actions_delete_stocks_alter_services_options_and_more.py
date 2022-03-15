# Generated by Django 4.0.3 on 2022-03-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvitaDentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actions_title', models.CharField(max_length=100, verbose_name='Название акции')),
                ('Actions_webp', models.ImageField(upload_to='images/actions_gallery_images/webp', verbose_name='WEBP-изображение акции')),
                ('Actions_gallery', models.ImageField(upload_to='images/actions_gallery_images', verbose_name='Обычное изображение акции')),
            ],
            options={
                'verbose_name': 'Акции',
                'verbose_name_plural': 'Акции',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['id'], 'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_functional_dentistry',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_implantology',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_orthodontics',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_orthopedics',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_periodontology',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_surgery',
        ),
        migrations.RemoveField(
            model_name='services',
            name='Services_therapy',
        ),
        migrations.AddField(
            model_name='services',
            name='Services_gallery',
            field=models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images', verbose_name='Обычное изображение услуги'),
        ),
        migrations.AddField(
            model_name='services',
            name='Services_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название услуги'),
        ),
        migrations.AddField(
            model_name='services',
            name='Services_webp',
            field=models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images/webp', verbose_name='WEBP-изображение услуги'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Doctors_photo',
            field=models.ImageField(upload_to='images/doctors_images'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Feedback_phone',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='functional_dentistry',
            name='Functional_Dentistry_image',
            field=models.ImageField(upload_to='images/functional_dentistry_images'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Gallery_photo_gallery',
            field=models.ImageField(upload_to='images/gallery_images'),
        ),
        migrations.AlterField(
            model_name='implantology',
            name='Implantology_image',
            field=models.ImageField(upload_to='images/implantology_images'),
        ),
        migrations.AlterField(
            model_name='instagram_links',
            name='Instagram_Links_images',
            field=models.ImageField(upload_to='images/instagram_links_images'),
        ),
        migrations.AlterField(
            model_name='orthodontics',
            name='Orthodontics_image',
            field=models.ImageField(upload_to='images/orthodontics_images'),
        ),
        migrations.AlterField(
            model_name='orthopedics',
            name='Orthopedics_image',
            field=models.ImageField(upload_to='images/orthopedics_images'),
        ),
        migrations.AlterField(
            model_name='periodontology',
            name='Periodontology_image',
            field=models.ImageField(upload_to='images/periodontology_images'),
        ),
        migrations.AlterField(
            model_name='surgery',
            name='Surgery_image',
            field=models.ImageField(upload_to='images/surgery_images'),
        ),
        migrations.AlterField(
            model_name='therapy',
            name='Therapy_image',
            field=models.ImageField(upload_to='images/therapy_images'),
        ),
    ]