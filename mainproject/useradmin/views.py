from django.shortcuts import render, redirect
from django.views import generic

from .forms import ActivityCategoryForm, CampForm
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

