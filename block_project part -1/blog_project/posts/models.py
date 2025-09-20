from django.db import models
from catagories.models import catagory
from author.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField()
    catagory=models.ManyToManyField(catagory)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title