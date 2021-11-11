'use strict';

// whatever pc the user chooses will show up in the creator-container (left side of column)
// need to somehow implement an if statement for whenever the user picks a pc
const addPCToContainer = (data) => {
    $('#creator').append(
        `<img src="${data}" style="height:140px;width=auto" />`)
}

// removes the pc that is unchecked
const removePCFromContainer = (data) => {
    $(`#creator img[src="${data}"]`).remove()
}

// takes whatever the pc the user picks from the list of pcs given (right side of column)
// this is an event handler
$('input[type="checkbox"]').on('click', function() {
    if (this.checked) {
        addPCToContainer($(this).val());
    } else {
        removePCFromContainer($(this).val());
    };
})