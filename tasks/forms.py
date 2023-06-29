from django import forms
from .models import Task
class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control my-3 rounded-2'
        self.fields['title'].widget.attrs['style'] = "padding: 12px 15px;border: 2px solid gray"
        self.fields['title'].label = ''
        self.fields['title'].required = True

