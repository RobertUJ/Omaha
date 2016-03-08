$(document).ready(function(){
    console.log("esta lista")

    $("#loginbtn").on("click", function(e){
        var a = $( "#loginform" ).serializeArray();
        console.log(a);
        //for(i in a){
        //    var elementValue = a[i]["value"];
        //    var elementName = a[i]["name"];
        //    if(elementValue.length == 0) {
        //        if(elementName == "username") {
        //            alert("La fecha de entrega es requerida!");
        //            e.preventDefault();
        //        }
        //        if(elementName == "url") {
        //            alert("La URL es requerida!");
        //            e.preventDefault();
        //        }
        //    }
        //}
    });

});