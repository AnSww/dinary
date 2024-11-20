from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

    title = forms.CharField(label='Название задачи')
    description = forms.CharField(label='Описание задачи', widget=forms.Textarea)
    status = forms.ChoiceField(label='Статус', choices=Task.STATUS_CHOICES)