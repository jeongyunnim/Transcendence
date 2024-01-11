from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from login.models import LoginData

class CreateLoginDataView(CreateView):
    model = LoginData
    fields = '__all__'
    template_view = 'login/login.html'
