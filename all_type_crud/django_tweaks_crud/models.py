from django.db import models

# Create your models here.
class CrudWithTweaks(models.Model):
      category_name=models.CharField(max_length=50,unique=True)
      category_code=models.IntegerField()
      category_description=models.TextField()
      choices=(('Active','Active'),('Inactive','Inactive'))
      category_status=models.CharField(max_length=20,choices=choices)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)