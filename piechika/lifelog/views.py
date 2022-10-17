from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import sleepLog, condition

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

class createConditionView(CreateView):
    template_name = 'lifelog/conditionForm.html'
    model = condition
    fields = (
        'rate',
        'text',
        'sleepLogId'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sleepLog'] = sleepLog.objects.get(pk = self.kwargs['pk'])

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.sleepLogId.id})

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
