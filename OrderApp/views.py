from django.shortcuts import render
from ecomApp.models import *
from Product.models import  *
from OrderApp.models import *
from django.http import JsonResponse
import json
import datetime
# Create your views here.
def cart(request):
    products =product.objects.all()
    setting=settings.objects.get(id=1)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,completed=False,proccess=False,pending=True)
        items = order.orderitem_set.all()
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
    context = {'products':products,'items':items,'order':order,'setting':setting}
    return render(request,'cart.html',context)
def checkout(request):
    setting=settings.objects.get(id=1)
    products =product.objects.all()
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,completed=False,proccess=False,pending=True)
        items = order.orderitem_set.all()
    else:
        items = []
        order={'get_cart_total':0,'get_cart_items':0}
    context={'setting':setting,'products':products,'items':items,'order':order}
    return render(request,'checkout.html',context)
def update_item(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('productId:',productId)
    print('action:',action)
    customer=request.user.customer
    products=product.objects.get(id=productId)
    order, created= Order.objects.get_or_create(customer=customer,completed=False,proccess=False,pending=True)
    orderItem, created= OrderItem.objects.get_or_create(order=order,products=products)
    if action =='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)
def processOrder(request):
    print('Data:', request.body)
    transaction_id=datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created= Order.objects.get_or_create(customer=customer,completed=False,proccess=False,pending=True)
        total = float(data['form']['total'])
        order.transaction_id=transaction_id
        if total==order.get_cart_total:
            order.proccess=True
        order.save()
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            first_name=data['form']['first_name'],
            last_name=data['form']['last_name'],
            address=data['form']['address'],
            city=data['form']['city'],
            email=data['form']['email'],
            phone=data['form']['phone'],
            zip_code=data['form']['zip_code'],
        
        
        )
    else:
        print("User is not logged in")
    return JsonResponse('Payment completed!',safe=False)