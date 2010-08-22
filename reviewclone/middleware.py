import facebook
from django.conf import settings

from socialregistration.models import FacebookProfile

class FacebookNameMiddleware(object):
    def process_request(self, request):
        """
        Finds and saves the first name and last name initial of a 
        socialregistration Facebook user.
        """
        # Check if the user is logged in and does not have a first or last name
        if request.user.username and not (request.user.first_name  or \
            request.user.last_name):
            fb_user = facebook.get_user_from_cookie(request.COOKIES,
                settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY)
            graph = facebook.GraphAPI(fb_user['access_token']).get_object("me")
            print graph
            try:
                fb_profile = FacebookProfile.objects.get(uid=graph['id'])
                fb_profile.user.first_name = graph['first_name']
                fb_profile.user.last_name = graph['last_name'][0]
                fb_profile.user.save()
            except:
                # Something went wrong
                pass
        
        return None
