from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Student, CourseProfile

class UserForm(forms.Form):
    username = forms.CharField(label="Username", help_text="30 characters or fewer. Letters, digits and @/./+/-/_  only.")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, help_text="Enter the same password as before, for verification.")

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','grad_year','major']
        labels = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'grad_year': 'Graduation Year',
        'major': 'Major',
        }

class CourseForm(forms.Form):
    difficulty = forms.IntegerField(min_value=1, max_value=5)
    rating = forms.IntegerField(min_value=1, max_value=5)
    size = forms.ChoiceField(choices=(('lecture', 'Lecture'), ('seminar', 'Seminar')), required=False)
    DAY_CHOICES = ((1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'),
        (5, 'Friday'))
    day = forms.MultipleChoiceField(choices=DAY_CHOICES, required=False,
        widget=forms.CheckboxSelectMultiple)
    TIME_CHOICES = ((1, '8 am'), (2, '9 am'), (3, '10 am'), (4, '11 am'), (5, '12 pm'),
        (6, '1 pm'), (7, '2 pm'), (8, '3 pm'), (9, '4 pm'), (10, '5 pm'), (11, '6 pm'),
        (12, '7 pm'), (13, '8 pm'), (14, '9 pm'))
    start_time = forms.ChoiceField(choices=TIME_CHOICES, required=False, label="Start Time")
    end_time = forms.ChoiceField(choices=TIME_CHOICES, required=False, label="End Time")
    area = forms.MultipleChoiceField(choices=((1, 'Hu'), (2, 'Sc'),
        (3, 'So')), required=False, widget=forms.CheckboxSelectMultiple)
    skills = forms.MultipleChoiceField(choices=((1, 'QR'), (2, 'WR'), (3, 'Lang')), required=False,
        widget=forms.CheckboxSelectMultiple)
    keywords = forms.CharField(help_text="Enter keyword search terms", widget=forms.Textarea())
    major = forms.MultipleChoiceField(choices=((1, 'yes'), (2, 'no')), required=False,
        label='Class in your major', widget=forms.CheckboxSelectMultiple)

    '''
  class Meta:
    model = CourseProfile
    fields = ['average_rating','average_difficulty','num_students','skill','area']
    labels = {
    'average_rating': 'Average Rating',
    'average_difficulty': 'Average Difficulty',
    'num_students': 'Approximate Number of Students',
    'skill': "Skills Requirement",
    'area': "Area Requirement",
    }
    '''
