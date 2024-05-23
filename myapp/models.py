from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    post_date = models.DateField()
    image = models.ImageField(upload_to='static/')
    paragraph = models.TextField(max_length=1000)
    more_details_for_the_dedicated_page = models.TextField(max_length=1000,default=' ')