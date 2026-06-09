from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(_(""), max_length=50)