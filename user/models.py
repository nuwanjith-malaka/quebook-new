from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class AskerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    

    def get_absolute_url(self):
        return reverse('asker', kwargs={'pk': self.user.pk})