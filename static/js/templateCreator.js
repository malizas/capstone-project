'use strict';

// whatever pc the user chooses will show up in the creator-container (left side of column)
const addPCToContainer = (data) => {
    $('#picked').append(
        `<img src="${data}" style="height:140px;width:auto;" />`)
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

// save feature; takes the pcs that are checked and puts it into an array
$('#save_template').on('click', function(evt) {
    evt.preventDefault();
    const searchId = $('input[type="checkbox"]:checked').map(function() {
        return $(this).attr('id')
    }).get();

    const pc_ids = searchId.map(s => s.slice(2))

    const form_data = {
        pc_key: pc_ids
    }

    $.post('/save_template', form_data, res => {
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