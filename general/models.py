from statistics import mode
from django.db import models

# Create your models here.
class Repo(models.Model):
    matric_no=models.CharField(max_length=6)
    project_title=models.CharField(max_length=200)
    year=models.CharField(max_length=4)
    document=models.FileField(upload_to='pdf/general')
        
    
    def __str__(self):
        return self.matric_no

