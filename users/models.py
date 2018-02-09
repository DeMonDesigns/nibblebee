from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=300)
    bio = RichTextField()
    location = models.CharField(max_length=100)
    sex_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('N', '')
    ]
    sex = models.CharField(max_length=10, choices=sex_choices, default='N')
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile-image', blank=True, default='default_pic.jpg')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile(user=kwargs['instance']).save()

post_save.connect(create_profile, sender=User)
