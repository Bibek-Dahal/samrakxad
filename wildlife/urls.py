app_name = 'wildlife'
from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.ImageUploadView.as_view(),name='homepage')
]