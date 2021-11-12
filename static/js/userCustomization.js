'use strict';

//change text of the title
$('#title_text').on('input', function() {
  $('#title').text($('#title_text').val());
})

//title font size
const slider = $('#title_size');
$('#value').html(slider.val());

slider.on('input', function() {
  $('#value').html(slider.val());
  $('#title').css('font-size', slider.val() + 'px');
})

//change title alignment
$('#left-align').on('click', function() {
  $('#title').css('text-align', 'left')
})

$('#center-align').on('click', function() {
  $('#title').css('text-align', 'center')
})

$('#right-align').on('click', function() {
  $('#title').css('text-align', 'right')
})

//change background color
$('#bg-color').change(function() {
  $('#creator').css('background', $(this).val())
})

//change font color
$('#font-color').change(function(){
  $('#title').css('color', $(this).val())
})