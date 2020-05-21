from django.shortcuts import render
import urllib.request
import json
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Calendar
from .forms import CalendarForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from functools import partial
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

with open('almaz.json', 'r') as f:
    s = f.read()
    s = s.replace("'", '"')
    data = json.loads(s)

def home(request):
    return render(request, 'video/home.html')


def video(request):
    c = data['items']
    # c = json.dumps(d, indent=4, sort_keys=True)
    # return render(request, 'video/video.html', {'c': c})
    return render(request, 'video/video.html')

def jQeryYouTube(request):
    return render(request, 'video/jqery.html')

def calendar(request):
    return render(request, 'video/calendar.html')

class CalendarView(ListView):
    model = Calendar
    form_class = CalendarForm
    template_name = 'video/calendar.html'
    context_object_name = 'calendar'
    ordering = ['-date_posted']

class CalendarDetailView(DetailView):
    model = Calendar

# class CalendarCreateView(CreateView):
#     model = Calendar
#     template_name = 'video/calendar_form.html'
#     context_object_name = 'form'
#     form_class = CalendarForm
#     id_list = User.objects.filter(pk__in=[1, 2])
#     success_url = reverse_lazy('calendar')

    # def get_context_data(self, **kwargs):
    #     context = super(CalendarCreateView, self).get_context_data(**kwargs)
    #     id_list = User.objects.filter(pk__in=[1, 2])
    #     return context

def calendar_form(request):
    id_list = User.objects.filter(pk__in=[1, 2])
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('calendar')
    else:
        form = CalendarForm()

    context = {
        'form': form,
        'id_list': id_list

    }
    return render(request, 'video/calendar_form.html', context)
