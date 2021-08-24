from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Brand(models.Model):
    city = models.ForeignKey(City, related_name='brands', on_delete=models.CASCADE)
    employee_count = models.IntegerField()
    brand_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['employee_count']

    def __str__(self):
        return self.brand_name
