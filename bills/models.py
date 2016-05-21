from __future__ import unicode_literals

from django.db import models

class Bill(models.Model):
	name = models.CharField(max_length=200)
	status = models.BooleanField(default=False)

class Item(models.Model):
	bill = models.ForeignKey('bills.Bill')
	name = models.CharField(max_length=200)
	amount = models.IntegerField()
	price = models.IntegerField()