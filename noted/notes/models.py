from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(User)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', related_name='notes', blank=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.label

class Folder(models.Model):
    title = models.CharField(max_length=50)
    #owner = models.ForeignKey(User)
    note = models.ManyToManyField(Note)

    def __unicode__(self):
        return self.title