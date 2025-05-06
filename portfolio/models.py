from django.db import models

from django.db import models

class PortfolioEntry(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

