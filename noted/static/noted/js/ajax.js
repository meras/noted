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

    $('.note').click(function(){
        var note_id = $(this).attr("data-noteid");

        $.getJSON('/notes/note/', {note_id: note_id}, function(data){
            $('.note-info').html(data.title);
            $('.editor').html(data.body);
        });
    });
});