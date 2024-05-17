from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'explanation', 'due_date']  # 'description'을 'explanation'으로 수정
