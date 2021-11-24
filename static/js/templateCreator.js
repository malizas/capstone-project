'use strict';

// whatever pc the user chooses will show up in the creator-container (left side of column)
const addPCToContainer = (data) => {
    $('#picked').append(
        `<img src="${data}" id="${data} "style="height:140px;width:auto;" />`)
}

// removes the pc that is unchecked
const removePCFromContainer = (data) => {
    $(`#picked img[src="${data}"]`).remove()
}

// clears all pcs in the creator-container
$('#trash_all').on('click', function() {
    $('#picked').empty();
    $('input[type="checkbox"]').prop('checked', false);
})

// takes whatever the pc the user picks from the list of pcs given (right side of column)
// notes to self: this is what you call an event handler
$('input[type="checkbox"]').on('click', function() {
    if (this.checked) {
        addPCToContainer($(this).val());
    } else {
        removePCFromContainer($(this).val());
    };
})

//search function
$('#search').keyup(function(){
    const input = $(this).val().toLowerCase();
    $('#all_photocards li').filter(function(){
        $(this).toggle($(this).text().toLowerCase().indexOf(input) > -1);
    })
})
// save feature
$('#save_template').on('click', function(evt) {
    // select all the checked checboxes on the right side of the screen,
    // remember, we want the ids of the checked pcs not the value!
    // once we have that array, we make an ajax post request to send the array to the server side
    // the array should have the ids that are selected (aka the pcs in the template);
    // it should take the pcs in the array and do a comparison of the pc_picked table
    // conditionals: if a pc in the array is already in the pc_picked table, we don't do anything
    // if it's new and not in the pc_picked table, we add it
    // if it's not in the array and in the pc_picked table, we delete it

    evt.preventDefault();
    const searchId = $('input[type="checkbox"]:checked').map(function() {
        return $(this).attr('id')
    }).get();

    const pc_ids = searchId.map(s => s.slice(2));

    $.post('/save_template', pc_ids, res => {
        alert(res);
    });
})

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