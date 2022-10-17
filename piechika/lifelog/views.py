from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import sleepLog

def indexView(request):
    sleeplogList = sleepLog.objects.order_by('-date')
    return render(request, 'lifelog/index.html', {'sleeplogList': sleeplogList})

class sleeplogListView(ListView):
    template_name = 'lifelog/sleeplogList.html'
    model = sleepLog
    context_object_name = 'sleeplogList'

class sleeplogDetailView(DetailView):
    template_name = 'lifelog/sleeplogDetail.html'
    model = sleepLog
    context_object_name = 'sleeplogDetail'

class sleeplogCreateView(CreateView):
    template_name = 'lifelog/sleeplogCreate.html'
    model = sleepLog
    fields = (
        'userId',
        'date',
        'staDateTime',
        'endDateTime',
        'sleepingTime'
    )
    success_url = reverse_lazy('index')

class sleeplogUpdateView(UpdateView):
    template_name = 'lifelog/sleeplogUpdate.html'
    model = sleepLog
    context_object_name = 'sleeplogUpdate'
    fields = (
        'userId',
        'date',
        'staDateTime',
        'endDateTime',
        'sleepingTime'
    )
    success_url = reverse_lazy('index')

class sleeplogDeleteView(DeleteView):
    template_name = 'lifelog/sleeplogDelete.html'
    model = sleepLog
    context_object_name = 'sleeplogDelete'
    success_url = reverse_lazy('index')
