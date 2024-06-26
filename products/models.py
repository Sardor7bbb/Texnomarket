from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategoriesModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Categoriy'
        verbose_name_plural = 'Products Categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Products Tags'


class ProductColorModel(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Color'
        verbose_name_plural = 'Products Colors'


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Size'
        verbose_name_plural = 'Products Sizes'


class ProductManufactureModel(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True, upload_to='manufacture/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Manufacture'
        verbose_name_plural = 'Products Manufactures'


class ProductModel(models.Model):
    image = models.ImageField(upload_to='products/')

    name = models.CharField(max_length=255, db_index=True)
    long_description = models.TextField()
    short_description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    sku = models.CharField(max_length=10, unique=True)
    count = models.PositiveIntegerField()

    manufacture = models.ForeignKey(ProductManufactureModel, on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    categories = models.ManyToManyField(ProductCategoriesModel, related_name='products')
    sizes = models.ManyToManyField(ProductSizeModel, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.count != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    def get_related_products(self):
        return ProductModel.objects.filter(categories=self.categories).exclude(pk=self.pk)[:3]

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImagesModel(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
