from django.urls import path
from . import views, apiViews

urlpatterns = [
    path('Familyentry/', views.Familyentry, name='Familyentry'),
    path('FormReg/', views.Form_Submission, name='FormSubmit'),
    path('AddFCode/', views.Fcode, name='FormSubmited'),
    path('getFamilycode/', apiViews.getFamilycode, name='getFamilycode'),
    path('UserEntryLogIn/', views.DoLoginUser, name='DoLoginUser'),
    path('LogInPage/', views.LogInPage, name='DoLoginUser'),
   # path('addData/', views.addData, name='addData')

]
