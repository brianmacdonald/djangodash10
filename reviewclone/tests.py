import random
import string
from datetime import datetime 
           
from django.contrib.auth.models import User
from django.test import TestCase

from models import Review, Item, Relation
from utils import find_simular 

class TestViews(TestCase):
    fixtures = ['item.json', 'item']

    def test_item_count(self):
        self.assertEqual(Item.objects.all().count(), 257)



