from django.db import models
from Product.models import product
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_order=models.DateField(auto_now_add=True)
    pending=models.BooleanField(default=False)
    proccess=models.BooleanField(default=False)
    completed=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200,null=True)
    cash_on_delivery=models.BooleanField(default=False) 

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
  
    
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    products = models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.quantity * self.products.now_price
        return total

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    email = models.EmailField()
    phone =models.CharField(max_length=11)
    zip_code = models.CharField(max_length=5)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name
          