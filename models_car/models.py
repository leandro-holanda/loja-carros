from django.db import models

from brands.models import Brand


class ModelCar(models.Model):

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='models_car'
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand.name} - {self.name}'