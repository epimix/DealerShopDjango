from django.db import models

class Car(models.Model):
    TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='carphotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class BuyingRequest(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='buying_requests')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Buying Request for {self.car} by {self.customer_name}"
