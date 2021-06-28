from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    desc = models.CharField(max_length=500)
    mdate = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class DecryptedPath(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dfilename = models.CharField(max_length=30)
    ddate = models.DateTimeField(default=now)
    fpath = models.FilePathField(path='media/decrypted/')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fpath


class EncryptedPath(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    edate = models.DateTimeField(default=now)
    efilename = models.CharField(max_length=30)
    fpath = models.FilePathField(path='media/encrypted_file/')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.fpath

