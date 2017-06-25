$(document).ready(function() {
    $('ul.tabs').tabs();
});
$(document).ready(function() {
    $('ul.tabs').tabs('select_tab', 'tab_id');
});

$(document).ready(function() {
    $('select').material_select();
});

$('select').material_select('destroy');

$('.timepicker').pickatime({
    default: 'now', // Set default time
    fromnow: 0, // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function() {} //Function for after opening timepicker  
});

$(".home-line").on("change", function() {
  var line = $(this).val();
  console.log(line);
  var saveData = $.ajax({
    type: 'GET',
    url: "http://40.71.189.185:5001/station/" + line,
    dataType: "text",
    success: function(resultData) {
        var result = JSON.parse(resultData);
        console.log(result[0][1]);

        for (var i = 0; i < result.length; i++) {
            /*
            $(".stations").append($('<option>', {
                value: Object.keys(result[i][1])[0],
                text: result[i][0]
            }));
            */

            var o = new Option(result[i][0], Object.keys(result[i][1])[0]);
            /// jquerify the DOM object 'o' so we can use the html method
            $(o).html(result[i][0]);
            $("#stations").append(o);
            
            


            
        }
        $("#stations").material_select('update');
      }
    });
  });