from django.db import connection
from django.shortcuts import render, redirect, render_to_response, HttpResponse
from django.views import generic

from user.models import ServantRequest
from .forms import *
from .models import *

# Create your views here.
def adminhome_view(request):
    return render(request, 'useradmin/adminhome.html')

def addactivity_view(request):
    form = ActivityCategoryForm

    if request.method == 'POST':
        form = ActivityCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('useradmin:add_activity')
    return render(request, 'useradmin/activity_category.html', {'form': form})

def addcamp_view(request):

    form = CampForm

    if request.method == 'POST':
        print("checking")
        form = CampForm(request.POST, request.FILES)

        if form.is_valid():
            print("Inside isvalid")
            form.save(commit=True)
            return redirect('useradmin:add_camp')

    return render(request, 'useradmin/add_camp.html', {'form': form})

def test_view(request):

    return render(request, 'useradmin/base.html')

def sample_view(request):

    return render(request, 'useradmin/test.html')

class CampListView(generic.ListView):
    template_name = 'useradmin/campview.html'
    context_object_name = 'camp_list'


    def get_queryset(self):
        return CampRegistration.objects.all()


def add_user_view(request):
    form = AddUserForm()
    # reguserform = RegUserForm()
    if request.method == 'POST':
        print("Check1")
        form = AddUserForm(request.POST)
        reguserform = RegUserForm()

        if form.is_valid():
            print("Check2")
            user = form.save()
            reg = reguserform.save(commit=False)
            reg.user = user
            reg.save()
            return redirect('useradmin:add_user')
    return render(request, 'useradmin/add_user.html', {'form': form})


def signup_servant_view(request):
    form = SignUpServantForm

    if request.method == 'POST':
        form = SignUpServantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('useradmin:servant_reg')

    return render(request, 'useradmin/servant_reg.html', {'form': form})


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def servantlist_view(request):
    servantdetail = RegServant.objects.all()
    return render(request, 'useradmin/servant_list.html', {'servantdetail': servantdetail})

def servantmanage_view(request, pk):
    if request.method == 'GET':
        #servant = RegServant.objects.get(id=pk)
        cursor = connection.cursor()
        cursor.execute("""SELECT *
                               FROM useradmin_regservant WHERE id ='%d'"""%(pk))
        dict = {}
        dict = dictfetchall(cursor)
        print(dict)
    return render(request, 'useradmin/servant_detail.html', {'dict': dict})


class NewsListView(generic.ListView):
    template_name = 'useradmin/newslist.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.all()

class NewsDetailView(generic.DetailView):
    model = News
    template_name ='useradmin/news_detail.html'


def add_news_view(request):
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('useradmin:add_news')

    return render(request, 'useradmin/add_news.html', {'form': form})

def ser_req_list(request):
    ser_req = ServantRequest.objects.filter(status='pending')
    return render(request, 'useradmin/servant_request_list.html', {'ser_req': ser_req})

def acceptbtn_view(request):
    if request.method == 'POST':
        if request.POST.get('accept'):
            accept = request.POST.get('accept')
            ServantRequest.objects.filter(pk=accept).update(status='accepted')

            #return HttpResponse(accept)
            return redirect('useradmin:servant_req')
        else:
            reject = request.POST.get('reject')
            ServantRequest.objects.filter(pk=reject).update(status='rejected')
            return redirect('useradmin:servant_req')

def maintaintype_view(request):
    type_form = MaintainTypeForm

    if request.method == 'POST':
        type_form = MaintainTypeForm(request.POST)

        if type_form.is_valid():
            type_form.save()
            return redirect('useradmin:add_type')
    return render(request, 'useradmin/add_type.html', {'type_form': type_form})

