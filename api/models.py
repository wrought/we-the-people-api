from django.db import models

# Create your models here.

class Petition(models.Model):
	pid = models.CharField(primary_key=True, max_length=10)
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=500, editable=False) # api url
        whurl = models.CharField(max_length=500) # whitehouse.gov url
	description = models.CharField(max_length=10000)
	created_at = models.CharField(max_length=15)
	issues = models.CharField(max_length=100)
	signature_count = models.CharField(max_length=7)
	signatures_needed = models.CharField(max_length=7)

class Signature(models.Model):
        petition = models.ForeignKey(Petition, editable=False, related_name='signatures')
	sid = models.CharField(max_length=10, primary_key=True)
        name = models.CharField(max_length=100)
	url = models.CharField(max_length=500, editable=False) # api url
