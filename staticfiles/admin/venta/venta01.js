$(document).ready(function () {
    calculartotal();
    $('select').change(function(){
        console.log('op holaaa');
        cuandosecambiaproducto();
        console.log('op holaaa2');
    });
    console.log('op holaaa3');
});

function cuandosecambiaproducto() {

    console.log('primera funcion');
    var $cantidaddeproducto = $('#detalleventa_set-group > div > fieldset > table > tbody').children('tr').length;

    // aqui en vectornombre cargo los id de los elementos del detalle producto
    vectornombre = [];
    vectornombreid = [];
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        var nombredeproductoconid = '#select2-id_detalleventa_set-' + i + '-producto-container';
        vectornombre.push(nombredeproductoconid);
    }
    // aqui en vectornombreid cargo los nombres de los productos con su id
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        vectornombreid.push($(vectornombre[i]).text());
        // console.log($(vectornombre[i]).text());
    }

    // aqui en vectoridp pongo los id de los productos del detalle compra
    // uso vectoraux para cargar en vectoraux[0] el nombre y en vectoraux[1] la id del producto
    // y al final todas la ids de los productos tengo en vectoridp
    vectoridp = [];
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        vectoraux = [];
        if (vectornombreid[i] != '') {
            vectoraux = vectornombreid[i].split(', cod: ');
            console.log('vectoraux[1]' + vectoraux[1]);
            vectoridp.push(vectoraux[1]);
        }
    }

    // aqui pone en blanco las cajas de precio unitarios y la cajas de cantidad de productos
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        var cajapreciounitario = '#id_detalleventa_set-' + i + '-preciounitario';
        $(cajapreciounitario).val('');
    }

    // aqui pon el vector posiciones pongo los numeros de linea de los productos
    posiciones = [];
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        if (vectornombreid[i] != '') {
            posiciones.push(i);
        }
    }

    console.log(posiciones);
    console.log(posiciones.length);

    console.log('Ivan1+++++++++++++++++++++++++++++++++++++++++++++++++++');
    for (var i = 0; i < $cantidaddeproducto - 2; i++) {
        console.log('vectoraux[i]');
        console.log(vectoridp[i]);
        console.log(vectoridp[i].length);
    }
    console.log('Ivan2+++++++++++++++++++++++++++++++++++++++++++++++++++');
    if(posiciones.length != 0){
        $.ajax({
            type: 'GET',
            data: {'valor':JSON.stringify(vectoridp)},
            contextType: "application/json;charset=utf-8",
            dateType: "json",
            url: '/productosajax/',
            success: function (response){

                console.log(response.vector[0]);
                console.log(response.vector[1]);
                console.log(response.vector[2]);


                // #id_detalleventa_set-0-preciounitario
                var cajapreciounitario;
                for(var i=0;i <= vectoridp.length;i++) {
                    var cajapreciounitario = '#id_detalleventa_set-'+posiciones[i]+'-preciounitario';
                    $(cajapreciounitario).val('');
                }
                for(var i=0;i < vectoridp.length;i++) {
                    var cajapreciounitario = '#id_detalleventa_set-'+posiciones[i]+'-preciounitario';
                    $(cajapreciounitario).val(String(response.vector[i]));
                }

                calcularsubtotales();
                calculartotal();


            }
        });
        console.log("FIN FOR Y AJAX");
    }
}
// aqui al pones las cantidades de los productos, calcula los subtotales
function calcularsubtotales() {
    console.log('hola subtotales');
    var $cantidaddeproducto = $('#detalleventa_set-group > div > fieldset > table > tbody').children('tr').length;
    console.log('cantidaddeproducto + 2: '+$cantidaddeproducto);
    for (var i=0 ; i<$cantidaddeproducto-2 ; i++){
        var preciouni = '#id_detalleventa_set-'+i+'-preciounitario';
        var cantidad = '#id_detalleventa_set-'+i+'-cantidad';
        var subtotald = '#id_detalleventa_set-'+i+'-subtotal';
        var st = parseInt($(preciouni).val()) * parseInt($(cantidad).val());
        $(subtotald).val(String(st));

        // var ist = st *10/110;
        // console.log(ist);

        // var ivaf = '#id_detalleventa_set-'+i+'-subtotaliva';
        // $(ivaf).val(numberFormat(String(Math.round(ist.toFixed(2)))));




    }

}

$(document).keyup(function() {

    console.log('ppapapapapapa');
    calcularsubtotales();
    calculartotal();



});


$(document).click(function() {

    console.log('ppapapapapapa');
    calcularsubtotales();
    calculartotal();



});


function calculartotal() {
    console.log('calcular total');
    totaldetotales = 0;
    var $cantidaddeproducto = $('#detalleventa_set-group > div > fieldset > table > tbody').children('tr').length;
    if($cantidaddeproducto-2 > 0){
        for(i = 0; i<$cantidaddeproducto-2;i++){
            a1 = '#id_detalleventa_set-'+i+'-subtotal';
            console.log($(a1).val());
            console.log('$(a1).val()');
            console.log( '');

            totaldetotales = totaldetotales + parseInt( $(a1).val() );
            // parseInt(sacaseparadordemil($(preciouni).val()))
            console.log(totaldetotales);
        }
        console.log('totaldetotales: ');
        console.log(totaldetotales);
    }
    // totaldetotales = totaldetotales + parseInt($('#id_arancelmaa').val());
    // totaldetotales = totaldetotales + parseInt($('#id_deudamontoquevaabonar').val());


    $('#Total').val(numberFormat(String(totaldetotales)));
}



// pone punto serapadores de mil
function numberFormat(numero){
    // Variable que contendra el resultado final
    var resultado = "";

    // Si el numero empieza por el valor "-" (numero negativo)
    if(numero[0]=="-")
    {
        // Cogemos el numero eliminando los posibles puntos que tenga, y sin
        // el signo negativo
        nuevoNumero=numero.replace(/\./g,'').substring(1);
    }else{
        // Cogemos el numero eliminando los posibles puntos que tenga
        nuevoNumero=numero.replace(/\./g,'');
    }

    // Si tiene decimales, se los quitamos al numero
    if(numero.indexOf(",")>=0)
        nuevoNumero=nuevoNumero.substring(0,nuevoNumero.indexOf(","));

    // Ponemos un punto cada 3 caracteres
    for (var j, i = nuevoNumero.length - 1, j = 0; i >= 0; i--, j++)
        resultado = nuevoNumero.charAt(i) + ((j > 0) && (j % 3 == 0)? ".": "") + resultado;

    // Si tiene decimales, se lo añadimos al numero una vez forateado con
    // los separadores de miles
    if(numero.indexOf(",")>=0)
        resultado+=numero.substring(numero.indexOf(","));

    if(numero[0]=="-")
    {
        // Devolvemos el valor añadiendo al inicio el signo negativo
        return "-"+resultado;
    }else{
        return resultado;
    }
}

function sacaseparadordemil(numero) {

    var a = (String(numero)).replace('.','').replace('.','').replace('.','').replace('.','').replace('.','').replace('.','').replace('.','').replace('.','');
    // a = (String(numero)).replace('.','');
    // a = (String(numero)).replace('.','');
    // a = (String(numero)).replace('.','');

    return a;
}