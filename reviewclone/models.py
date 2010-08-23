from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

REVIEW_CHOICES = (
    (0.5, '0.5 Star'),
    (1, '1 Star'),
    (1.5, '1.5 Stars'),
    (2, '2 Stars'),
    (2.5, '2.5 Stars'),
    (3, '3 Stars'),
    (3.5, '3.5 Stars'),
    (4, '4 Stars'),
    (4.5, '4.5 Stars'),
    (5, '5 Stars'),
)


class Item(models.Model):
    name = models.CharField(max_length=155)
    released = models.DateTimeField()

    def __unicode__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    amount = models.FloatField("Rating", choices=REVIEW_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s review by %s %s." % (self.item.name, self.user.first_name,
                                        self.user.last_name)


class Relation(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1_%(app_label)s_%(class)s_related') # Follower
    user_2 = models.ForeignKey(User, related_name='user_2_%(app_label)s_%(class)s_related') # Followie
    type = models.CharField(max_length=155, default='follow')
    is_active = models.BooleanField(default=True)
 

class Similar(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1_%(app_label)s_%(class)s_related')  
    user_2 = models.ForeignKey(User, related_name='user_2_%(app_label)s_%(class)s_related') 
    count = models.IntegerField()
