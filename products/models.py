from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    sku = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    stock = models.IntegerField(default=0, verbose_name='Кол-во на складе')

    def __str__(self):
        return self.name
    def clean(self):
        if not self.name or self.name.strip() == '':
            raise ValidationError ({'name': 'Названия товара не может быть пустым'})
        if self.price <= 0:
            raise ValidationError({'price': 'Цена должна быть больше нуля'})
        if Product.objects.filter(sku=self.sku).exclude(pk=self.pk).exists():
            raise ValidationError({'sku': 'Товар с таким артикулом уже существует'})
        if self.stock < 0:
            raise ValidationError({'stock': 'Количество на складе не может быть отрицательным'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
 
        super().save(*args, **kwargs)
        
    