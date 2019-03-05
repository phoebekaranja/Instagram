from django.contrib import admin
from .models import Image,Location,Categories


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Category',)

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Categorys)
