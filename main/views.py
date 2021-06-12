import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import UsersForm
from .models import Users


def index(request):
    users = Users.objects.all()
    return render(request, "main/index.html", {"users": users})

class userCreate(CreateView):
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('main:index')

class userUpdate(UpdateView):
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('main:index')

def userDelete(request, pk):
    Users.objects.filter(pk=pk).delete()
    return redirect('main:index')