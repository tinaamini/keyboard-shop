
from django.db import models
from product.models import BaseProducts

class Order(models.Model):
    product = models.ForeignKey(BaseProducts, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="جمع قیمت")
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ سفارش")
    # customer_name = models.CharField(max_length=100, verbose_name="نام مشتری")
    # customer_email = models.EmailField(verbose_name="ایمیل مشتری")

    def __str__(self):
        return f"سفارش {self.quantity} عدد از {self.product.name}"

    def save(self, *args, **kwargs):
        # کاهش موجودی محصول قبل از ذخیره سفارش
        if self.product.stock >= self.quantity:
            self.product.stock -= self.quantity
            self.product.save()
        else:
            raise ValueError('موجودی کافی نیست')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'