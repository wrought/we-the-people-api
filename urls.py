from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from djangorestframework.permissions import IsUserOrIsAnonReadOnly
from api.resources import AllPetitionsResource, PetitionResource, SignatureResource

from api.views import HomeView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^WeThePeopleApi/', include('WeThePeopleApi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Example for API app
    # url(r'^objects/$', ListOrCreateModelView.as_view(resource=ObjectResource), name='object-root'),
    # url(r'^objects/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=ObjectResource), name='object'),

    # Make read-only unless admin
    #class permissions.IsUserOrIsAnonReadOnly(VIEW??)
    # Petitions and Signatures API urls
    url(r'^petitions/$', ListOrCreateModelView.as_view(resource=AllPetitionsResource), name='petitions'),
    url(r'^petitions/(?P<pid>[^/]+)/$', InstanceModelView.as_view(resource=PetitionResource), name='petition'),
    url(r'^petitions/(?P<petition>[^/]+)/signatures/$', ListOrCreateModelView.as_view(resource=SignatureResource), name='signatures'),
    url(r'^petitions/(?P<petition>[^/]+)/signatures/(?P<sid>[^/]+)/$', InstanceModelView.as_view(resource=SignatureResource), name='signature'),
)
