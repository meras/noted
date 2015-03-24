from django.db import models


class Folder(models.Model):
    """
    Each user account contains at least one Folder.
    Folders are used to organize collections of Notes.
    Each notebook has a name, which must be unique within the
    owner's account. Folders can be grouped into stacks, which
    contain one or more notebooks, but cannot directly contain notes.
    """
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, default=0)
    #notes = models.ManyToManyField('Note', blank=True)

    def __unicode__(self):
        return self.title


class Note(models.Model):
    """
    A Note represents a single unit of information
    A note is made up of a single title and body section (the content)
    Timestamps are automatically generated with a creation of a new note
    Each note can have many Tags.Each note exists in only one Folder at a time.
    It is not possible for a single note to exist in two different folders.
    If the note is copied, a new note is created. If the new note is edited, the original will not be changed.
    """
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