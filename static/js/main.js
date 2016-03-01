$(document).ready( function() {
    console.log( "ready!" );

    $(".btnAgregar").on("click", function(e){
        var a = $( "#form_project" ).serializeArray();
        console.log(a);
        for(i in a){
            var elementValue = a[i]["value"];
            var elementName = a[i]["name"];

            if(elementValue.length == 0) {

                if(elementName == "domain") {
                    alert("El dominio es requerido!");
                    e.preventDefault();
                }

                if(elementName == "url") {
                    alert("La URL es requerida!");
                    e.preventDefault();
                }
            }
        }
        alert("Se agrego correctamente!")
    });


    var dateInitial = $('#datepicker');
    dateInitial.attr('autocomplete','off');
    dateInitial.datepicker({
            dateFormat: 'yy-mm-dd',
            changeMonth: true,
            changeYear: true,
            yearRange: "-20:+0"
    });


});