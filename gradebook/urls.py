from django.conf.urls.defaults import *
from isis.gradebook.models import *
from django.contrib import admin
from isis.gradebook.forms import *

# Using generic views
class_dict = {
  'queryset': Class.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^isis/', include('isis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^$', 'isis.gradebook.views.dashboard'),
    (r'^dashboard/$', 'isis.gradebook.views.dashboard'),
    (r'^class/(?P<class_id>\d+)/$', 'isis.gradebook.views.gradebook'),
    (r'^class/(?P<object_id>\d+)/edit/$', 'django.views.generic.create_update.update_object', {'model': Class, 'form_class': TeacherClassEditForm, 'post_save_redirect': "/gradebook/"} ),
    (r'^class/add/$', 'isis.gradebook.views.class_add'),
    #(r'^class/add/$', 'django.views.generic.create_update.create_object', {'form_class': TeacherClassEditForm),
    (r'^class/(?P<object_id>\d+)/delete/$', 'django.views.generic.create_update.delete_object', {'model': Class, 'post_delete_redirect': "/gradebook/"}),
    (r'^class/(?P<class_id>\d+)/student/add/$',
    'isis.gradebook.views.class_add_student'),
    (r'^students/$',
    'django.views.generic.list_detail.object_list', { 'queryset': Student.objects.all()}),
    #(r'^gradebook/class/add/$', 'isis.gradebook.views.class_add'),
)
