from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>post_create</h1>")

def post_detail(request):
    return HttpResponse("<h1>post_detail</h1>")

def post_list(request):
    return render(request, "index.html", {})

def post_update(request):
    return HttpResponse("<h1>post_update</h1>")

def post_delete(request):
    return HttpResponse("<h1>post_delete</h1>")