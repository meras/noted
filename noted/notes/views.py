from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from models import *
from forms import NoteForm, TagForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.html import strip_tags

@login_required()
def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    folders = Folder.objects.all()
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'tags': tags, 'folders': folders})


@login_required
def add_tag(request):
    """

    :param request:
    :return:
    """
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
            messages.add_message(request, messages.INFO, 'Tag deleted')
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = TagForm(instance=tag)
    return render(request, 'notes/addtag.html', {'form': form, 'tag': tag})


def note_content(request):
    """

    :param request:
    :return:
    """
    note_id = None
    if request.method == 'GET':
        note_id = request.GET['note_id']

    note = None
    if note_id:
        note = Note.objects.get(pk=note_id)

    return JsonResponse({'title': note.title, 'body': note.body})


@login_required
def edit_note(request):
    if request.is_ajax():
        id = request.POST.get('id')
        note = get_object_or_404(Note, id=id)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.add_message(request, messages.INFO, "Note added")
            #return JsonResponse({'title': note.title,'preview': strip_tags(note.body[:80])})
            return render(request, 'notes/note_entry.html', {'note': note})


@login_required
def delete_note(request):
    if request.is_ajax():
        id = request.POST.get('id')
        if id is not None:
            note = get_object_or_404(Note, id=id)

        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, "Note deleted")
            return HttpResponse("OK")


@login_required
def add_note(request):
    if request.is_ajax():
        form = NoteForm(request.POST)
        folder_name = request.POST.get('folder_name')
        if form.is_valid():
            note = form.save(commit=False)
            note.folder = Folder.objects.get(slug=folder_name)
            note.save()
            # return HttpResponseRedirect(reverse('notes:index'))
            # return JsonResponse({'title': note.title, 'body': note.body, 'timestamp': note.timestamp})
            return render(request, 'notes/note_entry.html', {'note': note})


from forms import FolderForm

@login_required()
def add_folder(request):
    id = request.GET.get('id', None)
    if id is not None:
        folder = get_object_or_404(Folder, id=id)
    else:
        folder = None

    if request.method =='POST':
        if request.POST.get('control') == 'delete':
            folder.delete()
            messages.add_message(request, messages.INFO, "Folder deleted")
            return HttpResponseRedirect(reverse('notes:index'))

        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Folder added")
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = FolderForm(instance=folder)

    return render(request, 'notes/addfolder.html', {'form':form, 'folder':folder})


def folder(request, folder_title_slug):
    # Create a c ontext dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        folder = Folder.objects.get(slug=folder_title_slug)
        folders = Folder.objects.all()
        context_dict['thisFolder'] = folder
        context_dict['folders'] = folders
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        notes = Note.objects.filter(folder=folder)

        # Adds our results list to the template context under name pages.
        context_dict['notes'] = notes
        context_dict['folder_slug'] = folder_title_slug
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
    except Folder.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'notes/index.html', context_dict)