from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True) #null means it can be empty in the database and blank means it can be empty when submitting a form
    updated = models.DateTimeField(auto_now=True) #Creates a time stamp for when the room was last updated
    created = models.DateTimeField(auto_now_add=True) #Creates a time stamp for when the room was created

    def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True, null=True)
    # add additional fields to the profile model
    def __str__(self):
        return str(self.user)

class Account(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=True, null=True)
    # add additional fields to the account model

    class Meta:
        unique_together = ('profile', 'username')

    def __str__(self):
        return f"({self.profile.user.username}) - {self.username}"


class MultipleImage(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    images = models.ImageField(null=False, blank=False)

    def __str__(self):
        return str(self.account.username)
