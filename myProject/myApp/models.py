from django.db import models

from django.contrib.auth.models import AbstractUser


class Custom_user(AbstractUser):
    
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer')
    ]
    
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    
    def __str__(self):  
        
        return f"{self.user_type}-{self.username}"
    

class ResumeModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    # Additional fields
    profile_pic=models.ImageField(upload_to="Media/Pro_pic",null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or 'Untitled'


    
    
    
    
    
    