from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    image = models.FileField(upload_to='documents/',null=True,blank=True)
    content =models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self): # <=> __str__
        return self.title

    #class on the model order desc
    #make order data in the detail page
    class Meta:
        ordering = ['-id','-timestamp','-update']
