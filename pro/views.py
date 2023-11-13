from django.shortcuts import render, redirect
from .models import Member


# Create your views here.

def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem': mem})


def add(request):
    return render(request, 'add.html')


def addreco(request):
    p = request.POST['first']
    k = request.POST['last']
    l = request.POST['country']
    mem = Member(firstname=p, lastname=k, country=l)
    mem.save()
    return redirect("/")


def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")


def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})


def uprec(request,id):
    p = request.POST['first']
    k = request.POST['last']
    l = request.POST['country']
    mem = Member.objects.get(id=id)
    mem.firstname=p
    mem.lastname=k
    mem.country=l
    mem.save()
    return redirect("/")

