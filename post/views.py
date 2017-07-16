from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

# Create your views here.
# insert the CRUD method

#create a form
#get data from form and insert into database

def postCreate(request):
    #permission to the user to create,update or delete current post
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404 #redirect('post/index.html')
    forms = PostForm(request.POST or None, request.FILES or None)

    if forms.is_valid():
        instance = forms.save(commit=False)
        # print forms.cleaned_data.get('title')   print content field into the console
        instance.save()

    context = {
        'form': forms,
    }
    return render(request,'post/form.html', context)

def postDetail(request , id=None): # retrieve/ read / zoom
    # instance = get_object_or_404(<models_name, <element_of_table:'title','id'...>)
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': instance.title
    }
    return render(request,'post/details.html',context)

def postList(request): # list item / general
    querySet_list = Post.objects.all()

    # search bar
    q_search = request.GET.get('q_search')
    if q_search:
        querySet_list = Post.objects.filter(
            Q(title__icontains=q_search)|
            Q(content__icontains=q_search)
        ).distinct()
    #pagination
    paginator = Paginator(querySet_list, 3)  # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        querySet = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        querySet = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        querySet = paginator.page(paginator.num_pages)





    context = {
        'object_list': querySet,
        'title': 'List'
    }
    return render(request,'post/index.html',context)



def postUpdate(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)

    forms = PostForm(request.POST or None, request.FILES or None,instance=instance)

    if forms.is_valid():
        instance = forms.save(commit=False)
        # print forms.cleaned_data.get('title')   print content field into the console
        instance.save()
        return redirect('post:detail', id=instance.id)

    context = {
        'instance': instance,
        'title': instance.title,
        'form': forms,
    }
    return render(request, 'post/form.html', context)


def postDelete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('post:list')