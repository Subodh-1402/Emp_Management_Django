from django.db import models

# Create your models here.

class emp(models.Model):
	eName = models.CharField(max_length=100)
	eID = models.IntegerField()
	eDesignation = models.CharField(max_length=100)
	eJoiningDate = models.CharField(max_length=100)
	eDepartment = models.CharField(max_length=100)
	eSalary = models.IntegerField()
	eExperience = models.IntegerField()


class News(models.Model):
    
    occation = models.TextField()

class holiday(models.Model):

	date = models.DateField()
	occation = models.TextField()