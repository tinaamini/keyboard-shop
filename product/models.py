from django.db import models
import re
from django.urls import reverse
from colorfield.fields import ColorField
from colorfield.widgets import ColorWidget


# Create your models here.
def add_space_between_farsi_english(text):
    # Regular expression to find places where Persian and English characters meet
    pattern = re.compile(r'([\u0600-\u06FF])([a-zA-Z])|([a-zA-Z])([\u0600-\u06FF])')
    return pattern.sub(r'\1\3&nbsp;\2\4', text)


class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,related_name='scategory',null=True)
    is_sub=models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('productBlog:category_filter', args=[self.slug])


class BaseProducts(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    category = models.ManyToManyField(Category, related_name='products')
    img = models.ImageField(upload_to="media/", null=True)

    description = models.TextField(max_length=300, verbose_name="توضیحات", null=True, blank=True)
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت محصول", null=True, blank=True)
    deleted = models.BooleanField()
    is_activated = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def formatted_name(self):
        return add_space_between_farsi_english(self.name)



    class Meta:
        verbose_name = "محصول پایه"
        verbose_name_plural = 'محصولات پایه'


class Attributes(models.Model):
    title = models.CharField(max_length=50, verbose_name="ویژیگی")
    deleted = models.BooleanField()
    is_activated = models.BooleanField()
    type = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ویژیگی"
        verbose_name_plural = ' ویژیگیها'


class Value(models.Model):
    product = models.ForeignKey('BaseProducts', on_delete=models.SET_NULL, null=True, verbose_name='محصول')
    attribute = models.ForeignKey('Attributes', on_delete=models.SET_NULL, null=True, verbose_name='ویژگی')
    value = models.CharField(max_length=200, verbose_name='مقدار', null=True, blank=True)
    colors = ColorField(verbose_name='مقدار', null=True, blank=True)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget(attrs={'style': 'width: 100px; height: 36px;'})
        return super().formfield(**kwargs)

    class Meta:
        verbose_name = 'مقدار'
        verbose_name_plural = 'مقادیر'

    def __str__(self):
        return self.value or self.colors


class ProductImage(models.Model):
    product = models.ForeignKey(BaseProducts, related_name='images', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='product_images/', verbose_name='تصویر', null=True)

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'

    def __str__(self):
        return f"Image for {self.product.name}"
