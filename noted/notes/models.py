from django.db import models
from django.template.defaultfilters import slugify

class Folder(models.Model):
    name = models.CharField(max_length=128, unique = True )
    slug = models.SlugField(default = ' ')

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Folder, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

# Create your models here.
class Note(models.Model):
    folder = models.ForeignKey(Folder, default = 0)
    label = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', related_name='notes', blank=True)

    def __unicode__(self):
        return self.label


class Tag(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __unicode__(self):
        return self.label