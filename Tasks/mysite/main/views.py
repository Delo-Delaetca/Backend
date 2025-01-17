from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import User


def index(request):
    context = {'Users': User.objects.all()}
    return render(request, "index.html", context)


def create(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        new_user = User()
        new_user.login = request.POST['login']
        new_user.name = request.POST['name']
        new_user.password = request.POST['pass']
        new_user.save()
        
        return redirect(index)
            
 #pk = primary key
def read(request, id):
    if request.method == "GET":
        return render(request, "read.html", {'User':User.objects.get(pk=id)})

def update(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.login = request.POST['login']
        user.name = request.POST['name']
        user.password = request.POST['pass']
        user.save()
        
        return redirect(read, id )

def delete(request, id):
    User.objects.get(pk=id).delete()
    return redirect(index)