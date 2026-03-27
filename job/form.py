from django import forms
from .models import Apply , Job
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control'}),
        }   

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner', 'slug']