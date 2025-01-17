from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    if request.method == "GET":
        return render(request, "index.html", {})


def auth(request):
    if request.method == "GET":
        return render(request, "auth.html", {})


def result(request):
    if request.method == "POST":
        data = {'name' : request.POST['fname']}
        return render(request, "resultat.html", data)