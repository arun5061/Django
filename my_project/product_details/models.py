from __future__ import unicode_literals

from django.db import models

# Create your models here.
class productModel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, default=0.00)
    featured = models.BooleanField(default=False)
