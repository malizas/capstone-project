'use strict';

// when clicked, will bring to_customize
$('#to_customize').on('click', function() {
    $('#photocards').hide();
    $('#customize').show();
    $('#to_customize').hide();
    $('#back').show();
})

// when clicked, will go back to all the photocards
$('#back').on('click', function() {
    $('#photocards').show();
    $('#customize').hide();
    $('#to_customize').show();
    $('#back').hide();
})

// change the color "dynamically" without a use of a button
