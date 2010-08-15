from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
 
class TestViews(TestCase):

    def test_signup(self):
        not_logged_in_client = Client()
        response = not_logged_in_client.get(reverse('signup'))
        self.failUnlessEqual(response.status_code, 200)

    def test_signup_post(self):
        not_logged_in_client = Client()
        response = not_logged_in_client.post(reverse('signup'),
            {
                'username': 'foo',
                'password': 'bar',
                'first_name': 'eggs',
                'last_name': 'foobar',
                'email': 'spam@exmaple.com',
            }
        )
        self.failUnlessEqual(response.status_code, 302)
        users = User.objects.all()
        self.failUnlessEqual(users.count(), 1)
 

