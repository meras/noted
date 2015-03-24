/**
 * Created by meras on 15-03-18.
 */


$(document).ready(function () {
    // this saves a note as a new instance
    $('.btn-success').click(function () {
        var csrftoken = $.cookie('csrftoken');
        var note_content = $('.editor').html();
        var data = {
            title: "New note",
            body: note_content,
            csrfmiddlewaretoken: $.cookie('csrftoken')
        };

        $.post("/notes/addnote/", data).success(function (data) {
            $('.list-group').prepend(data)
        });

    });

    //edit an existing note
    $('.btn-info').click(function () {
        var note_id = $('.note-info').attr('id');
        var csrftoken = $.cookie('csrftoken');
        var note_title = $('.note-info > section').html();
        var note_content = $('.editor').html();
        var data = {
            id: note_id,
            title: note_title,
            body: note_content,
            csrfmiddlewaretoken: $.cookie('csrftoken')
        };

        $.post("/notes/editnote/", data).success(function (data) {
            $('[data-noteid=' + note_id + ']>p>small').empty().append(data.preview);
        });

    });

    //delete an existing note
    $('.btn-danger').click(function () {
        console.log("danger");
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
                $('[data-noteid=' + note_id + ']').empty().append("DELETED");
            }
        });
    });


    // retrieve a note once clicked on a list
    $('.note').click(function () {
        var note_id = $(this).attr("data-noteid");

        $.getJSON('/notes/note/', {note_id: note_id}, function (data) {
            $('.note-info').attr('id', note_id);
            $('.note-info > section').html(data.title);
            $('.editor').html(data.body);
        });
    });
});