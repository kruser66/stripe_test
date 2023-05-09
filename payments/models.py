from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Item(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=200
    )
    description = models.TextField(
        'Описание',
        blank=True
        )
    price = models.DecimalField(
        'цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        
    def __str__(self):
        return self.name