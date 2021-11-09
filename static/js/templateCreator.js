'use strict';

// const jsonData = require('./photocards.json')

// whatever pc the user chooses will show up in the creator-container
// need to somehow implement an if statement for whenever the user picks a pc
// so it's added to the creator-container (left side of column)
const addPCToContainer = (data) => {
    $('#creator-container').append(
        `<img src="${data}" style="height:180px;width=auto" />`)
}

// takes whatever the pc the user picks from the list of pcs given (right side of column)
$('input[type="checkbox"]').on('click', function(){
    let selection = [];
    $('input[type="checkbox"]:checked').each(function() {
        selection.push($(this).val());
    });
    addPCToContainer($(this).val());
    // if checked before then remove
    // $('#creator-container').html(selection)
});