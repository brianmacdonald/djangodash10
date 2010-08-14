import random
import string
from datetime import datetime 
           
from django.contrib.auth.models import User
from django.test import TestCase

from models import Review, Item, Relation
from utils import find_simular 

class TestModels(TestCase):
    fixtures = ['item.json', 'item']

    def setUp(self):
        # Create users
        User.objects.create_user("foo", "foo@example.com", "12345", ).save()
        User.objects.create_user("foo2", "foo2@example.com", "12345", ).save()
        User.objects.create_user("foo3", "foo3@example.com", "12345", ).save()

        # Find Users
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)
        self.third_user = User.objects.get(pk=3)

        # Find a few Items
        self.first_item = Item.objects.get(pk=2)
        self.second_item = Item.objects.get(pk=3)
        self.third_item = Item.objects.get(pk=4)

        # Create reviews
        self.review1 = Review(
            user=self.first_user, 
            item=self.first_item,
            amount=5
        )
        self.review2 = Review(
            user=self.first_user, 
            item=self.second_item,
            amount=1
        )            
        self.review3 = Review(
            user=self.first_user, 
            item=self.third_item,
            amount=3
        ) 
        self.review4 = Review(
            user=self.second_user, 
            item=self.first_item,
            amount=4
        )    
        self.review4 = Review(
            user=self.second_user, 
            item=self.second_item,
            amount=5
        )   
        self.review5 = Review(
            user=self.third_user, 
            item=self.second_item,
            amount=4
        )    
        self.review6 = Review(
            user=self.third_user, 
            item=self.third_item,
            amount=1
        )  

    def test_user_count(self):
        self.assertEqual(User.objects.all().count(), 3)

    def test_item_count(self):
        self.assertEqual(Item.objects.all().count(), 257)

    def test_review_count(self):
        pass


class TestSimular(TestModels):

    def test_first_user(self):
        pass

