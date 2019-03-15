from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.utils.translation import gettext as _


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    private = models.BooleanField(default=True)
    invite = models.CharField(max_length=10, blank=True, null=True)
    expdate = models.DateField(_("Expiration date"), default=date.today)
