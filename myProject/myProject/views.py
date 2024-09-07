from django.shortcuts import render,redirect
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from myProject.forms import *

def signinPage(request):
    
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(username=username,password=password)
    
        if user:
            login(request,user)
            return redirect("homePage")
    
    return render(request,"signinPage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect("signinPage")

def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        user_type=request.POST.get("role")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        
        if password==confirm_password:
            user=Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=password,
            )
            return redirect("signinPage")
    
    return render(request,"signupPage.html")

@login_required
def homePage(request):

    return render(request,"home.html")

@login_required
def addResumeField(request):
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewResumeList') 
    else:
        form = ResumeForm()
        
    
    context={
            'form':form
        }
        
    return render(request,"addResumeField.html",context)

@login_required
def viewResumeList(request):
    
    resume=ResumeModel.objects.all()
    
    context={
        'resumes':resume
    }
    
    return render(request,"viewResumeList.html",context)


def resume_detail(request,id):
    resume=ResumeModel.objects.get(id=id)
    
    
    return render(request,"resume_detail.html",{'resume':resume})



def resume_edit(request, id):
    
    resume = get_object_or_404(ResumeModel, id=id)
    
    if request.method == 'POST':
        
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('resume_detail', id=resume.id) 
    else:
        form = ResumeForm(instance=resume)
    
    return render(request, 'resume_edit.html', {'form': form, 'resume': resume})


def resume_delete(request,id):
    
    resume=ResumeModel.objects.get(id=id).delete()
    
    return redirect("viewResumeList")