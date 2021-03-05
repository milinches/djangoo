from django.shortcuts import render
from django.views import generic
from .models import Track

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'project/index.html'

class ListPageN(generic.ListView):
    template_name = 'project/list_view.html'
    queryset = Track.objects.filter(status=0).order_by('-time')
    context_object_name = 'track_page_n'

class ListPageD(generic.ListView):
    template_name = 'project/list_viewd.html'
    queryset = Track.objects.filter(status=1).order_by('-time')
    context_object_name = 'track_page_d'

class ListPageO(generic.ListView):
    template_name = 'project/list_viewo.html'
    queryset = Track.objects.filter(status=2).order_by('-time')
    context_object_name = 'track_page_o'

class DetailPage(generic.DetailView):
    model = Track
    context_object_name = 'track_detail'
    template_name = 'project/list_detail.html'