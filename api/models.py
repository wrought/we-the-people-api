from django.db import models

# Create your models here.

class Petition(models.Model):
	pid = models.CharField(primary_key=True, unique=True)
	title = models.CharField(max_length=150)
	# API URL
	url = models.URLField(verify_exists=False, max_length=500)
	# Whitehouse.gov URL
        whurl = models.URLField(verify_exists=True, max_length=500)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
	issues = models.TextField(max_length=200) # Comma, separated, list 
	signature_count = models.IntegerField(max_length=10)
	signatures_needed = models.IntegerField(max_length=10)

class Signature(models.Model):
        petition = models.ForeignKey(Petition, editable=False, related_name='signatures')
	sig_num = models.IntegerField(max_length=10)
	sig_date = models.DateField(auto_now=False, auto_now_add=False)
	first_name = models.CharField(max_length=50)
	last_initial = models.CharField(max_length=1)
	location_city = models.Charfield(max_length=100)
	location_state = models.Charfield(max_length=100)
	lat = models.DecimalField(max_digits=18, decimal_places=15)
	lng = models.DecimalField(max_digits=18, decimal_places=15)
	# API URL
	url = models.URLField(verify_exists=False, max_length=500)

	class Meta:
		ordering = ["sig_num"]

''' # @TODO use this to extend the Petition model to include a list of keywords
class Keyword(models.Model):
	petition = models.ForeignKey(Petition, editable=False, related_name='keyword')
	keyword = models.CharField(max_length=100)
'''
