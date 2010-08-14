from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'new/(?P<item_id>[\d]+)/$', 'reviewclone.views.create_review', name='create_review'),
    url(r'relation/$', 'reviewclone.views.relations_list', name='relations'),
    url(r'relation/new/$', 'reviewclone.views.create_relation', name='create_relation'),
    url(r'relation/delete/$', 'reviewclone.views.delete_relation', name='delete_relation'),
    url(r'myclones/$', 'reviewclone.views.simular_list', name='simular_list'),
    url(r'movies/$', 'reviewclone.views.items_list', name='items_list'),
    url(r'movies/(?P<letter>\w+)/$', 'reviewclone.views.items_list', name='items_list_letter'),
    url(r'after/(?P<review_id>\d+)/$', 'reviewclone.views.after_review', name='after_review'),
    url(r'user/(?P<username_slug>[-\w]+)/$', 'reviewclone.views.user_reviews', name='user_reviews'),
    url(r'dashboard/$', 'reviewclone.views.dashboard', name='dashboard'),

)
