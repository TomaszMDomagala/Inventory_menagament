import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class FoodType(models.Model):
    food = models.CharField(max_length = 200)
    add_date = models.DateField('date added')
    exp_date = models.DateField('expire date', null=True, blank=True)
    opened = models.BooleanField(default = False)
    opened_date = models.DateField('opened date', null=True, blank=True)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(default = 0, max_digits = 10, decimal_places = 2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.food
    def was_published_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days = 1)
    def get_absolute_url(self):
        return reverse('foods-detail', kwargs={'pk': self.pk})
