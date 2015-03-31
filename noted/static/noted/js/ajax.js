//edit an existing note
function saveChanges() {
    var note_id = $('.note-info').attr('id');
    var csrftoken = $.cookie('csrftoken');
    var note_title = $('.title').text();
    var note_content = $('.editor').html();
    var data = {
        id: note_id,
        title: note_title,
        body: note_content,
        csrfmiddlewaretoken: $.cookie('csrftoken')
    };

    $.post("/notes/editnote/", data).success(function (data) {
        //$('[data-noteid=' + note_id + ']>p>small').empty().append(data.preview);
        $('[data-noteid=' + note_id + ']').replaceWith(data);
    });
}

function getNote(thisRef) {
    var note_id = thisRef.attr("data-noteid");
    $.getJSON('/notes/note/', {note_id: note_id}, function (data) {
        $('.note-info').attr('id', note_id);
        $('.title').html(data.title);
        $('.editor').html(data.body);
    })
}

function validateURL(textval) {
    var urlregex = new RegExp("^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");
    return urlregex.test(textval);
}

// inserts a new empty note
function addNote() {
    var csrftoken = $.cookie('csrftoken');
    var folder_id = 1;
    var url = window.location.pathname.split('/')[3];
    var data = {
        title: "New Note",
        body: "",
        folder_id: folder_id,
        folder_name: url,
        csrfmiddlewaretoken: $.cookie('csrftoken')
    };

    $.post("/notes/addnote/", data).success(function (data) {
        $('.list-group').prepend(data);
        $('.note:first').on("click", function () {
            getNote($(this))
        });
    });
}

$(document).ready(function () {
    // retrieve a note once clicked on a list
    $('.note').click(function () {
        getNote($(this));
    });

    $('.note:first').click();

    // this creates a note as a new instance
    $('#new').click(function () {
        var csrftoken = $.cookie('csrftoken');
        //TODO get correct folder id
        var folder_id = 1;
        var url = window.location.pathname.split('/')[3];

        var data = {
            title: "New Note",
            body: " ",
            folder_id: folder_id,
            folder_name: url,
            csrfmiddlewaretoken: $.cookie('csrftoken')
        };

        $.post("/notes/addnote/", data).success(function (data) {
            $('.list-group').prepend(data);
            $('.note:first').on("click", function () {
                getNote($(this))
            });
            console.log($('.note:first'));
        });

    });


    //delete an existing note
    $('.delete').click(function () {
        var note_id = $('.note-info').attr('id');
        var note_title = $('.title').html();
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
                $('.note').click(function () {
                    getNote($(this));
                });

                $('.note:first').click();
//                $('.editor').empty().append("<h1 class='text-center'>No note selected<h1>");
            }
        });
    });

    $('#save').click(function () {
        saveChanges()
    });
});

