from django.db import models

# Create your models here.
class Destiny(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='templates')
    description = models.TextField(100)
    price = models.IntegerField(5)
    offer = models.BooleanField(default=False)
