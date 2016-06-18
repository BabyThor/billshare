from __future__ import unicode_literals

from django.db import models

class Bill(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)
	status = models.BooleanField(default=False)
	date = models.DateTimeField()
	slug = models.CharField(max_length=100, null=False, blank=False)

	def __unicode__(self):
		return self.name

class Item(models.Model):
	bill = models.ForeignKey('bills.Bill')
	name = models.CharField(max_length=200, null=False, blank=False)
	amount = models.IntegerField(default=0)
	price = models.IntegerField(default=0)
	price_per_person = models.IntegerField(default=0)

	def __unicode__(self):
		return '%s (%s)' % (self.name, self.bill.name)