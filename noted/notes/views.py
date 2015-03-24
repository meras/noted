from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from models import Note, Tag
from forms import NoteForm, TagForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'tags': tags})

@login_required()
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

@login_required()
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':
        id = request.POST.get('id')
        if id is not None:
            note = get_object_or_404(Note, id=id)

        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, "Note deleted")
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Note added")
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form, 'note': note})