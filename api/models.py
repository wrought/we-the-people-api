from django.db import models

# Create your models here.

class Petition(models.Model):
	pid = models.CharField(unique=True)
	title = models.CharField(max_length=150)
	# API URL
	url = models.URLField(verify_exists=False, max_length=500)
	# Whitehouse.gov URL
        whurl = models.URLField(verify_exists=True, max_length=500)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
	issues = models.CharField(max_length=100)
	signature_count = models.IntegerField(max_length=10)
	signatures_needed = models.IntegerField(max_length=10)

# @TODO need to make these signatures actually unique w/r/t a petition on the sid key!!!
class Signature(models.Model):
	key = models.CharField(primary_key=True, max_length=64, editable=False)
        petition = models.ForeignKey(Petition, editable=False, related_name='signatures')
	sig_num = models.IntegerField(max_length=10) # @TODO to in
	sig_date = models.DateField(auto_now=False, auto_now_add=False)
	first_name = models.CharField(max_length=50)
	last_initial = models.CharField(max_length=1)
	location_city = models.Charfield(max_length=100)
	location_state = models.Charfield(max_length=100)
	url = models.CharField(max_length=500, editable=False) # api url
