'use strict'

const jsonData = require('./photocards.json');

// whatever pc the user chooses will show up in the creator-container
const createDivsforPCs = jsonFile => {
    for (const data of jsonFile) {
        $('#creator-container').append(`<div class="pc_picked${data.pc_id}">${data.pc_img}</div>`);
    }
};

// takes whatever the pc the user picks from the list of pcs
const userPicked = (evt) => {
    evt.preventDefault;
    $('.all_photocards').attr('{{ card.photocard_id }}')
}  

(function customTemplate() {
    createDivsforPCs(jsonData);
    userPicked();

    $('#{{ card.photocard_id }}').on('click', evt => {
        const clickedPC = evt.target;

    })
})();