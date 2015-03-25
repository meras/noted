/**
 * Created by mickeypash on 24/03/15.
 */
//function get_text(el) {
//    ret = "";
//    var length = el.childNodes.length;
//    for(var i = 0; i < length; i++) {
//        var node = el.childNodes[i];
//        if(node.nodeType != 8) {
//            ret += node.nodeType != 1 ? node.nodeValue : get_text(node);
//        }
//    }
//    return ret;
//}
//var words = get_text(document.getElementById('editor'));
//var count = words.split(' ').length;

function wordCount(val) {
    return {
        charactersNoSpaces: val.replace(/\s+/g, '').length,
        characters: val.length,
        words: val.match(/\S+/g).length,
        lines: val.split(/\r*\n/).length
    }
}

var count = $('#count');

$('.editor').on('input', function () {

    var c = wordCount(this.value);

    count.html(
            "Count: " + c.words);

});