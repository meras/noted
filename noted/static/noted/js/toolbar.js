// WYSIWYG for the title, content and tags
var editor = new MediumEditor('.editor', {
        buttons: ['bold', 'italic', 'header1', 'header2', 'anchor', 'unorderedlist', 'orderedlist'],
        cleanPastedHTML: false
    }),
    title = new MediumEditor('.title', {
        placeholder: 'Untitled note...',
        disableToolbar: true,
        disableReturn: true
    }),
    tags = new MediumEditor('.tags', {
        placeholder: 'Click to add tags...',
        disableToolbar: true,
        disableReturn: true
    });

// Full screen mode
$(function () {
    $(".resize").click(function () {
        $(".test").toggle(1000);
        $(".topnav").slideToggle(1400);
        $('note-info').css({
            'height': '100%',
            'width': '100%'
        });
    });
    $('.font').click(function () {
        $('.note-content').css({
            'background-color': '#554F48',
            'color': '#FFFFFF'
        });
    });
});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});