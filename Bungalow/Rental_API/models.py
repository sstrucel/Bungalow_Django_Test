from django.db import models

# Create your models here.
class Listing(models.Model):
    area_unit = models.CharField(max_length=100)
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2)
    bedrooms = models.IntegerField()
    home_size = models.IntegerField()
    home_type = models.CharField(max_length=100)
    last_sold_date = models.DateField()
    last_sold_price = models.IntegerField()
    link = models.TextField()
    price = models.IntegerField()
    property_size = models.IntegerField()
    rent_price = models.IntegerField()
    rentzestimate_amount = models.IntegerField()
    rentzestimate_last_updated = models.DateField()
    tax_value = models.DecimalField(max_digits=20, decimal_places=2)
    tax_year = models.IntegerField()
    year_built = models.IntegerField()
    zestimate_amount = models.IntegerField()
    zestimate_last_updated = models.DateField()
    zillow_id = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address