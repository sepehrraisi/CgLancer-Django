from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    sub_categories = models.ManyToManyField("self")

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
