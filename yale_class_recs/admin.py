from django.contrib import admin

from .models import EvaluationComments
from .models import EvaluationCourseNames
from .models import EvaluationCourses
from .models import EvaluationProfessors

admin.site.register(EvaluationComments)
admin.site.register(EvaluationCourseNames)
admin.site.register(EvaluationCourses)
admin.site.register(EvaluationProfessors)
