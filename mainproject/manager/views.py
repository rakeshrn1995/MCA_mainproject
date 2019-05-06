from django.db import connection
from django.shortcuts import render, redirect
from .forms import SignUpServantForm
from .models import RegServant
from django.views.generic import ListView, CreateView, DeleteView, DetailView

# Create your views here.

def home_view(request):
    return render(request, 'manager/home.html')


def signup_servant_view(request):
    form = SignUpServantForm

    if request.method == 'POST':
        form = SignUpServantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manager:servant_reg')

    return render(request, 'manager/servant_reg.html', {'form': form})

def servantlist_view(request):
    servantdetail = RegServant.objects.all()
    return render(request, 'manager/servant_list.html', {'servantdetail': servantdetail})


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def servantmanage_view(request, pk):
    if request.method == 'GET':
        #servant = RegServant.objects.get(id=pk)
        cursor = connection.cursor()
        cursor.execute("""SELECT *
                               FROM RegServant WHERE id ='%d'"""%(pk))
        dict = {}
        dict = dictfetchall(cursor)
        print(dict)

    return render(request, 'manager/servant_detail.html', dict)