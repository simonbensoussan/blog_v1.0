from django.shortcuts import render
from .form import JoinForm
# Create your views here.

def home(request):
    form = JoinForm()
    context = {"form": form}
    template = "index.html"
    return render(request,template,context)