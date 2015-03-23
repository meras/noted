/**
 * Created by meras on 15-03-18.
 */


$(document).ready(function() {
    //$('.note').click(function(){
    //    var note_id = $(this).attr("data-noteid");
    //    var test_data = "HALLO ECLIPSE GLARGOW"
    //
    //    $.get('/notes/note_body/', {note_id: note_id}, function(data){
    //        $('.editor').html(data);
    //    });
    //});

    //          Demonstating how to delete a post
    //
    //$.post("/notes/addnote/?id=9", {control: 'delete',
    //                       csrfmiddlewaretoken:$.cookie('csrftoken')
    //                      });

    // this saves a note as a new instance
    $('.btn-success').click(function(){
        var csrftoken = $.cookie('csrftoken');
        var note_title = $('.note-info > section').html();
        var note_content = $('.editor').html();
        var data = {
            label: note_title,
            body: note_content,
            csrfmiddlewaretoken:$.cookie('csrftoken')};

        $.post("/notes/addnote/", data);
    });

    //edit an existing note
    $('.btn-info').click(function(){
        var note_id = $('.note-info').attr('id');
        var csrftoken = $.cookie('csrftoken');
        var note_title = $('.note-info > section').html();
        var note_content = $('.editor').html();
        var data = {
            id: note_id,
            label: note_title,
            body: note_content,
            csrfmiddlewaretoken:$.cookie('csrftoken')};
        console.log(note_id);

        $.post("/notes/addnote/", data);
    });

    // retrieve a note once clicked on a list
    $('.note').click(function(){
        var note_id = $(this).attr("data-noteid");

        $.getJSON('/notes/note/', {note_id: note_id}, function(data){
            $('.note-info').attr('id', note_id);
            $('.note-info > section').html(data.title);
            $('.editor').html(data.body);
        });
    });
});