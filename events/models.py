from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=150)
    event_date = models.DateTimeField()
    max_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if not self.title or self.title.strip() == '':
            raise ValidationError({'title': 'Название не может быть пустым'})
        if not self.event_date or self.event_date < timezone.now():
            raise ValidationError({'event_date': 'Дата мероприятия должна быть в будущем'})
        if not self.max_guests or self.max_guests <= 0:
            raise ValidationError({'max_guests': 'Максимальное число гостей должно быть больше нуля'})
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)