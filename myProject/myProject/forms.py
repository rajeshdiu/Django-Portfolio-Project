from django import forms
from myApp.models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = [
            'title', 'description', 'file','profile_pic', 
            'name', 'email', 'phone_number', 
            'address', 'linkedin_url', 'github_url', 
            'portfolio_url', 'education', 'experience', 'skills'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Resume Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Brief Description'}),
            
            'profile_pic': forms.ClearableFileInput(attrs={'multiple': False}),
            
            'file': forms.ClearableFileInput(attrs={'multiple': False}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Your Address'}),
            'linkedin_url': forms.URLInput(attrs={'placeholder': 'LinkedIn URL'}),
            'github_url': forms.URLInput(attrs={'placeholder': 'GitHub URL'}),
            'portfolio_url': forms.URLInput(attrs={'placeholder': 'Portfolio URL'}),
            'education': forms.Textarea(attrs={'placeholder': 'Your Education'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Your Experience'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Your Skills'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False  