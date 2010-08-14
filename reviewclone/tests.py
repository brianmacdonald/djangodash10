import random
import string
from datetime import datetime 
           
from django.contrib.auth.models import User
from django.test import TestCase

from models import Unit, Item, Relation
from utils import find_simular 

class TestViews(TestCase):

    def test_relation(self):
        pass



