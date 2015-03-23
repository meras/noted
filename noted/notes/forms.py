from django import forms
from notes.models import Note, Tag, Folder


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)





class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('label', 'body', 'tags')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)
