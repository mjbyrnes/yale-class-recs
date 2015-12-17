from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserForm, StudentForm, CourseForm

from .models import Student

def index(request):
    return HttpResponse(index.html)

class CoverView(generic.ListView):
  template_name = "yale_class_recs/cover.html"
  def get_queryset(self):
    return None

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
      form2 = CourseForm()

  return render(request, 'yale_class_recs/info.html', {'form': form,'form2': form2})

def get_new_user_info(request):
  error = 0

  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      grad_year = form.cleaned_data['grad_year']
      major = form.cleaned_data['major']
    else:
      error = "Be sure to fill in all of the fields!"

    form = UserForm(request.POST)
    if form.is_valid() and error == 0:
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      if User.objects.filter(username=username).count() != 0:
        error = "The username you selected is already in use. Please choose a new one"
      elif password != form.cleaned_data['confirm_password']:
        error = "The passwords entered do not match"
      else:
        new_user = User.objects.create_user(username, password, first_name=first_name, 
          last_name=last_name)
        new_user.save()
        student = Student.objects.create(first_name=first_name, last_name=last_name,
          grad_year=grad_year, major=major, username=new_user)
        student.save()
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/yale_class_recs/user/' + username)
          else:
            error = "An account for this user already exists, but it is deactivated"
        else:
          error = "There was a problem creating your account. Please try again"

    else:
      error = "Be sure to fill in all of the fields!"


  form = UserForm()
  form2 = StudentForm()
  context = {
    'form': form,
    'form2': form2,
    'error': error,
  }
  return render(request, 'yale_class_recs/user_info.html', context)

def user_home(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/yale_class_recs/login')
  context = {
    'username': request.user.username,
  }
  return render(request, 'yale_class_recs/user_home_page.html', context)

