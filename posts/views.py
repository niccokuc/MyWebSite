from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>post_create</h1>")

def post_detail(request):
    context_data = {
            "title":"Detail"
    }
    return render(request, "index.html", context_data)

def post_list(request):
    # if request.user.is_authenticated():
    #     context_data = {
    #         "title": "My User List"
    #     }
    context_data = {
        "title": "List"
    }
    return render(request, "index.html", context_data)

def post_update(request):
    return HttpResponse("<h1>post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")