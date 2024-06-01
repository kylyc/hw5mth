from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name="Основная фотография",
        blank = True, null = True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'