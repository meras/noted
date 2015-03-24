from django import forms
from models import Note, Tag#, Folder


class NoteForm(forms.ModelForm):
    """

    """

    class Meta:
        model = Note
        fields = ('title', 'body', 'tags')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)


# class FolderForm(forms.ModelForm):
#     class Meta:
#         model = Folder
#         fields = ('title', )
