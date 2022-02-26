from django.db import models
from django.db import models

# Create your models here.
class fruits(models.Model):
    id1 = models.IntegerField()
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.FileField()

