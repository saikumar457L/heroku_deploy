from django.db import models


from django.conf import settings


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    date_of_birth = models.DateTimeField(blank=True,null=True)
    photo = models.ImageField(upload_to='user/%y/%m/%d/',blank=True)

    def __str__ (self):
        return "Profile for user {}".format(self.user.username)

class Marktry(models.Model):
    body=models.TextField()

    def __str__ (self):
        return "some info"
