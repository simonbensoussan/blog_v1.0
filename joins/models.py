from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Join(models.Model):

    username = models.CharField(max_length= 255)
    email = models.EmailField()
    update =models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "{0}  -> {1}".format(self.username,self.email)