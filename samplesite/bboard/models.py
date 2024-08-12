from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.FloatField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)
# Create your models here.
# 1 manage.py makemigrations bboard - создание миграции
# manage.py sqlmigrate bboard 0001 - просмотр в консоли
