from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

class Schedules(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
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
    Date_From = models.DateField(default = '')
    Date_To = models.DateField(default = '')
    weeks = MultiSelectField(choices = WEEK_DAYS)

    def __str__(self):
        return f'user.username'