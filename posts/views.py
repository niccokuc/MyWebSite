from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    """
    THIS IS THE MAIN FORM ENTRY METHOD
    """
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_date.get("title"))
        instance.save()
        messages.success(request, "Function was successful.")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Function was unsuccessful.")
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context_data = {
            "instance_list": instance,
            "title":instance.title,
    }
    return render(request, "post_detail.html", context_data)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    # if request.user.is_authenticated():
    #     context_data = {
    #         "title": "My User List"
    #     }
    # context_data = {
    #     "title": "List"
    # }
    return render(request, "index.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    # put in the values of the instance it fetched.
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Update was successful.", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    #else:
    #     messages.error(request, "Update was unsuccessful.")

    context = {
            "instance": instance,
            "title":instance.title,
            "form": form,
    }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")