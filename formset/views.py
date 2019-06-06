from django.shortcuts import render
from django.forms import modelformset_factory
from .models import FormSetModel


def index(request):
    example_formset = modelformset_factory(FormSetModel, fields='__all__')

    if request.method == "POST":
        formset = example_formset(request.POST)
        instances = formset.save()

    formset = example_formset(queryset=FormSetModel.objects.all())
    # formset = example_formset(queryset=FormSetModel.objects.all())

    vars = {
        'formset': formset
    }

    return render(request, 'formset/index.html', vars)