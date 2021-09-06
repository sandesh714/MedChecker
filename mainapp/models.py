from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Schedules(models.Model):
    WEEK_DAYS = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        
    )

    medicine_name = models.CharField(max_length=100)
    Date_From = models.DateField()
    Date_To = models.DateField()
    weeks = MultiSelectField(choices = WEEK_DAYS)

