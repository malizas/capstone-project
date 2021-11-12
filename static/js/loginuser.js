// when clicked, will bring up the log in
$('#register').on('click', function() {
    $('#log_user').hide();
    $('#register_user').show();
    $('#register').hide();
    $('#log').show();
})

$('#log').on('click', function() {
    $('#log_user').show();
    $('#register_user').hide();
    $('#register').show();
    $('#log').hide();
})