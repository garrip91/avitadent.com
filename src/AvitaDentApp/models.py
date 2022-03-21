from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from django.utils import timezone

# ДЛЯ ДОБАВЛЕНИЯ:
# blank=True, null=True


# 1
class Services(models.Model):
    
    # Services_orthodontics = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_implantology = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_functional_dentistry = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_orthopedics = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_periodontology = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_therapy = models.CharField(max_length=50, verbose_name='Название услуги')
    # Services_surgery = models.CharField(max_length=50, verbose_name='Название услуги')
    Services_title = models.CharField(blank=True, null=True, max_length=100, verbose_name='Название услуги')
    Services_webp = models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images/webp', verbose_name='WEBP-изображение услуги')
    Services_gallery = models.ImageField(blank=True, null=True, upload_to='images/services_gallery_images', verbose_name='Обычное изображение услуги')

    def __str__(self):
        return self.Services_title

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"
        ordering = ['id']
        
        
# 2
class Actions(models.Model):
    
    Actions_title = models.CharField(max_length=100, verbose_name='Название акции')
    Actions_webp = models.ImageField(upload_to='images/actions_gallery_images/webp', verbose_name='WEBP-изображение акции')
    Actions_gallery = models.ImageField(upload_to='images/actions_gallery_images', verbose_name='Обычное изображение акции')

    def __str__(self):
        return self.Actions_title

    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"
        ordering = ['id']
        
        
# 3
class Gallery(models.Model):
    
    Gallery_title = models.CharField(max_length=100)
    Gallery_webp = models.ImageField(blank=True, null=True, upload_to='images/gallery_gallery_images/webp', verbose_name='WEBP-изображение галереи')
    Gallery_photo_gallery = models.ImageField(upload_to='images/gallery_gallery_images', verbose_name='Обычное изображение галереи')

    def __str__(self):
        return self.Gallery_title

    class Meta:
        verbose_name = "Галерея работ"
        verbose_name_plural = "Галерея работ"
        ordering = ['id']
        
        
# 4
class Reviews(models.Model):
    
    # Reviews_yandex = models.CharField(max_length=50)
    # Reviews_google = models.CharField(max_length=50)
    # Reviews_zoon = models.CharField(max_length=50)
    # Reviews_spr = models.CharField(max_length=50)
    # Reviews_prodoctorov = models.CharField(max_length=50)
    # Reviews_yell = models.CharField(max_length=50)
    Reviews_name = models.CharField(blank=True, null=True, max_length=50, verbose_name='Автор отзыва')
    Reviews_date = models.CharField(blank=True, null=True, max_length=50, verbose_name='Дата отзыва')
    Reviews_source = models.CharField(blank=True, null=True, max_length=50, verbose_name='Источник отзыва')
    Reviews_text = models.CharField(blank=True, null=True, max_length=1000, verbose_name='Текст отзыва')

    def __str__(self):
        return self.Reviews_text

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
        ordering = ['id']


# 4.1
# class Reviews_Yandex(models.Model):
    # Reviews_Yandex_yandex = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Yandex_full_name = models.CharField(max_length=50)
    # Reviews_Yandex_review = models.CharField(max_length=1000)
    # Reviews_Yandex_date = models.DateField()
    # Reviews_Yandex_source = models.URLField(max_length = 200)
    # Reviews_Yandex_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы Яндекс"
        # verbose_name_plural = "Отзывы Яндекс"


# 4.2
# class Reviews_Google(models.Model):
    # Reviews_Google_google = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Google_full_name = models.CharField(max_length=50)
    # Reviews_Google_review = models.CharField(max_length=1000)
    # Reviews_Google_date = models.DateField()
    # Reviews_Google_source = models.URLField(max_length = 200)
    # Reviews_Google_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы Гугл"
        # verbose_name_plural = "Отзывы Гугл"


# 4.3
# class Reviews_Zoon(models.Model):
    # Reviews_Zoon_zoon = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Zoon_full_name = models.CharField(max_length=50)
    # Reviews_Zoon_review = models.CharField(max_length=1000)
    # Reviews_Zoon_date = models.DateField()
    # Reviews_Zoon_source = models.URLField(max_length = 200)
    # Reviews_Zoon_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы Зун"
        # verbose_name_plural = "Отзывы Зун"


# 4.4
# class Reviews_Spr(models.Model):
    # Reviews_Spr_spr = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Spr_full_name = models.CharField(max_length=50)
    # Reviews_Spr_review = models.CharField(max_length=1000)
    # Reviews_Spr_date = models.DateField()
    # Reviews_Spr_source = models.URLField(max_length = 200)
    # Reviews_Spr_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы СПР"
        # verbose_name_plural = "Отзывы СПР"


# 4.5
# class Reviews_Prodoctorov(models.Model):
    # Reviews_Prodoctorov_prodoctorov = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Prodoctorov_full_name = models.CharField(max_length=50)
    # Reviews_Prodoctorov_review = models.CharField(max_length=1000)
    # Reviews_Prodoctorov_date = models.DateField()
    # Reviews_Prodoctorov_source = models.URLField(max_length = 200)
    # Reviews_Prodoctorov_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы Продокторов"
        # verbose_name_plural = "Отзывы Продокторов"


