
$(document).ready(function() {
    $('form').submit(function(event) {
        var date = new Date($('input[name="date"]').val());

        if (date < new Date()) {
            event.preventDefault();
            alert("Reservation date must be in the future.");
        }
    
    });
});