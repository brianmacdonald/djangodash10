from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=155)
    released = models.DateTimeField()


class Review(models.Model):
    user = models.ForeignKey(User)
    item =models.ForeignKey(Item)
    amount = models.FloatField()
    

class Relation(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1_%(app_label)s_%(class)s_related') # Follower
    user_2 = models.ForeignKey(User, related_name='user_2_%(app_label)s_%(class)s_related') # Followie
    type = models.CharField(max_length=155, default='follow')
    is_active = models.BooleanField(default=True)
 

class Simular(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1_%(app_label)s_%(class)s_related')  
    user_2 = models.ForeignKey(User, related_name='user_2_%(app_label)s_%(class)s_related') 
    count = models.IntegerField()
