from django.db import models


CATEGORY = (
    ('vegetables', 'vegetables'),
    ('fruits', 'fruits'),
    ('juice', 'juice'),
    ('dried', 'dried')
)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    regular_price = models.FloatField(blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=120, null=True)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name





