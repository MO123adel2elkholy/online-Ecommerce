from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

# Brand-model


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Brand Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Brand Description'))
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Variant Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Variant Description'))
    class Meta:
         verbose_name = "Variant"
         verbose_name_plural = "Variants"

    def __str__(self):
         return self.name
