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
    INT_CHOICES = [(i*0.1, i*0.1) for i in range(1,51)]
    difficulty = forms.ChoiceField(initial=3.0, choices=INT_CHOICES, required=False)
    rating = forms.ChoiceField(initial=3.0,choices=INT_CHOICES, required=False)
    size = forms.ChoiceField(initial='E',choices=(('L', 'Lecture'), ('S', 'Seminar'), ('E','Either')), required=False)
    DAY_CHOICES = (('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'),
        ('F', 'Friday'))
    day = forms.MultipleChoiceField(label='Unwanted Days of the Week (will completely remove days selected)', choices=DAY_CHOICES, required=False,
        widget=forms.CheckboxSelectMultiple)
    TIME_CHOICES = ((8, '8 am'), (9, '9 am'), (10, '10 am'), (11, '11 am'), (12, '12 pm'),
        (13, '1 pm'), (14, '2 pm'), (15, '3 pm'), (16, '4 pm'), (17, '5 pm'), (18, '6 pm'),
        (19, '7 pm'), (20, '8 pm'), (21, '9 pm'))
    start_time = forms.ChoiceField(initial=8, choices=TIME_CHOICES, required=False, label="Earliest Start Time")
    end_time = forms.ChoiceField(initial=21,choices=TIME_CHOICES, required=False, label="Latest End Time")
    area = forms.MultipleChoiceField(label="Area Requirements", choices=(('YCHU', 'Humanities (Hu)'), ('YCSC', 'Sciences (Sc)'),
        ('YCSO', 'Social Sciences (So)')), required=False, widget=forms.CheckboxSelectMultiple)
    skills = forms.MultipleChoiceField(label="Skills Requirements", choices=(('YCQR', 'Quantitative Reasoning (QR)'), ('YCWR', 'Writing (WR)'), ("YCL", 'Foreign Language (L)')), required=False,
        widget=forms.CheckboxSelectMultiple)
    keywords = forms.CharField(label="Keywords (separate with commas):", widget=forms.Textarea(),
        required=False)
    major = forms.ChoiceField(choices=((2, 'Doesn\'t Matter'), (1, 'Yes'), (0, 'No')), required=False,
        label='Related to your major?', widget=forms.RadioSelect, initial=2)

class WeightForm(forms.Form):
    INT_CHOICES = [(i, i) for i in range(11)]
    difficulty_weight = forms.ChoiceField(initial=5, choices=INT_CHOICES, required=False, label="Difficulty")
    rating_weight = forms.ChoiceField(initial=5, choices=INT_CHOICES, required=False, label="Rating")
    size_weight = forms.ChoiceField(initial=5, choices=INT_CHOICES, required=False, label="Size")
    keyword_weight = forms.ChoiceField(initial=5, choices=INT_CHOICES, required=False, label="Keyword Match")
