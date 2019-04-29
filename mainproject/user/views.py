
from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from login.forms import SignupForm
from manager.models import RegServant

from login.models import RegUser
from .forms import *
from django.shortcuts import redirect
from login import config

# Create your views here.

def memreg_view(request):

    form = MemRegForm()

    if request.method == 'POST':
        form = MemRegForm(request.POST)

        if form.is_valid():
            print("Inside is valid")
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
        form = MaintainForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user:maintain')

    return render(request, 'user/maintain.html', {'form': form})


class BookListView(generic.ListView, FormMixin):
    template_name = 'user/book_list.html'
    form_class = BookList_Form

    context_object_name = 'book_list'

    def get_queryset(self):
        return BookDetail.objects.all()

    def get_context_data(self):
        context = super(BookListView, self).get_context_data()

        context['form'] = self.get_form()

        return context






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

# def dictfetchall(cursor):
#     """Return all rows from a cursor as a dict"""
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]

def load_lang(request):
    print("hiii")
    lang = request.GET.get('id')
    # job = JobType.objects.get()
    print(type(lang))
    if lang == '1':
        language = BookDetail.objects.all()
    else:

        language = BookDetail.objects.filter(language=lang)
        print(language)
    return render(request, 'user/load_lang.html', {'language': language})

    # if request.is_ajax() and request.GET:
    #     print("hiii")
    #     lang = request.GET.get('id')
    #     # job = JobType.objects.get()
    #     cursor = connection.cursor()
    #     cursor.execute("""
    #     select * from user_bookdetail where language=%s
    #     """,[lang])
    #     #language = BookDetail.objects.filter(language=lang)
    #     dict = dictfetchall(cursor)
    #     print(dict)
    #     r = json.dumps(dict[0])
    #     return JsonResponse(r, safe=False)
        #for l in language:
           # print(l.book_name)
       # return HttpResponse(dict)

# def load_lang_view(request):
#     if request.method == 'POST':
#         form = BookList_Form(request.POST)
#
#         if form.is_valid():
#             print("Inside is valid")
#             return redirect('user:book_list')
#     else:
#         form = BookList_Form()
#     return render(request, 'user/book_list.html', {'form': form})

# class Member_ListView(generic.ListView):
#     template_name = 'user/mem_list.html'
#     form_class = MemberList_Form
#
#     context_object_name = 'member_list'
#
#     def get_queryset(self):
#         return MemReg.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(Member_ListView, self).get_context_data(**kwargs)
#         context['u_id'] = str(config.u_id)
#         return context


# class UserProfileView(generic.UpdateView):
#     model = RegUser
#     form_class = UserProfileUpdateForm, UserUpdateForm
#     template_name = 'user/profile_update.html'


def member_list_view(request):
    mem_detail = MemReg.objects.all()
    user = config.u_id
    return render(request, 'user/mem_list.html', {'mem_detail': mem_detail})
