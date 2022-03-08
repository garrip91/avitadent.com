from django.contrib import admin

from .models import Services, Actions

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
    list_display = ('Services_title', 'Services_webp', 'get_image')
    readonly_fields = ('get_image',)
    
    
class ActionsAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Actions
        
    # list_display = ('author', 'comment', 'film')
    # list_editable = ('travel_time',)
    
    # def get_short_comment(self, obj):
        # return F'{obj.comment[:100]}...'
    # get_short_comment.short_description = 'comment'
    
    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Actions_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    #list_display = ('Actions_title', 'Actions_gallery')
    list_display = ('Actions_title', 'Actions_webp', 'get_image')
    #readonly_fields = ('Actions_gallery',)
    readonly_fields = ('get_image',)
    
    
admin.site.register(Services, ServicesAdmin)
admin.site.register(Actions, ActionsAdmin)