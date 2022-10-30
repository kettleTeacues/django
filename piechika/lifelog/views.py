from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.db.models import Count

from .models import sleepLog, condition
from .consts import ITEM_PER_PAGE

def indexView(request):
    sleeplogList = sleepLog.objects.order_by('-date')
    
    paginator = Paginator(sleeplogList, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)

    return render(
        request,
        'lifelog/index.html',
        {'page_obj': page_obj}
    )


class sleeplogListView(LoginRequiredMixin, ListView):
    template_name = 'lifelog/sleeplogList.html'
    model = sleepLog
    def get_queryset(self):
        return sleepLog.objects.filter().order_by('-id')

    paginate_by = ITEM_PER_PAGE
    context_object_name = 'sleeplogList'

class sleeplogDetailView(LoginRequiredMixin, DetailView):
    template_name = 'lifelog/sleeplogDetail.html'
    model = sleepLog
    context_object_name = 'sleeplogDetail'

class createConditionView(LoginRequiredMixin, CreateView):
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

class sleeplogCreateView(LoginRequiredMixin, CreateView):
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

class sleeplogUpdateView(LoginRequiredMixin, UpdateView):
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
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

class sleeplogDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'lifelog/sleeplogDelete.html'
    model = sleepLog
    context_object_name = 'sleeplogDelete'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})