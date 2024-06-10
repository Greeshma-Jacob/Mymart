from django.db import models

# Create your models here.
class categorydb(models.Model):
    CName=models.CharField(max_length=100,null=True,blank=True)
    CDesc=models.CharField(max_length=100,null=True,blank=True)
    CImage=models.ImageField(upload_to="Category Images",null=True,blank=True)

class productdb(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    PName=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    PDesc=models.CharField(max_length=100,null=True,blank=True)
    PImage=models.ImageField(upload_to="Product Images",null=True,blank=True)