# 4.6
# class Reviews_Yell(models.Model):
    # Reviews_Yell_yell = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    # Reviews_Yell_full_name = models.CharField(max_length=50)
    # Reviews_Yell_review = models.CharField(max_length=1000)
    # Reviews_Yell_date = models.DateField()
    # Reviews_Yell_source = models.URLField(max_length = 200)
    # Reviews_Yell_stars = models.IntegerField(default=0)

    # class Meta:
        # verbose_name = "Отзывы Йелл"
        # verbose_name_plural = "Отзывы Йелл"
        
        
# 5
class Orthodontics(models.Model):

    Orthodontics_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    Orthodontics_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название Ортодонтической УСЛУГИ')
    Orthodontics_webp = models.ImageField(blank=True, null=True, upload_to='images/Orthodontics_images/webp', verbose_name='WEBP-изображение страницы Ортодонтия')
    Orthodontics_image = models.ImageField(upload_to='images/Orthodontics_images', verbose_name='Обычное изображение страницы Ортодонтия')
    #Orthodontics_datetime = models.DateTimeField('Дата и время создания записи', default=timezone.now)

    def __str__(self):
        return str(self.Orthodontics_title)

    class Meta:
        verbose_name = "Ортодонтия"
        verbose_name_plural = "Ортодонтия"
        ordering = ['Orthodontics_IntegerField']


# 6
class Implantology(models.Model):
    
    Implantology_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    Implantology_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название Имплантологической УСЛУГИ')
    Implantology_webp = models.ImageField(blank=True, null=True, upload_to='images/Implantology_images/webp', verbose_name='WEBP-изображение страницы Имплантология')
    Implantology_image = models.ImageField(upload_to='images/Implantology_images', verbose_name='Обычное изображение страницы Имплантология')

    def __str__(self):
        return str(self.Implantology_title)

    class Meta:
        verbose_name = "Имплантология"
        verbose_name_plural = "Имплантология"
        ordering = ['Implantology_IntegerField']
        
        
# 7
class FunctionalDentistry(models.Model):
    
    FunctionalDentistry_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    FunctionalDentistry_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название УСЛУГИ Функциональной стоматологии')
    FunctionalDentistry_webp = models.ImageField(blank=True, null=True, upload_to='images/Functional_Dentistry_images/webp', verbose_name='WEBP-изображение страницы Функциональная стоматология')
    FunctionalDentistry_image = models.ImageField(upload_to='images/Functional_Dentistry_images', verbose_name='Обычное изображение страницы Функциональная стоматология')

    def __str__(self):
        return str(self.FunctionalDentistry_title)

    class Meta:
        verbose_name = "Функциональная стоматология"
        verbose_name_plural = "Функциональная стоматология"
        ordering = ['FunctionalDentistry_IntegerField']


# 8
class Orthopedics(models.Model):
    
    Orthopedics_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    Orthopedics_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название УСЛУГИ Ортопедия')
    Orthopedics_webp = models.ImageField(blank=True, null=True, upload_to='images/Orthopedics_images/webp', verbose_name='WEBP-изображение страницы Ортопедия')
    Orthopedics_image = models.ImageField(upload_to='images/Orthopedics_images', verbose_name='Обычное изображение страницы Ортопедия')

    def __str__(self):
        return str(self.Orthopedics_title)

    class Meta:
        verbose_name = "Ортопедия"
        verbose_name_plural = "Ортопедия"
        ordering = ['Orthopedics_IntegerField']
        
        
# 9
class Periodontology(models.Model):
    
    Periodontology_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    Periodontology_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название УСЛУГИ Парадонтология')
    Periodontology_webp = models.ImageField(blank=True, null=True, upload_to='images/Periodontology_images/webp', verbose_name='WEBP-изображение страницы Парадонтология')
    Periodontology_image = models.ImageField(upload_to='images/Periodontology_images', verbose_name='Обычное изображение страницы Парадонтология')

    def __str__(self):
        return str(self.Periodontology_title)

    class Meta:
        verbose_name = "Парадонтология"
        verbose_name_plural = "Парадонтология"
        ordering = ['Periodontology_IntegerField']
        
        
# 10
class Therapy(models.Model):
    
    Therapy_IntegerField = models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер для ручного внесения')
    Therapy_title = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, verbose_name='Название УСЛУГИ Терапия')
    Therapy_webp = models.ImageField(blank=True, null=True, upload_to='images/Therapy_images/webp', verbose_name='WEBP-изображение страницы Терапия')
    Therapy_image = models.ImageField(upload_to='images/Therapy_images', verbose_name='Обычное изображение страницы Терапия')

    def __str__(self):
        return str(self.Therapy_title)

    class Meta:
        verbose_name = "Терапия"
        verbose_name_plural = "Терапия"
        ordering = ['Therapy_IntegerField']
        
        
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
    #Feedback_phone = PhoneNumberField(null=False, blank=False, unique=True)
    Feedback_phone = models.CharField(max_length=18, unique=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        ordering = ['id']

class Make_An_Appointment(models.Model):
    
    Make_An_Appointment_name = models.CharField(max_length=50)
    Make_An_Appointment_phone = PhoneNumberField(null=False, blank=False, unique=True)
    Make_An_Appointment_mail = models.EmailField(max_length = 254)

    class Meta:
        verbose_name = "Запись на приём"
        verbose_name_plural = "Запись на приём"