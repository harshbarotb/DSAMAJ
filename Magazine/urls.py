from django.urls import path

from . import views

urlpatterns = [
    path('MagazinePage/', views.Magazine, name='Magazine'),
    path('EventCoverPage/', views.EventCoverPage, name='EventCoverPage'),
    path('EventImagePage/<str:i_Re_Enter_Id>', views.EventImagePage, name='EventImagePage'),
]
