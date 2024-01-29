from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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


class SchoolCreateView(CreateView):
    # school_form.html waiting by default
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    # school_confirm_delete.html waiting by default
    # school - context by default
    model = models.School
    success_url = reverse_lazy("basic:list")

