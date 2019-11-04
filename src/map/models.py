from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class News(models.Model):
    CRIME_CATEGORY = (
        
    )
    title = models.CharField(max_length=60)
    category = models.CharField(max_length=55,choices=CRIME_CATEGORY)
    severity = models.IntegerField(default=1,validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    state = models.CharField(max_length=35)
    city = models.CharField(max_length=40)
