$(document).ready( function() {
    console.log( "ready!" );

    //-------boton "AgregarProyecto" de Proyectos---------//
    $(".btnAgregar").on("click", function(e){
        var a = $( "#form_project" ).serializeArray();
        console.log(a);
        for(i in a){
            var elementValue = a[i]["value"];
            var elementName = a[i]["name"];
            if(elementValue.length == 0) {
                if(elementName == "due_date") {
                    alert("La fecha de entrega es requerida!");
                    e.preventDefault();
                }
                if(elementName == "url") {
                    alert("La URL es requerida!");
                    e.preventDefault();
                }
            }
        }
    });
    //-------boton "AgregarProyecto" de Proyectos---------//
    //$(".btnAgregar").on("click", function(e){
    //    var a = $( "#form_project" ).serializeArray();
    //    console.log(a);
    //    for(i in a){
    //        var elementValue = a[i]["value"];
    //        var elementName = a[i]["name"];
    //
    //        if(elementValue.length == 0) {
    //
    //            if(elementName == "due_date") {
    //                alert("La fecha de entrega es requerida!");
    //                e.preventDefault();
    //            }
    //
    //            if(elementName == "url") {
    //                alert("La URL es requerida!");
    //                e.preventDefault();
    //            }
    //        }
    //    }
    //
    //});

    //-------formato de fecha ---------//
    var dateInitial = $('#datepicker');
    dateInitial.attr('autocomplete','off');
    dateInitial.datepicker({
            dateFormat: 'yy-mm-dd',
            changeMonth: true,
            changeYear: true,
            yearRange: "-20:+0"
    });


});