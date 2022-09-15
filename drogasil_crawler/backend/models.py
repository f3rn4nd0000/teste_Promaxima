from django.db import models

# Create your models here.
class Productdata(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.FloatField()

    """ ESSAS SAO OPCIONAIS, SE EU FIZER O BASICO FAÇO ISSO TBM"""
    product_code = models.IntegerField()
    ean_code = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    avg_grade = models.DecimalField(max_digits=3, decimal_places=1)
