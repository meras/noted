from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index_view, add_note, add_tag, note_content, edit_note, delete_note

urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^addnote/', add_note, name='addnote'),
	url(r'^editnote/', edit_note, name='editnote'),
	url(r'^deletenote/', delete_note, name='deletenote'),
	url(r'^addtag/', add_tag, name='addtag'),
	url(r'^note/$', note_content, name='note'),
	)