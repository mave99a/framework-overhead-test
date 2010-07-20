# NOTE: Must import *, since Django looks for things here, e.g. handler500.
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Load the WhereBeUs application's URLs
urlpatterns = patterns('', 
                       (r'^test-1k/$', 'views.test1k'), 
                       (r'^test-10k/$', 'views.test10k'), 
                       (r'^test-1m/$', 'views.test1m'), 
                       (r'^template/test-1k/$', direct_to_template, {'template': 'test-1k.html'}),                   
                       (r'^template/test-10k/$', direct_to_template, {'template': 'test-10k.html'}),                   
                       (r'^template/test-1m/$', direct_to_template, {'template': 'test-1m.html'}),                   
                       )
