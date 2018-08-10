from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blogModel(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    added = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
