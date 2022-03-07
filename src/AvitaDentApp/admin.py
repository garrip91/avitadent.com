from django.contrib import admin

from .models import Services, Stocks



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
    
    list_display = ('Stocks_title', 'Stocks_gallery')
    
    
admin.site.register(Services, ServicesAdmin)
admin.site.register(Stocks, StocksAdmin)