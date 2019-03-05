from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    # location = models.ForeignKey(Location)
    # category = models.ManyToManyField(Categorys, default = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    # Image_image = models.ImageField(upload_to = 'images/')
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
