
from django.contrib import admin
from django.urls import path

from myProject.views import *


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signinPage,name="signinPage"),
    path('signupPage/', signupPage,name="signupPage"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    path('homePage/', homePage,name="homePage"),
    path('addResumeField/', addResumeField,name="addResumeField"),
    path('viewResumeList/', viewResumeList,name="viewResumeList"),
    path('resume_delete/<str:id>', resume_delete,name="resume_delete"),
    path('resume_detail/<str:id>', resume_detail,name="resume_detail"),
    path('resume_edit/<str:id>', resume_edit,name="resume_edit"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
