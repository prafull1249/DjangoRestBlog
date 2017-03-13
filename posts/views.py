from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

from .models import Post
from .forms import PostForm

def post_create(request):

    form = PostForm(request.POST or None)
    print form
    if form.is_valid():
        instance = form.save(commit=False) # commit = false does not save the instance to the database.
        # print form.cleaned_data.title
        instance.save() # saves to the database.
        messages.success(request, "Successfully created ! ")
        return redirect("posts:list")
    else:
        messages.error(request, "Not Successfully created ! ")
    context = {
        "title":"Create",
        "form":form,
    }
    return render(request, "post_form.html", context)




def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    # provide instance to PostForm which is a subclass of models.modelForm so that it already loads the instance without creating a new one.
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False) # commit = false does not save the instance to the database.
        instance.save() # saves to the database.
        # message success
        messages.success(request, "Successfully saved ! ")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #    messages.error(request, "Save failed ! ")
    context = {
        "title":"Update",
        "instance" : instance,
        "form" : form,
    }
    return render(request, "post_form.html", context)



def post_delete(request, id=None):

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect( "posts:list")


def post_list(request):
    query_set = Post.objects.all()
    context = {
        "object_list" : query_set,
        "title":"List",
    }

    return render(request, "posts_list.html", context)


def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"Detail",
        "instance" : instance,
    }
    return render(request, "post_detail.html", context)
