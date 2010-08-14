from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import os.path

urlpatterns = patterns('',
    (r'^', include('reviewclone.urls')),                      
)

urlpatterns += patterns('',
    (r'^admin/(.*)', admin.site.root),    
    (r'^admin(.*)', admin.site.root),    
)     
