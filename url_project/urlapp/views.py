from django.views.generic import DetailView
from .models import UrlModel
from .forms import UrlForm
from django.shortcuts import render, redirect


def url_new(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            model = UrlModel.objects.last()
            return redirect(model)
    else:
        form = UrlForm()
    return render(request, 'urlapp/urlmodel_form.html', {'form': form})


class DetailURLView(DetailView):
    model = UrlModel
