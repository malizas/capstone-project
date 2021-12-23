'use strict';

//change text of the title
$('#title_text').on('input', function() {
  $('#title').text($('#title_text').val());
})

//change text of description
$('#desc_text').on('input', function() {
  $('#desc').text($('#desc_text').val());
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
  $('#title').css('text-align', 'left');
})

$('#center-align').on('click', function() {
  $('#title').css('text-align', 'center');
})

$('#right-align').on('click', function() {
  $('#title').css('text-align', 'right');
})

//change description alignment
$('#left-desc').on('click', function() {
  $('#desc').css('text-align', 'left');
})

$('#center-desc').on('click', function() {
  $('#desc').css('text-align', 'center');
})

$('#right-desc').on('click', function() {
  $('#desc').css('text-align', 'right');
})

//change background color
$('#bg-color').change(function() {
  $('#creator').css('background', $(this).val());
})

//change font color
$('#font-color').change(function(){
  $('#title').css('color', $(this).val());
  $('#desc').css("font-family", $(this).val());
})

//change fonts
$('#font-family').change(function () {
  $('#title').css("font-family", $(this).val());
  $('#desc').css("font-family", $(this).val());
});

//change image size
const img_slider = $('#pc_size');
$('#pc_value').html(img_slider.val());

img_slider.on('input', function() {
  $('#pc_value').html(img_slider.val());
  $('#picked img').css('height', img_slider.val() + 'px');
})