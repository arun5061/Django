from __future__ import unicode_literals

from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class programmers(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    language = models.ManyToManyField(language)

    def __str__(self):
        return self.name
