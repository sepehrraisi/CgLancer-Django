from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    sub_categories = models.ManyToManyField("self")
    image = models.ImageField(upload_to="media/gallery/category", null=True, blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="media/gallery/products", null=True, blank=True)
