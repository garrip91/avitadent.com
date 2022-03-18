from django.contrib import admin

from .models import Services, Actions, Feedback, Gallery, Reviews, Orthodontics

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
        return mark_safe(F'<img src={obj.Gallery_photo_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    list_display = ('Gallery_title', 'Gallery_webp', 'get_image', 'id')
    readonly_fields = ('get_image',)
    
    
admin.site.register(Services, ServicesAdmin)
admin.site.register(Actions, ActionsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Reviews, ReviewsAdmin)