from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


class ExtendUser(models.Model):
	type_user = models.IntegerField(
		choices=TYPE_USER, verbose_name= "Тип пользователя", blank=False, default=1)
	name = models.CharField(max_length=200, verbose_name="Имя", blank=True)
	age = models.IntegerField(verbose_name = "Возраст")
	city = models.CharField(max_length=200, verbose_name="Город", blank=True, null=True)
	created_date = models.DateTimeField(
		default=timezone.now)

	def __str__(self):
		return self.name


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


class Question(models.Model):
	question_title = models.IntegerField(choices=QUESTION_TITLE,verbose_name="Название вопроса")
	question_1 = models.IntegerField(
		choices=QUESTION_1, verbose_name="1 Вопрос", blank=True)
	question_2 = models.IntegerField(
		choices=QUESTION_2, verbose_name="2 Вопрос", blank=True)
	question_3 = models.IntegerField(
		choices=QUESTION_3, verbose_name="3 Вопрос", blank=True)


class Test(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length= 200)
	published_date = models.DateTimeField(
		blank=True, null=True)
	created_date = models.DateTimeField(
		default=timezone.now)
	type_user = models.ForeignKey(
		ExtendUser, verbose_name="Тип пользователя", default=1,  blank=False, null=False)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()


