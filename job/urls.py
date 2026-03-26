
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.job_list),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
]