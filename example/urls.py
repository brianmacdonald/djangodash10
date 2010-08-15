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
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^signup/', 'views.signup', name="signup"),                      
)

urlpatterns += patterns('',
    (r'^', include('reviewclone.urls')),                      
)
 
