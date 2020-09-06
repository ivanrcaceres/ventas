$(document).ready(function () {
    console.log('hola desde change_list1');
    $('#reporteventa_form > div > div.submit-row').hide();
    calculartotal()
});
console.log('hola desde reportechangelis');

function calculartotal() {

    console.log('calcular total');
    totaldetotales = 0;
    var $cantidaddeproducto = $('#reportedetalleventa_set-group > div > fieldset > table > tbody').children('tr').length;
    if($cantidaddeproducto-2 > 0){
        for(i = 0; i<$cantidaddeproducto-2;i++){

            a1 = '#id_reportedetalleventa_set-'+i+'-subtotal';
            // console.log($(a1).val());
            // console.log('$(a1).val()');
            // console.log( '');

            totaldetotales = totaldetotales + parseInt( $(a1).val() );
            // parseInt(sacaseparadordemil($(preciouni).val()))
            // console.log(totaldetotales);
        }
        // console.log('totaldetotales: ');
        // console.log(totaldetotales);
    }
    // totaldetotales = totaldetotales + parseInt($('#id_arancelmaa').val());
    // totaldetotales = totaldetotales + parseInt($('#id_deudamontoquevaabonar').val());


    $('#Total').val(numberFormat(String(totaldetotales)));
}

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