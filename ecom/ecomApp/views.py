from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,HttpResponse,reverse
from ecomApp.models import *
from Product.models import  *
from ecomApp.forms import *

# Create your views here.
def Home(request):
    setting=settings.objects.get(id=1)
    slider = carousel.objects.all() 
    banner1 = Banner.objects.get(id=1)
    banner2 = Banner.objects.get(id=2)
    banner3 = Banner.objects.get(id=3)
    banner4 = Banner.objects.get(id=4)
    banner5 = Banner.objects.get(id=5)
    latest_products =product.objects.all().order_by('-id')
    feature_products = product.objects.all().filter(feature='True')
    women_category = product.objects.all().filter(category_id=2)[:8]
    men_category = product.objects.all().filter(category_id=1)[:8]
    category =Category.objects.filter(parent=None)
    

    context={
        'setting':setting,
        'slider':slider,
        'banner1':banner1,
        'banner2':banner2,
        'banner3':banner3,
        'banner4':banner4,
        'banner5':banner5,
        'latest_products':latest_products,
        'feature_products':feature_products,
        'women_category': women_category,
        'men_category':men_category,
        'category':category,
        

    }
    return render(request,'index.html',context)
def about(request):
    setting=settings.objects.get(id=1)
    aboutus=About_Us.objects.all()
    category =Category.objects.filter(parent=None)
    context={
        'setting':setting,
        'aboutus':aboutus,
        'category':category
    }

    return render(request,'about_us.html',context)
def ProductView(request,id):
    setting=settings.objects.get(id=1)
    product_view = product.objects.get(id=id)
    category =Category.objects.filter(parent=None)
    images=Images.objects.filter(product_id=id)
    products=product.objects.all().order_by('id')[:4]

    context={
        'setting':setting,
        'product_view':product_view,
        'category':category,
        'images':images,
        'products':products,
    }
    return render(request,'product.html',context)
def CategoryView(request,slug):
    setting=settings.objects.get(id=1)
    category5=get_object_or_404(Category,slug=slug)
    products3 = category5.product23.filter()
    category =Category.objects.filter(parent=None)
   
    context={
        'setting':setting,
        'category5':category5,
        'products3':products3,
        'category':category
    }
    return render(request,'shop.html',context)
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data=Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.messages = form.cleaned_data['messages']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Your message has been sent')
            return HttpResponseRedirect(reverse('contact'))
    setting=settings.objects.get(id=1)
    form=ContactForm
    category =Category.objects.filter(parent=None)
    context={
        'setting':setting,
        'form':form,
        'category':category
    }
    return render(request,'contact.html',context)
def SearchView(request):
    if request.method == 'POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            query=form.cleaned['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products=product.objects.filter(title__icontains=query)
            else:
                products=product.objects.filter(title__icontains=query)
            category5=get_object_or_404(Category,slug=slug)
            products3 = category5.product23.filter()
            category =Category.objects.filter(parent=None)
            context={
                'query':query,
                'category5':category5,
                'products3':products3,
                'category':category
            }
            return render(request,'shop.html',context)
    return HttpResponseRedirect('shop.html')
   