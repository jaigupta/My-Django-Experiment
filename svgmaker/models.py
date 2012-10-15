from django.db import models

class myform(models.Model):
	data=models.CharField(max_length=20000)
	title=models.CharField(max_length=100)
	slabel=models.CharField(max_length=100)

class values(models.Model):
	lform=models.ForeignKey(myform)
	fieldId=models.CharField(max_length=10)
	label=models.CharField(max_length=100)
	value=models.CharField(max_length=100)