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

class ServantListView(ListView):
    template_name = 'manager/home.html'
    queryset = RegServant.objects.all()

