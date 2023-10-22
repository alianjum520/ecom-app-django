from django.contrib import admin
from .models import *

# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display =['id','title','created_at', 'updated_at','address','email','contact','image_tag']
    list_filter=['title','created_at']
    list_per_page =10
    search_fields =['title','contact']
class CarouselAdmin(admin.ModelAdmin):
    list_display =['title','created_at', 'updated_at','sale_amount','type','keywords','image_tag']
    list_filter=['title','created_at']
    list_per_page =10
    search_fields =['title','keyword']
class bannerAdmin(admin.ModelAdmin):
    list_display =['title','created_at', 'updated_at','image_tag']
    list_filter=['title','created_at']
    list_per_page =10
    search_fields =['title','id']
class AboutAdmin(admin.ModelAdmin):
    list_display =['title','Designation','email','image_tag']
    list_filter=['title','Designation']
    list_per_page =10
    search_fields =['title','email']

class AboutAdmin2(admin.ModelAdmin):
    list_display =['id','description2']
    list_per_page =10
class ContactAdmin(admin.ModelAdmin):
    list_display =['name','email','subject','messages','created_at', 'updated_at','status']
    list_filter=['name','email']
    list_per_page =10
    search_fields=['name','subject']

admin.site.register(web_settings,SettingsAdmin)
admin.site.register(carousel,CarouselAdmin)
admin.site.register(Banner,bannerAdmin)
admin.site.register(About_Name,AboutAdmin)
admin.site.register(About_Us,AboutAdmin2)
admin.site.register(Contact,ContactAdmin)