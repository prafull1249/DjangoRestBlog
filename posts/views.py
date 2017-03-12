from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Post
from .forms import PostForm

def post_create(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False) # commit = false does not save the instance to the database.
        print form.cleaned_data.title
        instance.save() # saves to the database.
    # if request.method =="POST":
    #     print "title " + request.POST.get("title")
    #      print "content " + request.POST.get("content")

    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)



def post_update(request):
    context = {
        "title":"Update",
    }
    return render(request, "index.html", context)



def post_delete(request):
    context = {
        "title":"Delete",
    }
    return render(request, "index.html", context)


def post_list(request):
    query_set = Post.objects.all()
    context = {
        "object_list" : query_set,
        "title":"List",
    }

    return render(request, "index.html", context)


def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"Detail",
        "instance" : instance,
    }
    return render(request, "post_detail.html", context)
