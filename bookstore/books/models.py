from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    availability = models.BooleanField(default=False)
    url = models.URLField(default="https://example.com")


    def __str__(self):
        return self.title
