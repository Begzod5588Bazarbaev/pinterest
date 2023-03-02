from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	name = models.CharField(max_length=20, verbose_name='Имя')
	image = models.ImageField(verbose_name='Фотографие')
	body = models.TextField(max_length=100, verbose_name='О себе')

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name='Название')
	image = models.ImageField(verbose_name='Изображение')

	def __str__(self):
		return self.name


class Posts(models.Model):
	title = models.CharField(max_length=20, verbose_name='Название')
	image = models.ImageField(verbose_name='Изображение')
	detail = models.TextField(max_length=150, verbose_name='Информация')
	date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return self.title