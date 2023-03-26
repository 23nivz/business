from django.db import models

class companies(models.Model):
  newid = models.IntegerField()
  name = models.CharField(max_length=255,blank= True,null=True)   
  category = models.CharField(max_length=225 ,null =True,blank=True)
  address_1=models.CharField(max_length=225 ,null =True,blank=True)
  address_2=models.CharField(max_length=225 ,null =True,blank=True)
  city =models.CharField(max_length=225 ,null =True,blank=True)
  state =models.CharField(max_length=225 ,null =True,blank=True)
  zipcode=models.IntegerField()
  phone = models.CharField(max_length=225,null =True,blank=True)
  website = models.CharField(max_length=225 ,null =True,blank=True)
  email = models.CharField(max_length=255,null =True,blank=True)