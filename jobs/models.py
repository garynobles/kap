from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.CharField(max_length=200)
    referenceurl = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.summary)

    class Meta:
        ordering = ["order"]

class Announcements(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-date"]
