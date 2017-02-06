from django.db import models
from django.utils import timezone

TYPE_USER = {
	(1, 'Admin'),
	(2, 'User')
}
QUESTION_1 = {
	(1, 'Я смелый человек'),
	(2, 'Я счастливый человек'),
	(3, 'Я несчастен'),
}
QUESTION_2 = {
	(1, 'Я успешный человек'),
	(2, 'Я счастливый человек'),
	(3, 'Я несчастен'),
}
QUESTION_3 = {
	(1, 'Я хорошо вижу'),
	(2, 'Я счастливый человек'),
	(3, 'Я не вижу'),
}
QUESTION_TITLE = {
	(1, 'Тест на смелось'),
	(2, 'Тест на успешность'),
	(3, 'Тест на зоркость'),
}


class User(models.Model):
	type_user = models.IntegerField(
		choices=TYPE_USER)
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	city = models.CharField(max_length=200)


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
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length= 200)
	published_date = models.DateTimeField(
		blank=True, null=True)
	created_date = models.DateTimeField(
		default=timezone.now)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()