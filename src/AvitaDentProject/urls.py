"""AvitaDentProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AvitaDentApp.views import HomePageView, ServicesPageView, ActionsPageView, GalleryPageView, ClinicPageView, ReviewsPageView, ContactsPageView, OrthodonticsPageView, ImplantologyPageView, FunctionalDentistryPageView, OrthopedicsPageView, PeriodontologyPageView, TherapyPageView, SurgeryPageView, CertificatesAndLicensesPageView, PrivacyPolicyPageView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'), # AvitaDent
    path('services/', ServicesPageView.as_view(), name='services'), # Услуги
    path('actions/', ActionsPageView.as_view(), name='actions'), # Акции
    path('gallery/', GalleryPageView.as_view(), name='gallery'), # Работы
    path('clinic-page/', ClinicPageView.as_view(), name='clinic-page'), # О клинике
    path('reviews/', ReviewsPageView.as_view(), name='reviews'), # Отзывы
    path('contacts/', ContactsPageView.as_view(), name='contacts'), # Контакты
    path('orthodontics/', OrthodonticsPageView.as_view(), name='orthodontics'), # Ортодонтия
    path('implantology/', ImplantologyPageView.as_view(), name='implantology'), # Имплантология
    path('functional-dentistry/', FunctionalDentistryPageView.as_view(), name='functional-dentistry'), # Функциональная стоматология
    path('orthopedics/', OrthopedicsPageView.as_view(), name='orthopedics'), # Ортопедия
    path('periodontology/', PeriodontologyPageView.as_view(), name='periodontology'), # Парадонтология
    path('therapy/', TherapyPageView.as_view(), name='therapy'), # Терапия
    path('surgery/', SurgeryPageView.as_view(), name='surgery'), # Хирургия
    path('certificates-and-licenses/', CertificatesAndLicensesPageView.as_view(), name='certificates-and-licenses'), # Сертификаты и лицензии
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy-policy'), # Политика конфиденциальности
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
