from django.db import models

class Usercsv(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s" % (self.title)

    def __str__(self):
        return "%s" % (self.title)
