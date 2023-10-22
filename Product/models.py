from django.db import models

from django.utils.safestring import mark_safe

# Create your models here.
class Category(models.Model):
    status =(
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    keywords=models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='images/category/')
    status = models.CharField(max_length=20,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

        
    def __str__(self):
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    def get_absolute_url(self):
        return reverse('category_element',kwarg={'slug':self.slug})
class product(models.Model):
    status =(
        ('True','True'),
        ('False','False'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product23')
    title = models.CharField(max_length=200)
    keywords=models.CharField(max_length=100)
    short_description=models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,upload_to='images/Products/')
    now_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    old_price=models.DecimalField(decimal_places=2,max_digits=15,default=0)
    amount= models.IntegerField(default=0)
    min_amount= models.IntegerField(default=0)
    detail=models.TextField()
    on_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(decimal_places=2,max_digits=15,default=0,null=True,blank=True)
    new=models.BooleanField(default=False)
    feature=models.BooleanField(default=False)
    status = models.CharField(max_length=20,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created_at',)
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
    def get_absolute_url(self):
        return reverse('product_element',kwarg={'slug':self.slug})
    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
class Images(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True,upload_to='images/Products/')
    
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