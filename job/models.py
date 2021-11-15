from django.contrib.admin.filters import ChoicesFieldListFilter
from django.db import models

# Create your models here.

'''
Django model field 
    - html widget
    - Validation
    - DB size 
'''

JOB_TYPE_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
   
)

def image_upload(instance, filename):
    imagename, extenstion = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id, instance.id, extenstion)


class Job(models.Model): # Table 


    title = models.CharField(max_length= 100)  # column
    job_type = models.CharField(max_length=15, choices = JOB_TYPE_CHOICES)
    description = models.TextField(max_length= 1000)
    published_at =  models.DateTimeField(auto_now= True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experence = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    def __str__(self):
        return self.title


class Category( models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name