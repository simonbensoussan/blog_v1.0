from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact
from .forms import ContactForm
# Create your views here.
#
# def contact_create(request):
#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=True)
#         instance.save()
#     context = {
#         'form': form,
#     }
#     return render(request)

def home(request):
    context = {}
    return render(request,'index.html',context)