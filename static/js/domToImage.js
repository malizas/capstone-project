'use strict';

$('#save').on('click', function() {
    domtoimage.toBlob(document.getElementById('creator'))
    .then(function(blob) {
        window.saveAs(blob, "output.png")
    });

})

