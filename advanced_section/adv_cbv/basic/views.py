from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'

    # school_list - context by default
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'

    # school - context by default
    model = models.School
    template_name = 'basic/school_detail.html'

