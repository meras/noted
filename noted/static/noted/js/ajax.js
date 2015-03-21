/**
 * Created by meras on 15-03-18.
 */


$(document).ready(function() {
    $('.note').click(function(){
        var note_id = $(this).attr("data-noteid");
        //$('.main').empty().append(note_id);
        $.get('/notes/note_body/', {note_id: note_id}, function(data){
            $('.main').html(data);
        });
    });
});