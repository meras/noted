    $('.editor').on('paste', function () {
        console.log(this)
    });

    function wordCount(el) {
        var count = el.innerHTML.split(' ').length;
        return count
    }

    var count = $('.word-count');

    $('.editor').on('input', function () {
        var c = wordCount(this);
        count.html(c + "words");
    });