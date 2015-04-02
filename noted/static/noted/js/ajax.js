/*global $:false, jQuery:false */

function newNote() {
    var csrftoken = $.cookie('csrftoken');
    var folder_id = $('.folder-list>.active>a').attr("data-folderid");

    var data = {
        title: "New Note",
        body: " ",
        folder_id: folder_id,
        csrfmiddlewaretoken: $.cookie('csrftoken')
    };

    $.post("/notes/addnote/", data).success(function (data) {
        $('.list-group').prepend(data);
    });
}

//edit an existing note
function saveChanges() {
    var note_id = $('.note-info').attr('id');
    var csrftoken = $.cookie('csrftoken');
    var note_title = $('.note-info > section').text();
    var note_content = $('.editor').html();
    var data = {
        id: note_id,
        title: note_title,
        body: note_content,
        csrfmiddlewaretoken: $.cookie('csrftoken')
    };

    $.post("/notes/editnote/", data).success(function (data) {
        //$('#notelist [data-noteid=' + note_id + ']').replaceWith(data);
        var note = $('#notelist a[data-noteid=' + note_id + ']');
        $(note).find('strong').html(data.title);
        $(note).find('.preview').html(data.preview);
    });
}

function getNote(thisRef) {
    var note_id = thisRef.attr("data-noteid");
    $.getJSON('/notes/note/', {note_id: note_id}, function (data) {
        $('.note-info').attr('id', note_id);
        $('.note-info > section').html(data.title);
        $('.editor').html(data.body);
    });
}

function getNoteList(thisRef) {
    var folder_id = thisRef.attr("data-folderid");
    $.get('/notes/fold/', {folder_id: folder_id}, function (data) {
        $('#notelist>.list-group').empty().html(data);
        getNote($('#notelist .note').first());
    });
}

function validateURL(textval) {
    var urlregex = new RegExp( "^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");
    return urlregex.test(textval);
}


$(document).ready(function () {
    // retrieve a list of notes that belong to a folder
    $('.folder').on('click', function () {
        getNoteList($(this));
        $('.folder-list>.active').removeClass('active');
        $(this).parent().addClass('active');
    });

    // retrieve a note once clicked on a list
    $('#notelist').on('click', '.note', function () {
        getNote($(this));
        $('#notelist .active').removeClass('active');
        $(this).addClass('active');
    });

    // this creates a note as a new instance
    $('#new').on('click', function () {
        newNote();
    });


    //delete an existing note
    $('#delete').on('click', function () {
        var note_id = $('.note-info').attr('id');
        var note_title = $('.note-info > section').html();
        var csrftoken = $.cookie('csrftoken');
        var data = {
            id: note_id,
            control: 'delete',
            csrfmiddlewaretoken: $.cookie('csrftoken')
        };

        $.ajax({
            type: "POST",
            url: "/notes/deletenote/",
            data: data,
            success: function () {
                $('[data-noteid=' + note_id + ']').remove();
                $('.editor').empty().append("<h1 class='text-center'>No note selected<h1>");
            }
        });
    });

    $('#save').on('click', function () {
        saveChanges();
    });

    $('.editor').on({
        paste: function () {
            console.log(this);
        },
        input: function () {
            var text = $('.editor').text();
            var wordCount = text.trim().split(' ').length;

            $('#count').html(wordCount);
        }
    });
    $('.editor').focus();
});

