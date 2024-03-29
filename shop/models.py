from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from sorl.thumbnail import ImageField


class Category(models.Model):
    title = models.CharField(max_length=255)
    details = RichTextField()
    slug = AutoSlugField(populate_from='title',unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    availability = models.BooleanField()
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=255)
    colors = models.CharField(max_length=255)
    short_intro = RichTextField()
    details = RichTextField()
    pubdate = models.DateTimeField(auto_now_add=True)
    deals_of_the_day = models.BooleanField()
    is_new = models.BooleanField()

    def __str__(self):
        return self.title

    def image(self):
        return self.producthasimage_set.first().image

    def size_list(self):
        if not self.size:
            return []
        return self.size.split(',')


class ProductHasImage(models.Model):
    image = ImageField()
    caption = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductHasReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True)
