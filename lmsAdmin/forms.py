from django import forms
from .models import SchoolClass,User
from django.forms.widgets import SelectMultiple

class AssignTeacherForm(forms.ModelForm):
    teachers = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_teacher=False))

    class Meta:
        model = SchoolClass
        fields = ['teachers']

class AssignStudentForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_teacher=False))

    class Meta:
        model = SchoolClass
        fields = ['students']
