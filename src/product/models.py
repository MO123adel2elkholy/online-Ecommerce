from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
# from django.core.urlresolvers import reverse
class Product(models.Model):
    proname = models.CharField(max_length=40, verbose_name=_('product name'))
    prodescription = models.TextField(verbose_name=_('product Description'))
    procost = models.DecimalField(max_digits=5, decimal_places=3, verbose_name=_('product Cost'))
    proprice = models.DecimalField(max_digits=10, decimal_places=3, verbose_name=_('product Price'))
    prodiscount = models.DecimalField(max_digits=10, decimal_places=3, verbose_name=_('product discount'))
    procreated = models.DateTimeField(verbose_name=_('product day and time of creation'))
    proBrand = models.ForeignKey('settings.Brand', verbose_name=_('product Brand'), on_delete=models.CASCADE, null=True)
    proCategory = models.ForeignKey('ProductCategory', verbose_name=_('productCategory'), on_delete=models.CASCADE, null=True)
    proVariant = models.ForeignKey('settings.Variant', verbose_name=_('product variant'), on_delete=models.CASCADE, null=True)
    proIimage = models.ImageField(upload_to='product/images', verbose_name=_('product Image'), blank=True)
    proslug = models.SlugField(null=True, blank=True, verbose_name=_('product slug'))
    proisnew= models.BooleanField(default=True, verbose_name=_('product is new!'))
    proisbest = models.BooleanField(default=False, verbose_name=_('product is best!'))

    def save(self, *args, **kwargs):
        if not self.proslug:
            self.proslug= slugify(self.proname)
        super(Product, self).save(*args, **kwargs)

    #  get your url from models than views

    def __str__(self):
        return str(self.proname)

    def get_absolute_url(self):
        return reverse('all_products', kwargs={'slug': self.proslug})

    class Meta:
        verbose_name =_("Product")
        verbose_name_plural =_("products")

# Image Model

class ProductImage(models.Model):
    proIproduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    proIimage = models.ImageField(upload_to='product/images', verbose_name=_('product Image'))

    def __str__(self):
        return str(self.proIproduct)


class ProductCategory(models.Model):
    CategoryName = models.CharField(max_length=30)
    ParentCategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, limit_choices_to={'ParentCategory__isnull':True})
    Des_Category = models.TextField()
    Category_Image = models.ImageField(upload_to='category/')
    def __str__(self):
        return str(self.CategoryName)


class ProductAlt(models.Model):
    PLAN = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product plan'), related_name='main_product')
    Alternative = models.ManyToManyField(Product, verbose_name=_('product alternative'), related_name= 'alternative_products')

    class Meta:
         verbose_name =_("Alternative")
         verbose_name_plural =_("Alternatives")

    def __str__(self):
            return str( self.PLAN)



class ProductAccessory(models.Model):
    ACCPLAN = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product Accessory'),
                                related_name='main_ACC')
    AcCCAlternative = models.ManyToManyField(Product, verbose_name=_('Alternative Accessory'),
                                             related_name='alternative_ACC')

    class Meta:

        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"

    def __str__(self):
        return str(self.ACCPLAN)


