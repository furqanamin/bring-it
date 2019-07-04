from django.db import models

class Traveller(models.Model):
	username = models.CharField(max_length = 30)
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField()
	password = models.CharField(max_length = 30)