from django.contrib import admin

from .models import Services, Stocks

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
    
    list_display = ('Services_orthodontics', 'Services_implantology', 'Services_functional_dentistry', 'Services_orthopedics', 'Services_therapy', 'Services_periodontology', 'Services_surgery')
    
    
class StocksAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Stocks
        
    # list_display = ('author', 'comment', 'film')
    # list_editable = ('travel_time',)
    
    # def get_short_comment(self, obj):
        # return F'{obj.comment[:100]}...'
    # get_short_comment.short_description = 'comment'
    
    def get_image(self, obj):
        return mark_safe(F'<img src={obj.Stocks_gallery.url} width="100" height="100">')
    get_image.short_description = 'Изображение'    
    
    #list_display = ('Stocks_title', 'Stocks_gallery')
    list_display = ('Stocks_title', 'get_image')
    #readonly_fields = ('Stocks_gallery',)
    readonly_fields = ('get_image',)
    
    
admin.site.register(Services, ServicesAdmin)
admin.site.register(Stocks, StocksAdmin)