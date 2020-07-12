from django.db import models


class Result(models.Model):
    search = models.CharField(max_length=200,default='')
    result = models.CharField(max_length=500,default='')
    found = models.BooleanField(default=True)


    def __str__(self):
        return self.search


