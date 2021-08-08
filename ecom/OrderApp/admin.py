from django.contrib import admin
from OrderApp.models import *
# Register your models here.
class Orderitemline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('customer', 'products','quantity', 'get_total')
    can_delete = False
    extra = 0

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','address','city','email','phone','zip_code','date_added']
    list_filter = ['city','date_added']
    search_fields = ['first_name','city','date_added']
    can_delete = False
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','date_order','pending','proccess','completed','cash_on_delivery','transaction_id']
    list_filter = ['completed','proccess','pending','date_order']
    search_fields = ['transaction_id']
    can_delete = False
    inlines = [Orderitemline]
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['products','order','quantity','date_added']
    list_filter = ['order','date_added']
    search_fields = ['date_added']
    can_delete = False
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','date_added']
    list_filter = ['user','name','email']
    search_fields = ['user','name','email']
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
