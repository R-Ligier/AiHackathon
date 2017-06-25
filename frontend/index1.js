$(document).ready(function(){
  $('ul.tabs').tabs();
});
$(document).ready(function(){
  $('ul.tabs').tabs('select_tab', 'tab_id');
});

$(document).ready(function() {
   $('select').material_select();
  });

$('select').material_select('destroy');

$('.timepicker').pickatime({
    default: 'now', // Set default time
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function(){} //Function for after opening timepicker  
  });
      