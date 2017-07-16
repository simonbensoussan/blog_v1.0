from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField()
    email= models.EmailField()
    time= models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return self.name +','+ smart_unicode(self.email)


