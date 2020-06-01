from django.urls import path
from . import views

urlpatterns = [
    path('AdminDashbord/', views.BasicInfoHead, name='Dashboard'),
    path('Dashboard/', views.Dashboard, name='AdminDashbord'),
    path('FamilyHeadInfo/', views.MemHeadData, name='MemHeadData'),
    path('DeleteHeadData/<str:head_id>', views.DeleteHeadData, name='DeleteHeadData'),
    path('DeleteMemberData/<str:member_id>', views.DeleteMemberData, name='DeleteMemberData'),
    path('Show_Family/<str:head_id>', views.ShowFamily, name='Show_Family'),
    path('ShowFemale/', views.FemaleInfo, name='Show_Female'),
    path('CalculateAge/', views.CalCulateAge, name='CalCulateAge'),
    path('Eventcode/', views.Eventcode, name='Eventcode'),
    path('ShowMale/', views.MaleInfo, name='Show_Male'),
    path('BlogHomePage/', views.BlogHomePage, name='BlogHomePage'),
    path('BlogHomePageDataSave/', views.BlogHomePageDataSave, name='BlogHomePageDataSave'),
    path('Magazineupload/', views.Magazineupload, name='Magazineupload'),
    path('SaveMagazineData/', views.SaveMagazineData, name='SaveMagazineData'),
    path('EventPhotosPage/', views.EventPhotosPage, name='EventPhotosPage'),
    path('EventCoverImagesPage/', views.EventCoverImagesPage, name='EventCoverImagesPage'),
    path('EventImagesDashBoardHomePage/', views.EventImagesDashBoardHomePage, name='EventImagesDashBoardHomePage'),
    path('SubmitFamilyMember/', views.AddExtraFamilyMember, name='AddExtraFamilyMember'),
    path('AddFamilyMember/', views.AddFamilyMemberfFirstPageDirection, name='AddFamilyMemberfFirstPageDirection')
]
