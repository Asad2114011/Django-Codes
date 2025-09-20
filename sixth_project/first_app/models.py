from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    fathers_name=models.CharField()

    def __str__(self):
         return f"Roll:{self.roll}-{self.name}"