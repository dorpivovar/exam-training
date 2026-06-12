from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.

class Orders(models.Model):
    STATUS_CHOICES = [
        ("new", "Новый"),
        ("processing", "В обработке"),
        ("shipped", "Доставлен в службу доставки"),
        ("delivered", "Доставлен"),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус заказа",
    )
    customer_name = models.CharField(max_length=200, null=False, verbose_name='Имя клиента')
    product_name = models.CharField(max_length=200, null=False, verbose_name='Название товара')
    quanity = models.PositiveIntegerField(verbose_name='Количество')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    # status = models.CharField(max_length=50, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.customer_name
    
    
    def clean(self):
        if not self.customer_name or self.customer_name == '':
            raise ValidationError({'customer_name': 'Имя клиента не может быть пустым'})
        if not self.product_name or self.product_name == '':
            raise ValidationError({'product_name': 'Название товара не может быть пустым'})
        if self.quanity <= 0:
            raise ValidationError({'quanity': 'Кол-во не может быть меньше 1'})
        # if not self.order_date or self.order_date > timezone.localdate():
        #     raise ValidationError({'order_date': 'Дата заказа не может быть позже чем сегодня'})
        if not self.status in ['new', 'processing', 'shipped', 'delivered']:
            raise ValidationError({"status": "Статус не может быть чем либо кроме 'new', 'processing', 'shipped', 'delivered'"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)