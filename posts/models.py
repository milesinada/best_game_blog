from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Theme(models.Model):
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.description

class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])