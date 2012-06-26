from django.db import models

# Create your models here.
class Object(models.Model):
	pid = models.CharField(max_length=10)
	title = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	created_at = models.CharField(max_length=15)
	issues = models.CharField(max_length=100)
	signature_count = models.CharField(max_length=10)
	signatures_needed = models.CharField(max_length=10)
