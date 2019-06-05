from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TestModel
from django.urls import reverse_lazy


class FormListView(ListView):
    model = TestModel
    template_name = 'forms/post_list.html'


class FormDetailView(DetailView):
    model = TestModel
    template_name = "forms/post_view.html"


class FormCreateView(CreateView):
    template_name = 'forms/post_add.html'
    model = TestModel
    fields = '__all__'


class FormUpdateView(UpdateView):
    template_name = 'forms/post_edit.html'
    model = TestModel
    fields = '__all__'


class FormDeleteView(DeleteView):
    template_name = 'forms/post_delete.html'
    model = TestModel
    success_url = reverse_lazy('post_list')