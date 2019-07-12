from django.contrib.auth.models import User
# Create your models here.

from django.contrib.gis.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

FOOD_CHOICES = (
    ('carbs','Carbohydrates'),
    ('meat', 'Meat'),
    ('veg','Vegetables'),
    ('dairy','Dairy'),
    ('others','Others'),
)




class Page(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=6, choices=FOOD_CHOICES, default='carbs')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProﬁle to a User model instance.
    user = models.OneToOneField(User,on_delete = models.PROTECT) # The additional attributes we wish to include.
    def __str__(self):
        return self.user.username

