from django.db import models

# Create your models here.
class SimpleCrud(models.Model):
      category_name=models.CharField(max_length=50,unique=True)
      category_code=models.IntegerField()
      category_description=models.TextField()
      category_status=models.CharField(max_length=20)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)