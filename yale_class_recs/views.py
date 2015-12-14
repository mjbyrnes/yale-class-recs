from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from .forms import StudentForm

def index(request):
    return HttpResponse(index.html)

class CoverView(generic.ListView):
  template_name = "yale_class_recs/cover.html"
  def get_queryset(self):
    return None

class IndexView(generic.ListView):
  template_name = "yale_class_recs/index.html"
  def get_queryset(self):
    return None
  def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InfoForm()

    return render(request, 'index.html', {'form': form})

def get_name(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = StudentForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
          return HttpResponseRedirect('/thanks/')

  # if a GET (or any other method) we'll create a blank form
  else:
      form = StudentForm()

  return render(request, 'yale_class_recs/info.html', {'form': form})
