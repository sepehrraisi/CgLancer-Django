from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40)
    sub_categories = models.ManyToManyField("self", blank=True)
    image = models.ImageField(upload_to="gallery/category", default="/Default.png")

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=40)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="gallery/products", blank=True)
