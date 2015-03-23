from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from models import Note, Tag, Folder
from forms import NoteForm, TagForm, FolderForm
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test

from django.http import JsonResponse


def superuser_only(user):
    return (user.is_authenticated() and user.is_superuser)

@user_passes_test(superuser_only, login_url="/")
def index_view(request):
    folders = Folder.objects.all()
    notes = Note.objects.all().order_by('-timestamp')
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'folders':folders,'notes':notes, 'tags':tags})



@user_passes_test(superuser_only, login_url="/")
def add_folder(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Folder, id=id)
    else:
        note = None

    if request.method =='POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, "Folder deleted")
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Folder added")
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = FolderForm(instance=folder)

    return render(request, 'notes/addfolder.html', {'form':form, 'note':note})


@user_passes_test(superuser_only, login_url="/")
def add_note(request, folder_name_slug):

    try:
        fold = Folder.objects.get(slug=folder_name_slug)
    except Folder.DoesNotExist:
                fold = None

    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method =='POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, "Note deleted")
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            if fold:
              note = form.save(commit = false)
              note.folder = fold
              note.save()
            messages.add_message(request, messages.INFO, "Note added")
#            return HttpResponseRedirect(reverse('notes:index'))
            return folder(request, folder_name_slug)
        else:
            print form.errors
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form':form, 'note':note, 'folder_slug' : folder_name_slug})

@user_passes_test(superuser_only, login_url="/")
def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None
    
    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag deleted')
            return HttpResponseRedirect(reverse('notes:index'))
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            t = form.save(commit=False)
            t.slug = slugify(t.label)
            t.save()
            messages.add_message(request,messages.INFO, 'Tag deleted')
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = TagForm(instance=tag)
    return render(request, 'notes/addtag.html', {'form':form, 'tag':tag})



@user_passes_test(superuser_only, login_url="/")
def note_content(request):
    note_id = None
    if request.method == 'GET':
        note_id = request.GET['note_id']

    note = None
    print Note.objects.get(pk=note_id)
    if note_id:
        note = Note.objects.get(pk=note_id)

    return JsonResponse({'title': note.label, 'body': note.body})

def folder(request, folder_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        folder = Folder.objects.get(slug=folder_name_slug)
        folders = Folder.objects.all()
        context_dict['folders'] = folders
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        notes = Note.objects.filter(folder=folder)

        # Adds our results list to the template context under name pages.
        context_dict['notes'] = notes
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
    except Folder.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'notes/folder.html', context_dict)
