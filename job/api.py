## views API

from django.contrib.auth import decorators
from rest_framework.response import Response 
from job.serializers import JobSerializer
from rest_framework import  serializers
from .models import Job
from rest_framework.decorators import api_view


@api_view()
def JobListAPi(request):

    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many = True).data

    return Response({'data':data})