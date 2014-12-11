$(function() {
    var q = $('#q').attr('value');
    $.each($('.search-results'), function() {
        var $this = $(this);
        $this.html($this.text().replace(new RegExp(q, 'ig'), '<strong>' + q + '</strong>'));
    });
});
