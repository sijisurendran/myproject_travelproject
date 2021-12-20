from django.db import models

# Create your models here.
class place(models.Model):
   name= models.CharField(max_length=100)
   img=models.ImageField(upload_to='picture')
   desc=models.TextField()
   price=models.IntegerField()
   offer=models.BooleanField(default=False)

class details(models.Model):
   day=models.IntegerField()
   month=models.CharField(max_length=100)
   img=models.ImageField(upload_to='pics')
   desc=models.TextField()
   desc1=models.TextField()

