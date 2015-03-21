from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from models import Note, Tag
from forms import NoteForm, TagForm
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test


def superuser_only(user):
    return (user.is_authenticated() and user.is_superuser)

@user_passes_test(superuser_only, login_url="/")
def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    tags = Tag.objects.all()
    return render(request, 'notes/index.html', {'notes':notes, 'tags':tags})

@user_passes_test(superuser_only, login_url="/")
def add_note(request):
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
            form.save()
            messages.add_message(request, messages.INFO, "Note added")
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form':form, 'note':note})

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
def note_body(request):
    note_id = None
    if request.method == 'GET':
        note_id = request.GET['note_id']

    note_body = None
    print Note.objects.get(pk=note_id)
    if note_id:
        note_body = Note.objects.get(pk=note_id)

    return HttpResponse(note_body.body)