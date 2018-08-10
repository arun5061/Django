from django.contrib import admin
from . models import blogModel

# Register your models here.

class blogAdminModel(admin.ModelAdmin):
    list_display=["title","updated", "added"]
    list_display_links = ["updated","title"]
    class Meta:
        model = blogModel

admin.site.register(blogModel, blogAdminModel)
