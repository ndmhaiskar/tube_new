# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length=100)

	def __unicode__(self):
		return self.category

class VideoUpload(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	vfile = models.FileField(upload_to = 'media')
	category = models.ForeignKey(Category)
	upload_date = models.DateTimeField(auto_now_add=True)	
	
	def __unicode__(self):
		return self.title

	def __unicode__(self):
		return self.category

	def __unicode__(self):
		return self.description


import django_filters

class CatFilter(django_filters.FilterSet):

	class Meta:
		model = VideoUpload
		fields = ['title','category']
