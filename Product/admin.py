from django.contrib import admin

from .models import *

# Register your models here.




admin.site.register(Category)

 

class productImageInline(admin.TabularInline):
    model =Images
    extra =3
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','title', 'status','created_at', 'updated_at','now_price','amount','image_tag','feature']
    list_filter=['title','created_at']
    list_per_page =10
    search_fields =['title','now_price','detail']
    inlines=[productImageInline]
    prepopulated_fields ={'slug':('title',)}
class ImageAdmin(admin.ModelAdmin):
    list_display =['id','title', 'image_tag']
    list_filter=['title']
    list_per_page =10
    search_fields =['title']
admin.site.register(product,ProductAdmin)
admin.site.register(Images,ImageAdmin)

