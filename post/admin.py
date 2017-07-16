from django.contrib import admin
from .models import Post

# Register your models here.
#style interface admin
# class Meta: => link with the model (falcultatif)


class PostAdmin(admin.ModelAdmin):

        list_display = ["title","update","timestamp"]
        list_display_links = ['update']
        list_filter = ['update','timestamp']
        list_editable = ['title']
        search_fields = ['title','content']


# put the Post class into the admin interface
admin.site.register(Post,PostAdmin)

#class Meta :
        #model = Post    #name of the model to connect