from django.db import models
from django.contrib.auth.models import User
from time import time
import hashlib

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

def get_profile_file_name(instance, filename):
    return "uploaded_profiles/%s_profile_%s" % (str(time()).replace('.','_'), filename)


class Ribbit(models.Model):
    content = models.CharField(max_length=60)
    pic = models.FileField(upload_to=get_upload_file_name)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

class UserProfile(models.Model):
    gravatar_url = models.FileField(upload_to=get_profile_file_name, default='/static/gfx/default.jpg')
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
