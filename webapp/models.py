from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)

class registrationdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Pass=models.CharField(max_length=100,null=True,blank=True)
    Confirm=models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    UName=models.CharField(max_length=100,null=True,blank=True)
    PName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    TPrice=models.IntegerField(null=True,blank=True)




