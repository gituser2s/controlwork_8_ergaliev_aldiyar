from django.db import models
from django.db.models import Avg


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название")
    category = models.CharField(max_length=10, verbose_name='Категория', choices=(('Еда', 'Еда'), ('Машина', 'Машина'), ('Гаджеты', 'Гаджеты')), null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True, max_length=200)
    image = models.ImageField(verbose_name="Картинка", upload_to='webapp', null=True, blank=True)
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )

    def __str__(self):
        return f"{self.title}"
