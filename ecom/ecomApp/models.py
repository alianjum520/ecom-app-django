from django.db import models
from django.forms import ModelForm,TextInput,EmailInput
from django.utils.safestring import mark_safe

# Create your models here.
class settings(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax=models.CharField(blank=True, max_length=50)
    email=models.EmailField(null=True,blank=True,max_length=50)
    smptserver = models.CharField(max_length=100)
    smptemail=models.EmailField(null=True,blank=True,max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True,null=True,upload_to='images/icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    refrence = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    @property
    def logoURL(self):
        try:
            url = self.icon.url
        except:
            url = ''
        return url
    def image_tag(self):
        return mark_safe('<img src="{}" width="60" height="70" />'.format(self.icon.url))
    image_tag.short_description ="Image"

class carousel(models.Model):
    title = models.CharField(max_length=200)
    keywords=models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=100,blank=True,null=True)
    sale_amount = models.IntegerField(blank=True,null=True)
    image = models.ImageField(blank=True,upload_to='images/carousel/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def image_tag(self):
        return mark_safe('<img src="{}" width="60" height="70" />'.format(self.image.url))
    image_tag.short_description ="Image"
class Banner(models.Model):
    title = models.CharField(max_length=100)
    image1 = models.ImageField(blank=True,upload_to='images/banner/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    def image_tag(self):
        return mark_safe('<img src="{}" width="60" height="70" />'.format(self.image1.url))
    image_tag.short_description ="Image"
class About_Name(models.Model):
    image = models.ImageField(blank=True,null=True)
    title = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" width="60" height="70" />'.format(self.image.url))
    image_tag.short_description ="Image"
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class About_Us(models.Model):
    name=models.OneToOneField(About_Name, on_delete=models.CASCADE)
    description2=models.CharField(max_length=200)
class Contact(models.Model):
    STATUS=(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True) 
    subject=models.CharField(max_length=400,null=True,blank=True)
    messages=models.TextField(max_length=1000,blank=True,null=True)
    status=models.CharField(max_length=40,choices=STATUS,default='New')
    ip=models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields =['name','email','subject','messages']
        widgets ={
            'name':TextInput(attrs={'class':'input','placeholder':'Full Name'}),
            'email':EmailInput(attrs={'class':'input','placeholder':'example@something.com'}),
            'subject':TextInput(attrs={'class':'input','placeholder':'Write Your Subject'}),
            'messages':TextInput(attrs={'class':'input','placeholder':'Write Your Message'})
        }