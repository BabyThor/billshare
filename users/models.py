from __future__ import unicode_literals

from django.db import models

class Friend(models.Model):
	bill = models.ForeignKey('bills.Bill')
	name = models.CharField(max_length=200, null=False, blank=False)
	paid = models.IntegerField(default=0)
	items = models.ManyToManyField('bills.Item')
