from django.contrib.auth.models import User
from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=50)
    data = models.JSONField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)


class Example(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    source = models.CharField(max_length=2048)
