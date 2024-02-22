from django.db import models
from django.db import models
from django.utils.text import slugify

# Create your models here.




class Product(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    mrp=models.IntegerField()
    img=models.ImageField(upload_to='media')
    img1=models.ImageField(upload_to='media')
    img2=models.ImageField(upload_to='media')
    img3=models.ImageField(upload_to='media')
    img4=models.ImageField(upload_to='media')
    img5=models.ImageField(upload_to='media')
    img6=models.ImageField(upload_to='media')
    description=models.TextField()
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
         return self.name
    


class Contact(models.Model):
    firstname= models.CharField(max_length=50)
    lastname=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=60)
    message=models.TextField()
    def __str__(self):
     return self.firstname



class TopRanking(models.Model):
    image=models.ImageField(upload_to='media')
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    mrp=models.IntegerField()

    def __str__(self):
        return self.title
    


class Checkout(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=19)
    company=models.CharField(max_length=20)
    country=models.CharField(max_length=12)
    address=models.TextField()
    pincode=models.IntegerField()
    phone=models.IntegerField()
    email=models.CharField(max_length=20)
    # date=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.first_name


# class OrderItems(models.Model):
#     order=models.ForeignKey(Checkout,on_delete=models.CASCADE)
#     Product=models.CharField(max_length=52)
#     image=models.ImageField(upload_to='media/order_image')
#     quantity=models.IntegerField()
#     price=models.FloatField()
#     total=models.FloatField()
#     paid=models.BooleanField(default=False)
