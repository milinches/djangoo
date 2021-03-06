from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Track

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'project/index.html'

class ListPage(generic.ListView):
    template_name = 'project/list_view.html'
    queryset = Track.objects.all().order_by('-time')
    context_object_name = 'track_page_n'

class DetailPage(generic.DetailView):
    model = Track
    context_object_name = 'track_detail'
    template_name = 'project/list_detail.html'

class CreateTrack(CreateView):
    model = Track
    fields = ['tracking_number', 'slug', 'sender', 'receiver', 'signed_for_by', 'date', 'location', 'destination', 'status']

class UpdateTrack(UpdateView):
    model = Track
    fields = ['tracking_number', 'slug', 'sender', 'receiver', 'signed_for_by', 'date', 'location', 'destination', 'status']

class DeleteTrack(DeleteView):
    model = Track
    success_url = reverse_lazy('project:list')


