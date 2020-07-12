from django.db import models


class BuzzwordCategory(models.Model):
    name = models.CharField(max_length=200)
	
    def __str__(self):
        return self.name


class Buzzword(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500,default='')
    category = models.ForeignKey(BuzzwordCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    

	