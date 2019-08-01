from django.contrib import admin

# Register your models here.
from .models import *


class ProductHasImageInline(admin.TabularInline):
    model = ProductHasImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductHasImageInline,
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
