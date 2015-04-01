from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
                       url(r'^$', index_view, name='index'),
                       url(r'^addnote/', add_note, name='addnote'),
                       url(r'^editnote/', edit_note, name='editnote'),
                       url(r'^deletenote/', delete_note, name='deletenote'),
                       url(r'^addtag/', add_tag, name='addtag'),
                       url(r'^note/$', note_content, name='note'),
                       # url(r'^folder/(?P<folder_title_slug>[\w\-]+)/$', folder, name='folder'),
                       url(r'^fold/$', folder_content, name='folder_content'),
                       url(r'^addfolder/$', add_folder, name='addfolder')
)