from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.


class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True,max_length = 100)
    created_date = models.DateTimeField('Date created',default=timezone.now)


    def __str__(self):
        return self.email
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)
