from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from reviewclone.models import Review, Item, Relation, Similar
from reviewclone.utils import find_similar 

class TestModels(TestCase):
    fixtures = ['item.json', 'item']

    def setUp(self):

        self.generic_password = "12345"

        # Create users
        User.objects.create_user("foo", 
                                 "foo@example.com", 
                                 self.generic_password,
                                ).save()
        User.objects.create_user("foo2",
                                 "foo2@example.com",
                                 self.generic_password,
                                ).save()
        User.objects.create_user("foo3", 
                                 "foo3@example.com", 
                                 self.generic_password,
                                ).save()

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

        self.not_logged_in_client = Client()
        
        self.logged_in_client = Client()
        self.logged_in_client.login(
            username=self.first_user.username, 
            password=self.generic_password
        )

        # Creation relation
        Relation(
            user_1=self.first_user,
            user_2=self.second_user,
        ).save()

    def test_user_count(self):
        self.assertEqual(User.objects.all().count(), 3)

    def test_item_count(self):
        self.assertEqual(Item.objects.all().count(), 257)

    def test_review_count(self):
        self.assertEqual(Review.objects.all().count(), 8)


class TestSimilar(TestModels):

    def test_first_user_review_count(self):
        self.assertEqual(Review.objects.filter(user=self.first_user).count(), 3)

    def test_second_user_review_count(self):
        self.assertEqual(Review.objects.filter(user=self.second_user).count(), 3)

    def test_first_user(self):
        self.assertEqual(len(find_similar(self.first_user)), 1)

    def test_create_similar(self):
        for user, count in find_similar(self.first_user).iteritems():
            Similar(
                user_1=self.first_user, 
                user_2=user, 
                count=count
            ).save()
        similar_list = Similar.objects.filter(user_1=self.first_user)
        self.assertEqual(similar_list.count(), 1)
 

class TestViews(TestModels):

    def test_create_relation(self):
        response = self.logged_in_client.get(reverse('create_relation'))
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/create_relation.html')
        form = response.context['form'] 
        self.failUnlessEqual(len(form.fields), 1)

    def test_create_relation_post(self):
        relation = Relation.objects.filter(
            user_1=self.first_user,
            user_2=self.third_user,
        )
        self.failUnlessEqual(relation.count(), 0)
        response = self.logged_in_client.post(reverse('create_relation'),
            {
                'user_2': 3,
            }
        )
        self.failUnlessEqual(response.status_code, 302)
        self.failUnlessEqual(relation.count(), 1)

    def test_create_relation_post_error(self):
        relation = Relation.objects.filter(
            user_1=self.first_user,
            user_2=self.second_user,
        )
        self.failUnlessEqual(relation.count(), 1)        
        response = self.logged_in_client.post(reverse('create_relation'),
            {
                'user_2': 2,
            }
        )
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/create_relation.html')
        has_relation = response.context['has_relation'] 
        self.failUnlessEqual(has_relation, True)

    def test_delete_relation(self):
        response = self.logged_in_client.get(reverse('delete_relation'))
        self.failUnlessEqual(response.status_code, 200)
        user_2 = response.context['user_2']
        self.failUnlessEqual(user_2, None)
        form = response.context['form'] 
        self.failUnlessEqual(len(form.fields), 1)           

    def test_delete_relation_post(self):
        relation = Relation.objects.filter(
            user_1=self.first_user,
            user_2=self.second_user,
        )
        self.failUnlessEqual(relation.count(), 1)
        response = self.logged_in_client.post(reverse('delete_relation'),
            {
                'user_2': 2,
            }
        )
        self.failUnlessEqual(response.status_code, 302)
        self.failUnlessEqual(relation.count(), 0) 
        
    def test_relations_list(self):
        response = self.logged_in_client.get(reverse('relations'))
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/relations_list.html')
        object_list = response.context['object_list']
        self.failUnlessEqual(object_list.count(), 1)

    def test_dashboard(self):
        response = self.logged_in_client.get(reverse('dashboard'))
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name,
                             'reviewclone/dashboard.html')
        object_list = response.context['object_list']
        self.failUnlessEqual(object_list.count(), 6) 

    def test_dashboard_no_access(self):
        response = self.not_logged_in_client.get(reverse('dashboard'))
        self.failUnlessEqual(response.status_code, 302)

    def test_user_reviews(self):
        response = self.logged_in_client.get(
            reverse('user_reviews', 
                args=[self.second_user.username],
            )
        )
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/user_reviews.html')
        object_list = response.context['object_list']
        self.failUnlessEqual(object_list[0].user, self.second_user) 
        self.failUnlessEqual(object_list.count(), 3) 

    def test_user_reviews_404(self):
        response = self.logged_in_client.get(
            reverse('user_reviews', 
                args=['not_a_real_user'],
            )
        )
        self.failUnlessEqual(response.status_code, 404) 

    def test_similar_list(self):
        response = self.logged_in_client.get(reverse('similar_list'))
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name,
                             'reviewclone/similar_list.html')
        # Test similar list count       
        similar_list = response.context['object_list']
        self.failUnlessEqual(similar_list.count(), 1) 
        similar_query_list = Similar.objects.filter(user_1=self.first_user) 
        self.failUnlessEqual(similar_list.count(), 1) 

    def test_items_list(self):
        response = self.logged_in_client.get(reverse('items_list'))
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/items_list.html')
        items = response.context['object_list']
        self.failUnlessEqual(items.count(), 257) 

    def test_items_list_letter(self):
        response = self.logged_in_client.get(
            reverse('items_list_letter',
                args=['S'],       
            ),        
        )
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name,
                             'reviewclone/items_list.html')
        items = response.context['object_list']
        self.failUnlessEqual(items[1].name, u'Star Wars: Episode V - The Empire Strikes Back') 

    def test_create_review(self):
        response = self.logged_in_client.get(
            reverse('create_review', 
                args=[2],
            )
        )
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name, 
                             'reviewclone/create_review.html')
        form = response.context['form'] 
        self.failUnlessEqual(len(form.fields), 1)
        item = response.context['item'] 
        self.failUnlessEqual(item.name, u'The Shawshank Redemption')

    def test_create_review_post(self):
        response = self.logged_in_client.post(
            reverse('create_review', 
                args=[10],
            ),
            {
                'amount': 5,
            } 
        )
        self.failUnlessEqual(response.status_code, 302) 

    def test_create_review_error(self):
        response = self.logged_in_client.get(
            reverse('create_review',
                args=[2],
            )
        )
        self.failUnlessEqual(response.status_code, 200) 
        self.failUnlessEqual(response.template[0].name,
                             'reviewclone/create_review.html')

    def test_after_review(self):
        response = self.logged_in_client.get(reverse('after_review', args=[1]))
        self.failUnlessEqual(response.status_code, 200)  
        self.failUnlessEqual(response.template[0].name,
                             'reviewclone/after_review.html')

