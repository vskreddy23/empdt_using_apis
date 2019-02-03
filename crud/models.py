from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Empdtls(models.Model):
	firstname=models.CharField(max_length=12)
	lastname=models.CharField(max_length=12)
	emp_id=models.AutoField(primary_key=True,max_length=9)
	mail_id=models.EmailField(max_length=23,blank=True)
	contact_no=models.IntegerField()
	gender=models.CharField(max_length=6)

def __unicode__(self):
	return self.firstname
