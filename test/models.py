from django.db import models

# Create your models here.
class Calc(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	rate = models.FloatField()
	count = models.IntegerField()