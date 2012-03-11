$(function() {
    $('#text').keyup(function(event) {
        $.post('/api', {article: $(this).val()}, function(data) {
            $('#article').html(data);
        });
    });

    $.post('/api', {article: $('#text').val()}, function(data) {
        $('#article').html(data);
    });
});
