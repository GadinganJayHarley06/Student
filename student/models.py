# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Details(models.Model):
	fist_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	age = models.IntegerField()
	birthday = models.DateTimeField()
	course = models.CharField(max_length=150)
	
# Create your models here.
