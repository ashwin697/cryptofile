from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=260)
    content = RichTextUploadingField()
    views = models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=150)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title+ '-' +self.author

class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent =  models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)
     
    def __str__(self):
        return self.comment[0:18]+ "..." + self.user.username
    

