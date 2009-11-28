from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^isis/', include('isis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    #(r'^gradebook/$', 'isis.gradebook.views.dashboard'),
    #(r'^gradebook/dashboard/$', 'isis.gradebook.views.dashboard'),
  
    (r'^accounts/', include('registration.urls')),
    
    (r'^gradebook/', include('isis.gradebook.urls')),
    #(r'^gradebook/(?P<object_id>\d+)/create$', 'django.views.generic.', class_dict),
    #(r'^gradebook/(?P<object_id>\d+)/edit$', 'django.views.generic.', class_dict),
    #(r'^gradebook/(?P<object_id>\d+)/delete$', 'django.views.generic', class_dict),
    # (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    #(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    #url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    # (r'^(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),
)
