from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
GRADE = [
    ('10','10'),
    ('11','11')
]
class AskerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="john", max_length=20)
    last_name = models.CharField(default="doe", max_length=20)
    photo = models.ImageField(null=True, blank=True)
    school = models.CharField(default='sample shool', max_length=50)
    grade = models.CharField(choices=GRADE, default='10', max_length=2)
    city = models.CharField(default='sample city', max_length=20)

    def get_absolute_url(self):
        return reverse('asker', kwargs={'pk': self.user.pk})