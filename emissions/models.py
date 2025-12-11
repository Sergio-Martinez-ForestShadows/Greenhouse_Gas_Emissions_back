from django.db import models


class Emission(models.Model):
    year = models.IntegerField()
    emissions = models.DecimalField(max_digits=10, decimal_places=2)
    emission_type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Emission"
        verbose_name_plural = "Emissions"
        ordering = ["year", "country", "emission_type"]

    def __str__(self):
        return f"{self.year} - {self.country} - {self.emission_type}"
