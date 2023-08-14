
$(document).ready(function() {
    $('form').submit(function(event) {
        var date = new Date($('input[name="date"]').val());
        var time = $('input[name="time"]').val();
        var dayOfWeek = date.getDay();
        var openingTimeWeekdays = '16:00';
        var closingTimeWeekdays = '21:00';
        var openingTimeWeekends = '13:00';
        var closingTimeWeekends = '21:00';

        if (date < new Date()) {
            event.preventDefault();
            alert("Reservation date must be in the future.");
        }

        if (dayOfWeek >= 1 && dayOfWeek <= 4) {
            if (time < openingTimeWeekdays || time > closingTimeWeekdays) {
                alert("Reservation time must be within working hours.");
            }
        } else {
            if (time < openingTimeWeekends || time > closingTimeWeekends) {
                alert("Reservation time must be within working hours.");
            }
        }
    
    });
});