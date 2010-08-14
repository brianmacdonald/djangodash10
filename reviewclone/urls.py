from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'/$', 'views.dashboard', name='dashboard'),
    url(r'/(?P<username>\d+)/$', 'views.user_reviews', name='user_reviews'),
    url(r'/new/$', 'views.create_review', name='create_review'),
    url(r'/relation/$', 'views.relations_list', name='relations'),
    url(r'/relation/new/$', 'views.create_relation', name='create_relation'),
    url(r'/relation/delete/$', 'views.delete_relation', name='delete_relation'),
    url(r'/myclones/$', 'views.simular_list', name='simular_list'),
    url(r'/movies/$', 'views.items_list', name='items_list'),
    url(r'/movies/(?P<letter>\d+)/$', 'views.items_list', name='items_list_letter'),
    url(r'/after/$', 'views.after_review', name='after_review'),
)
