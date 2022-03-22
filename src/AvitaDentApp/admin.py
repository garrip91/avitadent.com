from django.contrib import admin

from .models import Services, Actions, Feedback, Gallery, Reviews, Orthodontics, Implantology, FunctionalDentistry, Orthopedics, Periodontology, Therapy, Surgery, Doctors, Certificates

from django.utils.safestring import mark_safe



# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Services
        
    # list_display = ('author', 'comment', 'film')
    # list_editable = ('travel_time',)
    
    # def get_short_comment(self, obj):
        # return F'{obj.comment[:100]}...'
    # get_short_comment.short_description = 'comment'
    
    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Services_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'
    
    #list_display = ('Services_title', 'Services_webp', 'Services_gallery')
    list_display = ('Services_title', 'Services_webp', 'get_image', 'id')
    readonly_fields = ('get_image',)
    
    
class ActionsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Actions

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Actions_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Actions_title', 'Actions_webp', 'get_image', 'id')
    readonly_fields = ('get_image',)
    
    
class FeedbackAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Feedback

    list_display = ('Feedback_name', 'Feedback_phone', 'id')
    
    
class GalleryAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Gallery

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Gallery_photo_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Gallery_title', 'Gallery_webp', 'get_image', 'id')
    readonly_fields = ('get_image',)
    
    
class ReviewsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Reviews

    list_display = ('Reviews_name', 'Reviews_date', 'Reviews_source', 'Reviews_text', 'id')
    
    
class OrthodonticsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Orthodontics

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Orthodontics_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Orthodontics_title', 'Orthodontics_webp', 'Orthodontics_image', 'get_image', 'Orthodontics_IntegerField')
    readonly_fields = ('get_image',)
    
    
class ImplantologyAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Implantology

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Implantology_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Implantology_title', 'Implantology_webp', 'Implantology_image', 'get_image', 'Implantology_IntegerField')
    readonly_fields = ('get_image',)
    
    
class FunctionalDentistryAdmin(admin.ModelAdmin):
    
    class Meta:
        model = FunctionalDentistry

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.FunctionalDentistry_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('FunctionalDentistry_title', 'FunctionalDentistry_webp', 'FunctionalDentistry_image', 'get_image', 'FunctionalDentistry_IntegerField')
    readonly_fields = ('get_image',)
    
    
class OrthopedicsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Orthopedics

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Orthopedics_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Orthopedics_title', 'Orthopedics_webp', 'Orthopedics_image', 'get_image', 'Orthopedics_IntegerField')
    readonly_fields = ('get_image',)
    
    
class PeriodontologyAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Periodontology

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Periodontology_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Periodontology_title', 'Periodontology_webp', 'Periodontology_image', 'get_image', 'Periodontology_IntegerField')
    readonly_fields = ('get_image',)
    
    
class TherapyAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Therapy

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Therapy_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Therapy_title', 'Therapy_webp', 'Therapy_image', 'get_image', 'Therapy_IntegerField')
    readonly_fields = ('get_image',)
    
    
class SurgeryAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Surgery

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Surgery_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Surgery_title', 'Surgery_webp', 'Surgery_image', 'get_image', 'Surgery_IntegerField')
    readonly_fields = ('get_image',)
    

class DoctorsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Doctors

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Doctors_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Doctors_name', 'Doctors_about', 'Doctors_webp', 'Doctors_image', 'get_image', 'id')
    readonly_fields = ('get_image',)


class CertificatesAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Certificates

    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Certificates_image.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Certificates_title', 'Certificates_a_href', 'Certificates_webp', 'Certificates_image', 'get_image', 'id')
    readonly_fields = ('get_image',)


admin.site.register(Services, ServicesAdmin)
admin.site.register(Actions, ActionsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Orthodontics, OrthodonticsAdmin)
admin.site.register(Implantology, ImplantologyAdmin)
admin.site.register(FunctionalDentistry, FunctionalDentistryAdmin)
admin.site.register(Orthopedics, OrthopedicsAdmin)
admin.site.register(Periodontology, PeriodontologyAdmin)
admin.site.register(Therapy, TherapyAdmin)
admin.site.register(Surgery, SurgeryAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Certificates, CertificatesAdmin)