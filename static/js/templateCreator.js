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