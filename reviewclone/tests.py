import random
import string
from datetime import datetime 
           
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from reviewclone.models import Review, Item, Relation, Simular
from reviewclone.utils import find_simular 

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
        ).save()
        self.review2 = Review(
            user=self.first_user, 
            item=self.second_item,
            amount=1
        ).save()           
        self.review3 = Review(
            user=self.first_user, 
            item=self.third_item,
            amount=3
        ).save()
        self.review4 = Review(
            user=self.second_user, 
            item=self.first_item,
            amount=4
        ).save()   
        self.review5 = Review(
            user=self.second_user, 
            item=self.second_item,
            amount=5
        ).save()  
        self.review6 = Review(
            user=self.second_user, 
            item=self.third_item,
            amount=3
        ).save()        
        self.review7 = Review(
            user=self.third_user, 
            item=self.second_item,
            amount=1
        ).save()   
        self.review8 = Review(
            user=self.third_user, 
            item=self.third_item,
            amount=1
        ).save()  

    def test_user_count(self):
        self.assertEqual(User.objects.all().count(), 3)

    def test_item_count(self):
        self.assertEqual(Item.objects.all().count(), 257)

    def test_review_count(self):
        self.assertEqual(Review.objects.all().count(), 8)


class TestSimular(TestModels):

    def test_first_user_review_count(self):
        self.assertEqual(Review.objects.filter(user=self.first_user).count(), 3)

    def test_second_user_review_count(self):
        self.assertEqual(Review.objects.filter(user=self.second_user).count(), 3)

    def test_first_user(self):
        self.assertEqual(len(find_simular(self.first_user)), 2)

    def test_create_simular(self):
        for user, count in find_simular(self.first_user).iteritems():
            Simular(
                user_1=self.first_user, 
                user_2=user, 
                count=count
            ).save()
        simular_list = Simular.objects.filter(user_1=self.first_user)
        self.assertEqual(simular_list.count(), 2)
 

class TestViews(TestModels):

    def test_create_relation(self):
       pass
 
    def test_create_relation_error(self):
       pass    

    def test_delete_relation(self):
       pass

    def test_relations_list(self):
       pass

    def test_dashboard(self):
       pass 

    def test_dashboard_access(self):
       pass
 
    def test_user_reviews(self):
       pass

    def test_user_reviews_404(self):
       pass

    def test_simular_list(self):
       pass

    def test_list_items(self):
       pass

    def test_list_items_letter(self):
       pass
 
    def test_create_review(self):
       pass
 
    def test_create_review_error(self):
       pass            

    def test_after_review(self):
       pass
 

