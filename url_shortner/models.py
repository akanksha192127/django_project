from django.db import models

# Create your models here.
class URLMapping(models.Model):
	id = models.AutoField(primary_key=True)
	original_link = models.CharField(max_length=2000, null=False)
	short_link = models.CharField(max_length=1000, null=False)
	count = models.IntegerField(null=False, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)