from urllib import quote_plus
from django import template
#this file permit to set symbol + between the words
# ex: the best world => the+best+world
#for social networking sharing usefull
#in the code we insert like this {{instance.content: urily}}

register = template.library()

@register.filter
def urlify(value):
    return quote_plus(value)