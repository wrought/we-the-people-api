from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from api.resources import ObjectResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeThePeopleApi.views.home', name='home'),
    # url(r'^WeThePeopleApi/', include('WeThePeopleApi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^objects/$', ListOrCreateModelView.as_view(resource=ObjectResource), name='object-root'),
    url(r'^objects/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=ObjectResource), name='object'),
)
