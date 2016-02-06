from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>post_create</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=2)
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

def post_update(request):
    return HttpResponse("<h1>post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")