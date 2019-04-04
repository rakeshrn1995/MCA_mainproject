from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from login.forms import SignupForm

from manager.models import RegServant
from .models import BookDetail
from .forms import *
from django.shortcuts import redirect

from login import config

# Create your views here.

def memreg_view(request):

    form = MemRegForm()

    if request.method == 'POST':
        form = MemRegForm(request.POST)

        if form.is_valid():
            print("Inside isvalid")
            form.save(commit=True)
            return redirect('user:mem_reg')

    return render(request, 'user/mem_reg.html', {'form': form})




def home_page(request):
    return render(request, 'user/Userbase.html')


def book_detail_view(request):
    form = BookDetailForm()

    if request.method == 'POST':
        print("*********")
        print(config.username)
        print('/////////////')
        form = BookDetailForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('user:bookdetail')
    return render(request, 'user/Bookdetail.html', {'form': form})


def profile_view(request):
    u_form = UserUpdateForm
    p_form = UserProfileUpdateForm

    return render(request, 'user/profile_update.html', {'u_form': u_form, 'p_form': p_form})

def check_view(request):
    post = BookDetail.objects.get(id=5)
    context={
        'post': post
    }
    return render(request, 'user/check.html', context)

def maintain_view(request):
    form = MaintainForm()
    if request.method == 'POST':
        print("*********")
        print(config.username)
        print('/////////////')
        form = MaintainForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('user:maintain')

    return render(request, 'user/maintain.html', {'form': form})


class BookListView(generic.ListView):
    template_name = 'user/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return BookDetail.objects.all()

class BookDetailView(generic.DetailView):
    model = BookDetail
    template_name ='user/detail.html'


def servant_request_view(request):
    if request.method == 'POST':
        form = ServantReqForm(request.POST)

        if form.is_valid():
            print("Inside isvalid")
            form.save(commit=True)
            return redirect('user:servant_request')
    else:
        form = ServantReqForm()
    return render(request, 'user/servant_request.html', {'form': form})


def load_servants(request):
    print("hiii")
    job = request.GET.get('job')
    # job = JobType.objects.get()
    servants = RegServant.objects.filter(job_type=job).order_by('first_name')
    return render(request, 'user/load_servants.html', {'servant': servants})