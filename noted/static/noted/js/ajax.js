/*global $:false, jQuery:false, document:false */
$(document).ready(function () {
    $.embedly.defaults.key = 'a8e0caf281894a17ac457ee551d96a74';
    /*
     * Helper functions
     */

    /* Create a new note instance*/
    function newNote() {
        var csrftoken = $.cookie('csrftoken'),
            folder_id = $('.folder-list>.active>a').attr("data-folderid"),
            data = {
                title: "Untitled note",
                body: "<br>",
                folder_id: folder_id,
                csrfmiddlewaretoken: csrftoken
            };
        $.post("/notes/addnote/", data, function (data) {
            $('#notelist').children().prepend(data).children().first().trigger('click');
            $('#title').empty();
        });
    }

    /* Edit an existing note*/
    function saveChanges() {
        var note_id = $('.note-info').attr('id'),
            csrftoken = $.cookie('csrftoken'),
            title = $('#title').text(),
            note_title = title === "" ? "Untitled note" : title,
            note_content = $('.editor').html(),
            data = {
                id: note_id,
                title: note_title,
                body: note_content,
                csrfmiddlewaretoken: csrftoken
            };

        $.post("/notes/editnote/", data).success(function (data) {
            var note = $('#notelist').find('a[data-noteid=' + note_id + ']');
            $(note).find('strong').html(data.title);
            $(note).find('.preview').html(data.preview);
        });
    }

    /* Retrieve note content as JSON*/
    function getNote(thisRef) {
        var note_id = thisRef.attr("data-noteid");
        $.getJSON('/notes/note/', {note_id: note_id}, function (data) {
            $('.note-info').attr('id', note_id);
            if (data.title === "Untitled note") {
                $('#title').empty();
            } else {
                $('#title').html(data.title);
            }
            $('.editor').html(data.body);
        });
    }

    /* Retrieve a list of notes that belong to a folder */
    function getNoteList(thisRef) {
        var folder_id = thisRef.attr("data-folderid");
        $.get('/notes/fold/', {folder_id: folder_id}, function (data) {
            $('#notelist').children().empty().html(data);
        });
    }

    function validateURL(textval) {
        //noinspection JSLint
        var urlregex = new RegExp("^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");
        return urlregex.test(textval);
    }

    /*
     * Event bindings
     */

    /* retrieve a list of notes that belong to a folder */
    $('.folder').on('click', function () {
        getNoteList($(this));
        $('.folder-list>.active').removeClass('active');
        $(this).parent().addClass('active');
    });

    // retrieve a note once clicked on a list
    $('#notelist').on('click', '.note', function () {
        getNote($(this));
        $('#notelist').find('.active').removeClass('active');
        $(this).addClass('active');
    });

    // this creates a note as a new instance
    $('#new').on('click', function () {
        newNote();
    });


    //delete an existing note
    $('#delete').on('click', function () {
        var note_id = $('.note-info').attr('id'),
            csrftoken = $.cookie('csrftoken'),
            data = {
                id: note_id,
                control: 'delete',
                csrfmiddlewaretoken: csrftoken
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
        /*
         * Replaces pasted url's with an href and tries to embed it
         */
        paste: function (event) {
            var pastedText = event.originalEvent.clipboardData.getData('text/plain'),
                newLink = $('<a href="' + pastedText + '">' + pastedText + '</a>');
            if (validateURL(pastedText)) {
                $('.editor p:contains(' + pastedText + ')').replaceWith(newLink);
                newLink.embedly({
                    query: {
                        maxwidth: 500
                    }
                });
            }
        },
        input: function () {
            var text = $('.editor').text();
            var wordCount = text.trim().split(' ').length;

            $('#count').html(wordCount);
        }
    }).focus();
});

$(document).ajaxComplete(function () {
    $('.editor').focus();
});
