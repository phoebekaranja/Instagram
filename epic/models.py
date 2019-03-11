from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Categories(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        epic = cls.objects.filter(category__name__icontains=search_term)
        return epic

class Image(models.Model):
    name = models.CharField(max_length=20)
    statement = models.TextField(default="lol", null=True)
    location = models.ForeignKey(Location, null=True)
    category = models.ManyToManyField(Categories, default = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    Image_image = models.ImageField(upload_to = 'images/')
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def gallery_images(cls):
        epic = cls.objects.all()
        return epic
