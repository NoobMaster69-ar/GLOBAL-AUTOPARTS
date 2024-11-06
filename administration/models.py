from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Items(models.Model):
    description = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    price = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = models.URLField(max_length=255)

    def __str__(self):
        return self.description
    
class Parameters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.value}%"
