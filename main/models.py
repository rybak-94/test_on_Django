from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	published_date = models.DateTimeField(
		blank=True, null=True)
	created_date = models.DateTimeField(
		default=timezone.now)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()


class Test(models.Model):
	author = models.ForeignKey('auth.User', null=True)
	title = models.CharField(max_length=200)
	published_date = models.DateTimeField(
		blank=True, null=True)
	type_user=models.CharField(max_length=200, null=True)
	created_date = models.DateTimeField(
		default=timezone.now)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()


