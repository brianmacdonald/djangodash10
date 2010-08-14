import operator

from models import Review, Item, Relation
from django.contrib.auth.models import User

from django.conf import settings 

def find_simular(p_user):
    """
    Finds count of simular reviews for each user.

    Parameter:
        `p_user`: User object

    First finds all of the reviews of the user.Then queries all 
    users that `p_user` does not have relation with. Next it 
    loops through each review `p_unit` has and loop each user, 
    querying to find if the user has a review within the lt/gt 
    offset. If the query returns the result the user is added to     
    the `simular` dict. If the user is already in the dict it 
    adds a value of one. The return will be a dict with user 
    objects as keys and count of matching reviews as values.
    """
    p_reviews = Review.objects.filter(user=p_user)
    r_users = Relation.objects.filter(user_1=p_user).values_list('user_2__pk')
    users = User.objects.all().exclude(pk=p_user.pk).exclude(pk__in=r_users)
    simular = {}
    for p_review in p_reviews:
        for user in users:
            reviews = Review.objects.filter(
	            user=user, 
		        amount__gt=p_review.amount-settings.REVIEWCLONE_OFFSET,
		        amount__lt=p_review.amount+settings.REVIEWCLONE_OFFSET,
		        item=p_review.item,
	        )
            if reviews.count() > 0:
		        try:
		            simular[user] += 1
		        except KeyError:
		            simular[user] = 1
    return simular 

