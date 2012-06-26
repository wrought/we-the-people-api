from djangorestframework.resources import ModelResource
from api.models import Object

class ObjectResource(ModelResource):
	model = Object
	fields = ('pid', 'title', 'url', 'description', 'created_at', 'issues', 'signature_count', 'signatures_needed')
