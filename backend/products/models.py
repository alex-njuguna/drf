from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        value = float(self.price) * 0.8
        return f"{value:.2f}"
    
    def get_discount(self):
        return "122"