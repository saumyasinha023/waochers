from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
	customer_id = models.CharField(max_length=100,primary_key=True)
	customer_name = models.CharField(max_length=100)
	customer_email = models.CharField(max_length=50)
	customer_phone = models.CharField(max_length=10)
	customer_password = models.CharField(max_length=100)
	def __unicode__(self):
		return self.customer_id
	class Meta:
		db_table = 'customer_tbl'