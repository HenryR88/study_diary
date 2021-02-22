from django.db import models
from django.contrib.auth.models import User
from smartfields import fields


class Topic(models.Model):
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    file = fields.FileField(upload_to='study_diaries/media/', blank=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) >= 40:
            return f"{self.text[:40]}..."
        else:
            return self.text


class Document(models.Model):
    title = models.CharField(max_length=250)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='study_diaries/media', blank=True)













