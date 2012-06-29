from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from api.resources import PetitionResource, SignatureResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeThePeopleApi.views.home', name='home'),
    # url(r'^WeThePeopleApi/', include('WeThePeopleApi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Example for API app
    # url(r'^objects/$', ListOrCreateModelView.as_view(resource=ObjectResource), name='object-root'),
    # url(r'^objects/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=ObjectResource), name='object'),

    # Petitions and Signatures API urls
    url(r'^petitions/$', ListOrCreateModelView.as_view(resource=PetitionResource), name='petition-root'),
    url(r'^petitions/(?P<pid>[^/]+)/$', InstanceModelView.as_view(resource=PetitionResource), name='petition'),
    url(r'^petitions/(?P<petition>[^/]+)/signatures/$', ListOrCreateModelView.as_view(resource=SignatureResource), name='signatures'),
    url(r'^petitions/(?P<petition>[^/]+)/signatures/(?P<sid>[^/]+)/$', InstanceModelView.as_view(resource=SignatureResource)),
)
