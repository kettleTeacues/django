from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import sleepLog

class Index(ListView):
    model = sleepLog