from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import sleepLog

class sleeplogListView(ListView):
    template_name = 'lifelog/sleeplogList.html'
    context_object_name = 'sleeplogList'
    model = sleepLog

class sleeplogDetailView(DetailView):
    template_name = 'lifelog/sleeplogDetail.html'
    context_object_name = 'sleeplogDetail'
    model = sleepLog