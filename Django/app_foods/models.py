from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    is_premium = models.BooleanField(null=True)
    promotion_end_at = models.DateField(null=True)