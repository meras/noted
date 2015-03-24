from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index_view, add_note, addnote, add_tag, note_content, folder, add_folder

urlpatterns = patterns('',
	url(r'^$', index_view, name='index'),
	url(r'^folder/(?P<folder_name_slug>[\w\-]+)/add_note/$', add_note, name='add_note'),
    url(r'^addnote/$', addnote, name='addnote'),
	url(r'^addtag/$', add_tag, name='addtag'),
	url(r'^note/$', note_content, name='note'),
    url(r'^folder/(?P<folder_name_slug>[\w\-]+)/$', folder, name='folder'),
    url(r'^addfolder/$', add_folder, name='addfolder')
	)