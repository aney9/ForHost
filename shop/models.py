from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 255
MAX_LENGTH_1 = 25

class Brand(models.Model):
    BrandName = models.CharField(max_length=MAX_LENGTH_1, verbose_name='Название бренда')
    Img = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='изображение бренда')

    def __str__(self):
        return self.BrandName

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class PetType(models.Model):
    TypeName = models.CharField(max_length=25, verbose_name='Тип животного', unique=True)
    Description = models.TextField(max_length=500, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.TypeName

    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'


class CategoryProduct(models.Model):
    CategoryName = models.CharField(max_length=MAX_LENGTH_1, verbose_name='Название категории товара')
    PetType = models.ForeignKey(PetType, on_delete=models.CASCADE, verbose_name='Тип животного', null=True, blank=True)

    def __str__(self):
        return self.CategoryName

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class CatalogProduct(models.Model):
    ProductName = models.CharField(max_length=100, verbose_name='Название продукта')
    PriceOfProduct = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    DescriptionProduct = models.CharField(max_length=300, verbose_name='Описание продукта')
    Img = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение продукта')
    Quantity = models.PositiveIntegerField(verbose_name='Количество')
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    Category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.ProductName

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Promotion(models.Model):
    PromotionName = models.CharField(max_length=100, verbose_name='Название акции')
    DiscountPercentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент скидки')
    StartDate = models.DateTimeField(verbose_name='Дата начала')
    EndDate = models.DateTimeField(verbose_name='Дата окончания')
    CatalogProduct = models.ManyToManyField(CatalogProduct, verbose_name='Продукты', blank=True)

    def __str__(self):
        return self.PromotionName

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'



class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY=[
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]
    buyer_surname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_middlename = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True,verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    catalogproduct = models.ManyToManyField('CatalogProduct', through='Pos_order', verbose_name='Товар')


    def __str__(self):
        return f"#{self.pk} - {self.buyer_surname} {self.buyer_name} {self.date_create}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    catalogproduct = models.ForeignKey(CatalogProduct, on_delete=models.PROTECT, verbose_name='продукт')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количство продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'{self.order.pk} {self.catalogproduct.name} ({self.order.buyer_surname} {self.order.buyer_name}'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'