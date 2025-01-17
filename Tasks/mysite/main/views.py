from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html",)
    if request.method == "POST":
        return redirect(auth, request.POST)



def auth(request):
    if request.method == "GET":
        return render(request, "auth.html",)
    if request.method == "POST":
        print(request.POST)
        return render(request, "auth.html", request.POST)

