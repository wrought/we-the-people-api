from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from api.models import Petition, Signature

class AllPetitionsResource(ModelResource):
	model = Petition
	fields = ('pid', 'title', 'url')
	def signatures(self, instance):
		return reverse('signatures', kwargs={'petition': instance.pid})

class PetitionResource(ModelResource):
	model = Petition
	fields = ('pid', 'title', 'url', 'whurl', 'description', 'created_at', 'issues', 'signature_count', 'signatures_needed')
        # Method used to tie signatures to petitions
	def signatures(self, instance):
		return reverse('signatures', kwargs={'petition': instance.pid})

class SignatureResource(ModelResource):
        model = Signature
        fields = ('sig_num', 'sig_date' 'petition', 'first_name', 'first_initial', 'location_city', 'location_state', 'lat', 'lng', 'url')
	# Method used to tie signatures to petitions
	def petition(self, instance):
		return reverse('petition', kwargs={'pid': instance.petition.pid})
