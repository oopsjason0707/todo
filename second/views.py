from django.shortcuts import render
from .models import Favourite, Todo


# Create your views here.

def index(request):
    return render(request, 'second/index.html')

def favourite(request):
    data = Favourite.objects.all()
    return render(request,"second/favourite.html",
    {'datas':data}
    )

def favoutie_detail(request):
    return render(request, "second/favourite_detail.html")

def todo_detail(request):
    return render(request, "second/todo_detail.html")
    

def todo(request):

    data = Todo.objects.all()

    if' group' in request.GET:
        data = data.filter(group__name=request.GET['group'])

    if 'end_date' in request.GET:
        data = data.filter(end_date__gte=request.GET['end_date'])

    return render(request, "second/todo.html", {'datas' : data.all()})


    





        