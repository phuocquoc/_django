from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
# Create your models here.


class Profile(models.Model):
    student = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default='profiles/default.jpg')

    def __str__(self):
        return self.username


class Skill(models.Model):
    name_choise = [
        ('Django', 'Django'),
        ('Python', 'Python'),
        ('VueJS', 'VueJS')
    ]
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(choices=name_choise,
                            null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def Create_Profile(sender, instance, created, **kwargs):
    if created:
        student = instance
        profile = Profile.objects.create(
            student=student,
            username=student.username,
            email=student.email,
            name=student.last_name,
        )


def Delete_Profile(sender, instance, **kwargs):
    print('Delete ok')


post_save.connect(Create_Profile, sender=User)
post_delete.connect(Delete_Profile, sender=Profile)
