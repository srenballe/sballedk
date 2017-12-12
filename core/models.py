from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    url = models.CharField(max_length=200, blank=True)
    active = models.BooleanField()
    dateFinished = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Text(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title