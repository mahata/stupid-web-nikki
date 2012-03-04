$(function() {
    $('#article').keyup(function(event) {
        $.post('/api', {article: $(this).val()}, function(data) {
            $('#preview').html(data);
        });
    });
});
