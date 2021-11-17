
from django.urls import path, include
from . import views, api

app_name = 'job'
urlpatterns = [
    
    path('', views.job_list, name = 'job_list'),
    path('add', views.add_job, name= 'add_job' ),
    path('<str:slug>', views.job_detail, name= 'job_detail' ),

    # API 
    path('api/jobs', api.JobListAPi, name= 'joblistapi' ),
    path('api/jobs/<int:id>', api.job_detail_api, name= 'job_detail_api' ),

    ## class based views
    path('api/v2/jobs/', api.JobLiastApi.as_view(), name= 'job_list_api' ),
    path('api/v2/jobs/<int:id>', api.JobDeaDetail.as_view(), name= 'job_detail' ),
     
     
    
]