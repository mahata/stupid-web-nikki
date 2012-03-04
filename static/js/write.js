$(function() {
    $('#article').keyup(function(event) {
        $.post('/api', {article: $(this).val()}, function(data) {
            $('#preview').html(data);
        });
    });

    $.post('/api', {article: $('#article').val()}, function(data) {
        $('#preview').html(data);
    });
});
