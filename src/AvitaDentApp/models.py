from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Doctors(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='../static/images/doctors_images')
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Доктора"
        verbose_name_plural = "Доктора"

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    photo_gallery = models.ImageField(upload_to='../static/images/gallery_images')

    class Meta:
        verbose_name = "Галерея работ"
        verbose_name_plural = "Галерея работ"

class Services(models.Model):
    orthodontics = models.CharField(max_length=50)
    implantology = models.CharField(max_length=50)
    functional_dentistry = models.CharField(max_length=50, related_name = 'Services_functional_dentistry')
    orthopedics = models.CharField(max_length=50)
    therapy = models.CharField(max_length=50)
    periodontology = models.CharField(max_length=50)
    surgery = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

class Orthodontics(models.Model):
    orthodontics = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/orthodontics_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Ортодонтия"
        verbose_name_plural = "Ортодонтия"

class Implantology(models.Model):
    implantology = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/implantology_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Имплантология"
        verbose_name_plural = "Имплантология"

class Functional_Dentistry(models.Model):
    functional_dentistry = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True, related_name = 'Functional_Dentistry_functional_dentistry')
    image = models.ImageField(upload_to='../static/images/functional_dentistry_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Функциональная стоматология"
        verbose_name_plural = "Функциональная стоматология"

class Orthopedics(models.Model):
    orthopedics = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/orthopedics_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Ортопедия"
        verbose_name_plural = "Ортопедия"

class Therapy(models.Model):
    therapy = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/therapy_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Терапия"
        verbose_name_plural = "Терапия"

class Periodontology(models.Model):
    periodontology = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/periodontology_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Парадонтология"
        verbose_name_plural = "Парадонтология"

class Surgery(models.Model):
    surgery = models.OneToOneField(Services, on_delete = models.CASCADE, primary_key = True)
    image = models.ImageField(upload_to='../static/images/surgery_images')
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Хирургия"
        verbose_name_plural = "Хирургия"

class Stocks(models.Model):
    title = models.CharField(max_length=100)
    stocks_gallery = models.ImageField(upload_to='../static/images/stocks_gallery_images')

    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"

class Instagram_Links(models.Model):
    title = models.CharField(max_length=100)
    instagram_links_images = models.ImageField(upload_to='../static/images/instagram_links_images')
    link = models.URLField(max_length = 200)

    class Meta:
        verbose_name = "Наш инстаграм"
        verbose_name_plural = "Наш инстаграм"

class Reviews(models.Model):
    yandex = models.CharField(max_length=50)
    google = models.CharField(max_length=50)
    zoon = models.CharField(max_length=50)
    spr = models.CharField(max_length=50)
    prodoctorov = models.CharField(max_length=50)
    yell = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"

class Reviews_Yandex(models.Model):
    yandex = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Яндекс"
        verbose_name_plural = "Отзывы Яндекс"

class Reviews_Google(models.Model):
    google = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Гугл"
        verbose_name_plural = "Отзывы Гугл"

class Reviews_Zoon(models.Model):
    zoon = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Зун"
        verbose_name_plural = "Отзывы Зун"

class Reviews_Spr(models.Model):
    spr = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы СПР"
        verbose_name_plural = "Отзывы СПР"

class Reviews_Prodoctorov(models.Model):
    prodoctorov = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Продокторов"
        verbose_name_plural = "Отзывы Продокторов"

class Reviews_Yell(models.Model):
    yell = models.OneToOneField(Reviews, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    date = models.DateField()
    source = models.URLField(max_length = 200)
    stars = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Отзывы Йелл"
        verbose_name_plural = "Отзывы Йелл"

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

class Make_An_Appointment(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    mail = models.EmailField(max_length = 254)

    class Meta:
        verbose_name = "Запись на приём"
        verbose_name_plural = "Запись на приём"