from django.db import models

from phonenumber_field.modelfields import PhoneNumberField



# 1
class Services(models.Model):
    # Services_orthodontics = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_implantology = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_functional_dentistry = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_orthopedics = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_periodontology = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_therapy = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_surgery = models.CharField(max_length=50, verbose_name='Название услуги')
    Services_title = models.CharField(max_length=100, verbose_name='Название услуги')
    Services_webp = models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images/webp', verbose_name='WEBP-изображение услуги')
    Services_gallery = models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images', verbose_name='Обычное изображение услуги')

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
        ordering = ['id']
        
        
# 2
class Actions(models.Model):
    Actions_title = models.CharField(max_length=100, verbose_name='Название акции')
    Actions_webp = models.ImageField(blank=True, null=True, upload_to='images/actions_gallery_images/webp', verbose_name='WEBP-изображение акции')
    Actions_gallery = models.ImageField(blank=True, null=True, upload_to='images/actions_gallery_images', verbose_name='Обычное изображение акции')

    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"
        ordering = ['id']
        
        
# 3
class Gallery(models.Model):
    Gallery_title = models.CharField(max_length=100)
    Gallery_photo_gallery = models.ImageField(upload_to='images/gallery_images')

    class Meta:
        verbose_name = "Галерея работ"
        verbose_name_plural = "Галерея работ"
        
        
# 4
class Reviews(models.Model):
    Reviews_yandex = models.CharField(max_length=50)
    Reviews_google = models.CharField(max_length=50)
    Reviews_zoon = models.CharField(max_length=50)
    Reviews_spr = models.CharField(max_length=50)
    Reviews_prodoctorov = models.CharField(max_length=50)
    Reviews_yell = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


# 4.1
class Reviews_Yandex(models.Model):
    Reviews_Yandex_yandex = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Yandex_full_name = models.CharField(max_length=50)
    Reviews_Yandex_review = models.CharField(max_length=1000)
    Reviews_Yandex_date = models.DateField()
    Reviews_Yandex_source = models.URLField(max_length = 200)
    Reviews_Yandex_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Яндекс"
        verbose_name_plural = "Отзывы Яндекс"


# 4.2
class Reviews_Google(models.Model):
    Reviews_Google_google = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Google_full_name = models.CharField(max_length=50)
    Reviews_Google_review = models.CharField(max_length=1000)
    Reviews_Google_date = models.DateField()
    Reviews_Google_source = models.URLField(max_length = 200)
    Reviews_Google_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Гугл"
        verbose_name_plural = "Отзывы Гугл"


# 4.3
class Reviews_Zoon(models.Model):
    Reviews_Zoon_zoon = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Zoon_full_name = models.CharField(max_length=50)
    Reviews_Zoon_review = models.CharField(max_length=1000)
    Reviews_Zoon_date = models.DateField()
    Reviews_Zoon_source = models.URLField(max_length = 200)
    Reviews_Zoon_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Зун"
        verbose_name_plural = "Отзывы Зун"


# 4.4
class Reviews_Spr(models.Model):
    Reviews_Spr_spr = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Spr_full_name = models.CharField(max_length=50)
    Reviews_Spr_review = models.CharField(max_length=1000)
    Reviews_Spr_date = models.DateField()
    Reviews_Spr_source = models.URLField(max_length = 200)
    Reviews_Spr_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы СПР"
        verbose_name_plural = "Отзывы СПР"


# 4.5
class Reviews_Prodoctorov(models.Model):
    Reviews_Prodoctorov_prodoctorov = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Prodoctorov_full_name = models.CharField(max_length=50)
    Reviews_Prodoctorov_review = models.CharField(max_length=1000)
    Reviews_Prodoctorov_date = models.DateField()
    Reviews_Prodoctorov_source = models.URLField(max_length = 200)
    Reviews_Prodoctorov_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Продокторов"
        verbose_name_plural = "Отзывы Продокторов"


# 4.6
class Reviews_Yell(models.Model):
    Reviews_Yell_yell = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    Reviews_Yell_full_name = models.CharField(max_length=50)
    Reviews_Yell_review = models.CharField(max_length=1000)
    Reviews_Yell_date = models.DateField()
    Reviews_Yell_source = models.URLField(max_length = 200)
    Reviews_Yell_stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Йелл"
        verbose_name_plural = "Отзывы Йелл"
        
        
# 5
class Orthodontics(models.Model):
    Orthodontics_orthodontics = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Orthodontics_image = models.ImageField(upload_to='images/orthodontics_images')
    Orthodontics_title = models.CharField(max_length=50)
    Orthodontics_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Ортодонтия"
        verbose_name_plural = "Ортодонтия"


# 6
class Implantology(models.Model):
    Implantology_implantology = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Implantology_image = models.ImageField(upload_to='images/implantology_images')
    Implantology_title = models.CharField(max_length=50)
    Implantology_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Имплантология"
        verbose_name_plural = "Имплантология"
        
        
# 7
class Functional_Dentistry(models.Model):
    Functional_Dentistry_functional_dentistry = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Functional_Dentistry_image = models.ImageField(upload_to='images/functional_dentistry_images')
    Functional_Dentistry_title = models.CharField(max_length=50)
    Functional_Dentistry_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Функциональная стоматология"
        verbose_name_plural = "Функциональная стоматология"


# 8
class Orthopedics(models.Model):
    Orthopedics_orthopedics = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Orthopedics_image = models.ImageField(upload_to='images/orthopedics_images')
    Orthopedics_title = models.CharField(max_length=50)
    Orthopedics_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Ортопедия"
        verbose_name_plural = "Ортопедия"
        
        
# 9
class Periodontology(models.Model):
    Periodontology_periodontology = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Periodontology_image = models.ImageField(upload_to='images/periodontology_images')
    Periodontology_title = models.CharField(max_length=50)
    Periodontology_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Парадонтология"
        verbose_name_plural = "Парадонтология"
        
        
# 10
class Therapy(models.Model):
    Therapy_therapy = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Therapy_image = models.ImageField(upload_to='images/therapy_images')
    Therapy_title = models.CharField(max_length=50)
    Therapy_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Терапия"
        verbose_name_plural = "Терапия"
        
        
# 11
class Surgery(models.Model):
    Surgery_surgery = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    Surgery_image = models.ImageField(upload_to='images/surgery_images')
    Surgery_title = models.CharField(max_length=50)
    Surgery_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Хирургия"
        verbose_name_plural = "Хирургия"
        
        
# 12
class Doctors(models.Model):
    Doctors_name = models.CharField(max_length=30)
    Doctors_surname = models.CharField(max_length=50)
    Doctors_middle_name = models.CharField(max_length=50)
    Doctors_photo = models.ImageField(upload_to='images/doctors_images')
    Doctors_about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Доктора"
        verbose_name_plural = "Доктора"


class Instagram_Links(models.Model):
    Instagram_Links_title = models.CharField(max_length=100)
    Instagram_Links_images = models.ImageField(upload_to='images/instagram_links_images')
    Instagram_Links_link = models.URLField(max_length = 200)

    class Meta:
        verbose_name = "Наш инстаграм"
        verbose_name_plural = "Наш инстаграм"

class Feedback(models.Model):
    Feedback_name = models.CharField(max_length=50)
    Feedback_phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

class Make_An_Appointment(models.Model):
    Make_An_Appointment_name = models.CharField(max_length=50)
    Make_An_Appointment_phone = PhoneNumberField(null=False, blank=False, unique=True)
    Make_An_Appointment_mail = models.EmailField(max_length = 254)

    class Meta:
        verbose_name = "Запись на приём"
        verbose_name_plural = "Запись на приём"