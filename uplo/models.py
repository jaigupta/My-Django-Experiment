from django.db import models
class counter(models.Model):
	name=models.CharField(max_length=12)
	counter=models.IntegerField()
