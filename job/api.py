## views API

from django.contrib.auth import decorators
from rest_framework.response import Response 
from job.serializers import JobSerializer
from rest_framework import  serializers, generics 
from .models import Job
from rest_framework.decorators import api_view


@api_view(['GET'])
def JobListAPi(request):

    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many = True).data

    return Response({'data':data})
@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = Job.objects.get(id = id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})

class JobLiastApi(generics.ListCreateAPIView):
    model =  Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer 

class JobDeaDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Job.objects.all()
    serializer_class = JobSerializer 
    lookup_field = 'id'
