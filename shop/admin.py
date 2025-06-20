from django.contrib import admin
from .models import *

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass



@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CatalogProduct)
class CatalogProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass




@admin.register(Order)
class OrderrAdmin(admin.ModelAdmin):
    pass


