from django.contrib.auth import get_user_model
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='review_products', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Продукт', to='webapp.Product', related_name='review_authors', null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Отзыв', null=False, blank=False, max_length=200)
    score = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), null=False, blank=False)

    class Meta:
        verbose_name = 'Отзыв',
        verbose_name_plural = 'Отзыв'