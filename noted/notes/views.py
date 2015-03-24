from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from models import Note, Tag
from forms import NoteForm, TagForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.html import strip_tags


def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'tags': tags})


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
        if form.is_valid():
            note = form.save()
            messages.add_message(request, messages.INFO, "Note added")
            # return HttpResponseRedirect(reverse('notes:index'))
            # return JsonResponse({'title': note.title, 'body': note.body, 'timestamp': note.timestamp})
            return render(request, 'notes/note_entry.html', {'note': note})


# from forms import FolderForm
#
# def add_folder(request):
#     # A HTTP POST?
#     if request.method == 'POST':
#         form = FolderForm(request.POST)
#
#         # Have we been provided with a valid form?
#         if form.is_valid():
#             # Save the new category to the database.
#             form.save(commit=True)
#
#             # Now call the index() view.
#             # The user will be shown the homepage.
#             return HttpResponseRedirect(reverse('notes:index'))
#         else:
#             # The supplied form contained errors - just print them to the terminal.
#             print form.errors
#     else:
#         # If the request was not a POST, display the form to enter details.
#         form = FolderForm()
#
#     # Bad form (or form details), no form supplied...
#     # Render the form with error messages (if any).
#     return render(request, 'notes/addfolder.html', {'form': form})