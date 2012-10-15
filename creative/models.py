from django.db import models

# Create your models here.
class stores(models.Model):
	secret=models.CharField(max_length=10)
	value=models.CharField(max_length=100000)
	age=models.IntegerField()
	name=models.CharField(max_length=50)
	emailid=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	passx=models.CharField(max_length=50)