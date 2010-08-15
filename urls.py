from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import os.path

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),    
    (r'^admin(.*)', admin.site.root),    
)    

urlpatterns += patterns('',
    url(r'^$', 'registration.views.home',  name="home"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    url(r'^after_signup/$', 'django.contrib.auth.views.login', {'template_name': 'after_signup.html'}, name="after_signup"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name="logout"),
    url(r'^signup/', 'registration.views.signup', name="signup"),                      
)

urlpatterns += patterns('',
    (r'^', include('reviewclone.urls')),                      
)
 
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': "media/"}),
)
