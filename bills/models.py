from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=200)
	amount = models.IntegerField()
	price = models.IntegerField()

class Bill(models.Model):
	name = models.CharField(max_length=200)
	status = models.BooleanField(default=False)