console.log('hola');

$('#repor2').click(function () {
    // console.log('holaaaaa');

    // location.href ="http://localhost:8000/pdfresumen/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2;

    // var $cliente01 = $('#select2-id_cliente-container').val();
    var $cliente01 = $('#select2-id_cliente-container').text();
    // var $fecha2 = $('#id_hasta').val();
    // console.log($cliente01);
    // console.log($cliente01);

    var $user01 = $('#select2-id_user-container').text();
    // console.log($user01);

    var $desde01 = $('#id_desde').val();
    // console.log($desde01);

    var $hasta01 = $('#id_hasta').val();
    // console.log($hasta01);

    $cliente02 = $cliente01.split(" Nro. Doc.: ");
    // console.log($cliente02);

    // cliente
    console.log('cliente:');
    $cliente03 = $cliente02[1];
    console.log($cliente03);
    cliente04 = String($cliente03);

    vectorid = [$cliente02[1]];
    // vectorid.append(cliente04);

    console.log('antes del ajax');
    // $.ajax({
    //     type: 'GET',
    //     data: {'valor': JSON.stringify(vectorid)},
    //     contextType: "application/json;charset=utf-8",
    //     dateType: "json",
    //     url: '/datodelcliente/',
    //     success: function (response) {
    //         console.log('dentro del ajax');
    //         console.log('response.vector[0]');
    //         console.log(response.vector[0]);
    //         cliente04 = response.vector[0];
    //         console.log('dentro del ajax');
    //     }
    // });
    console.log('despues del ajax');

    // user
    $user02 = $user01.substring(1);
    // console.log($user02);
    user03 = $user02;

    // aqui kilombo para sacar la fechas

    var $fecha1 = $('#id_desde').val();
    var $fecha2 = $('#id_hasta').val();
    // console.log($fecha1);
    // console.log($fecha2);
    vectorfecha = [$fecha1,$fecha1];
    // console.log(vectorfecha);

    dia1 = $fecha1[0];
    dia2 = $fecha1[1];

    diafull1 = parseInt(String(dia1)+String(dia2));

    // console.log(diafull1);

    mes1 = $fecha1[3];
    mes2 = $fecha1[4];

    mesfull1 = parseInt(String(mes1)+String(mes2));


    // console.log(mesfull1);
    ano1 = $fecha1[6];
    ano2 = $fecha1[7];
    ano3 = $fecha1[8];
    ano4 = $fecha1[9];


    anofull1 = parseInt( String(ano1)+String(ano2)+String(ano3)+String(ano4) );
// console.log(anofull1);

    dia12 = $fecha2[0];
    dia22 = $fecha2[1];

    diafull2 = parseInt(String(dia12)+String(dia22));

    // console.log(diafull2);

    mes12 = $fecha2[3];
    mes22 = $fecha2[4];

    mesfull2 = parseInt(String(mes12)+String(mes22));


    // console.log(mesfull2);
    ano12 = $fecha2[6];
    ano22 = $fecha2[7];
    ano32 = $fecha2[8];
    ano42 = $fecha2[9];

    anofull2 = parseInt( String(ano12)+String(ano22)+String(ano32)+String(ano42) );

    // console.log('anofull2');
    // console.log(anofull2);

    if( String(anofull2) == String(NaN)){

        console.log('es error');
        anofull2 = 0;
        console.log(anofull2);

    }
    if( String(mesfull2) == String(NaN)){

        console.log('es error');
        mesfull2 = 0;
        console.log(mesfull2);

    }
    if( String(diafull2) == String(NaN)){

        console.log('es error');
        diafull2 = 0;
        console.log(diafull2);

    }
    if( String(anofull1) == String(NaN)){

        console.log('es error');
        anofull1 = 0;
        console.log(anofull1);

    }
    if( String(mesfull1) == String(NaN)){

        console.log('es error');
        mesfull1 = 0;
        console.log(mesfull1);

    }
    if( String(diafull1) == String(NaN)){

        console.log('es error');
        diafull1 = 0;
        console.log(diafull1);

    }

    // LOS DATOS
    $eliminados = $('#id_eliminado').val();
    console.log('eliminados: ');
    console.log($eliminados);
    elimina2 = $eliminados;

    if(String($cliente02)=='undefined' || String($cliente02)=='NaN' || String($cliente02)== '' ){
        cliente04 = 'nadita';
        console.log('entro en el if choto');
    }
    console.log('cliente04');
    console.log(cliente04);

    // user03 = $user02;
    console.log('user02');
    console.log($user02);
    console.log('user03');
    console.log(user03);
    if(user03==''){
        user03='nadita';
    }
    console.log('user03');
    console.log(user03);
    console.log('DATOS');
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('anofull1');
    console.log(anofull1);
    console.log('diafull2');
    console.log(diafull2);
    console.log('mesfull2');
    console.log(mesfull2);
    console.log('anofull2');
    console.log(anofull2);
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('user03');
    console.log(user03);

    // cliente04 = cliente04.replace('-','');
    console.log('cliente04');
    console.log(cliente04);
    console.log('elimina2');
    console.log(elimina2);



// para desarrollo
// location.href ="http://localhost:8000/ventasreportes01/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
// para produccion
// location.href ="http://localhost/ventasreportes01/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;

    uurrll = [];
    var URLactual = window.location;
    uurrll = String(URLactual).split('admin');
    console.log(uurrll[0]+"ventasreportes01/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2);
    // http://localhost/admin/reporte/reporteventa/
    // http://localhost:8000/admin/reporte/reporteventa/


    // para desarrollo
    //location.href ="http://localhost:8000/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // para produccion
    // location.href ="http://localhost/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // PARA PRUEBA
    location.href = uurrll[0]+"ventasreportes01/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // http://localhost:8000/


});




$('#repor3').click(function () {
    // console.log('holaaaaa');

    // location.href ="http://localhost:8000/pdfresumen/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2;

    // var $cliente01 = $('#select2-id_cliente-container').val();
    var $cliente01 = $('#select2-id_cliente-container').text();
    // var $fecha2 = $('#id_hasta').val();
    // console.log($cliente01);
    // console.log($cliente01);

    var $user01 = $('#select2-id_user-container').text();
    // console.log($user01);

    var $desde01 = $('#id_desde').val();
    // console.log($desde01);

    var $hasta01 = $('#id_hasta').val();
    // console.log($hasta01);

    $cliente02 = $cliente01.split(" Nro. Doc.: ");
    // console.log($cliente02);

    // cliente
    console.log('cliente:');
    $cliente03 = $cliente02[1];
    console.log($cliente03);
    cliente04 = String($cliente03);

    vectorid = [$cliente02[1]];
    // vectorid.append(cliente04);

    console.log('antes del ajax');
    // $.ajax({
    //     type: 'GET',
    //     data: {'valor': JSON.stringify(vectorid)},
    //     contextType: "application/json;charset=utf-8",
    //     dateType: "json",
    //     url: '/datodelcliente/',
    //     success: function (response) {
    //         console.log('dentro del ajax');
    //         console.log('response.vector[0]');
    //         console.log(response.vector[0]);
    //         cliente04 = response.vector[0];
    //         console.log('dentro del ajax');
    //     }
    // });
    console.log('despues del ajax');

    // user
    $user02 = $user01.substring(1);
    // console.log($user02);
    user03 = $user02;

    // aqui kilombo para sacar la fechas

    var $fecha1 = $('#id_desde').val();
    var $fecha2 = $('#id_hasta').val();
    // console.log($fecha1);
    // console.log($fecha2);
    vectorfecha = [$fecha1,$fecha1];
    // console.log(vectorfecha);

    dia1 = $fecha1[0];
    dia2 = $fecha1[1];

    diafull1 = parseInt(String(dia1)+String(dia2));

    // console.log(diafull1);

    mes1 = $fecha1[3];
    mes2 = $fecha1[4];

    mesfull1 = parseInt(String(mes1)+String(mes2));


    // console.log(mesfull1);
    ano1 = $fecha1[6];
    ano2 = $fecha1[7];
    ano3 = $fecha1[8];
    ano4 = $fecha1[9];


    anofull1 = parseInt( String(ano1)+String(ano2)+String(ano3)+String(ano4) );
// console.log(anofull1);

    dia12 = $fecha2[0];
    dia22 = $fecha2[1];

    diafull2 = parseInt(String(dia12)+String(dia22));

    // console.log(diafull2);

    mes12 = $fecha2[3];
    mes22 = $fecha2[4];

    mesfull2 = parseInt(String(mes12)+String(mes22));


    // console.log(mesfull2);
    ano12 = $fecha2[6];
    ano22 = $fecha2[7];
    ano32 = $fecha2[8];
    ano42 = $fecha2[9];

    anofull2 = parseInt( String(ano12)+String(ano22)+String(ano32)+String(ano42) );

    // console.log('anofull2');
    // console.log(anofull2);

    if( String(anofull2) == String(NaN)){

        console.log('es error');
        anofull2 = 0;
        console.log(anofull2);

    }
    if( String(mesfull2) == String(NaN)){

        console.log('es error');
        mesfull2 = 0;
        console.log(mesfull2);

    }
    if( String(diafull2) == String(NaN)){

        console.log('es error');
        diafull2 = 0;
        console.log(diafull2);

    }
    if( String(anofull1) == String(NaN)){

        console.log('es error');
        anofull1 = 0;
        console.log(anofull1);

    }
    if( String(mesfull1) == String(NaN)){

        console.log('es error');
        mesfull1 = 0;
        console.log(mesfull1);

    }
    if( String(diafull1) == String(NaN)){

        console.log('es error');
        diafull1 = 0;
        console.log(diafull1);

    }

    // LOS DATOS
    $eliminados = $('#id_eliminado').val();
    console.log('eliminados: ');
    console.log($eliminados);
    elimina2 = $eliminados;

    if(String($cliente02)=='undefined' || String($cliente02)=='NaN' || String($cliente02)== '' ){
        cliente04 = 'nadita';
        console.log('entro en el if choto');
    }
    console.log('cliente04');
    console.log(cliente04);

    // user03 = $user02;
    console.log('user02');
    console.log($user02);
    console.log('user03');
    console.log(user03);
    if(user03==''){
        user03='nadita';
    }
    console.log('user03');
    console.log(user03);
    console.log('DATOS');
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('anofull1');
    console.log(anofull1);
    console.log('diafull2');
    console.log(diafull2);
    console.log('mesfull2');
    console.log(mesfull2);
    console.log('anofull2');
    console.log(anofull2);
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('user03');
    console.log(user03);

    // cliente04 = cliente04.replace('-','');
    console.log('cliente04');
    console.log(cliente04);
    console.log('elimina2');
    console.log(elimina2);



// para desarrollo
// location.href ="http://localhost:8000/ventasreportes02/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
//para produccion
//     location.href ="http://localhost/ventasreportes02/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
//

    uurrll = [];
    var URLactual = window.location;
    uurrll = String(URLactual).split('admin');
    console.log(uurrll[0]+"ventasreportes02/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2);
    // http://localhost/admin/reporte/reporteventa/
    // http://localhost:8000/admin/reporte/reporteventa/


    // para desarrollo
    //location.href ="http://localhost:8000/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // para produccion
    // location.href ="http://localhost/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // PARA PRUEBA
    location.href = uurrll[0]+"ventasreportes02/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // http://localhost:8000/

});



$('#repor4').click(function () {
    // console.log('holaaaaa');

    // location.href ="http://localhost:8000/pdfresumen/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2;

    // var $cliente01 = $('#select2-id_cliente-container').val();
    var $cliente01 = $('#select2-id_cliente-container').text();
    // var $fecha2 = $('#id_hasta').val();
    // console.log($cliente01);
    // console.log($cliente01);

    var $user01 = $('#select2-id_user-container').text();
    // console.log($user01);

    var $desde01 = $('#id_desde').val();
    // console.log($desde01);

    var $hasta01 = $('#id_hasta').val();
    // console.log($hasta01);

    $cliente02 = $cliente01.split(" Nro. Doc.: ");
    // console.log($cliente02);

    // cliente
    console.log('cliente:');
    $cliente03 = $cliente02[1];
    console.log($cliente03);
    cliente04 = String($cliente03);

    vectorid = [$cliente02[1]];
    // vectorid.append(cliente04);

    console.log('antes del ajax');
    // $.ajax({
    //     type: 'GET',
    //     data: {'valor': JSON.stringify(vectorid)},
    //     contextType: "application/json;charset=utf-8",
    //     dateType: "json",
    //     url: '/datodelcliente/',
    //     success: function (response) {
    //         console.log('dentro del ajax');
    //         console.log('response.vector[0]');
    //         console.log(response.vector[0]);
    //         cliente04 = response.vector[0];
    //         console.log('dentro del ajax');
    //     }
    // });
    console.log('despues del ajax');

    // user
    $user02 = $user01.substring(1);
    // console.log($user02);
    user03 = $user02;

    // aqui kilombo para sacar la fechas

    var $fecha1 = $('#id_desde').val();
    var $fecha2 = $('#id_hasta').val();
    // console.log($fecha1);
    // console.log($fecha2);
    vectorfecha = [$fecha1,$fecha1];
    // console.log(vectorfecha);

    dia1 = $fecha1[0];
    dia2 = $fecha1[1];

    diafull1 = parseInt(String(dia1)+String(dia2));

    // console.log(diafull1);

    mes1 = $fecha1[3];
    mes2 = $fecha1[4];

    mesfull1 = parseInt(String(mes1)+String(mes2));


    // console.log(mesfull1);
    ano1 = $fecha1[6];
    ano2 = $fecha1[7];
    ano3 = $fecha1[8];
    ano4 = $fecha1[9];


    anofull1 = parseInt( String(ano1)+String(ano2)+String(ano3)+String(ano4) );
// console.log(anofull1);

    dia12 = $fecha2[0];
    dia22 = $fecha2[1];

    diafull2 = parseInt(String(dia12)+String(dia22));

    // console.log(diafull2);

    mes12 = $fecha2[3];
    mes22 = $fecha2[4];

    mesfull2 = parseInt(String(mes12)+String(mes22));


    // console.log(mesfull2);
    ano12 = $fecha2[6];
    ano22 = $fecha2[7];
    ano32 = $fecha2[8];
    ano42 = $fecha2[9];

    anofull2 = parseInt( String(ano12)+String(ano22)+String(ano32)+String(ano42) );

    // console.log('anofull2');
    // console.log(anofull2);

    if( String(anofull2) == String(NaN)){

        console.log('es error');
        anofull2 = 0;
        console.log(anofull2);

    }
    if( String(mesfull2) == String(NaN)){

        console.log('es error');
        mesfull2 = 0;
        console.log(mesfull2);

    }
    if( String(diafull2) == String(NaN)){

        console.log('es error');
        diafull2 = 0;
        console.log(diafull2);

    }
    if( String(anofull1) == String(NaN)){

        console.log('es error');
        anofull1 = 0;
        console.log(anofull1);

    }
    if( String(mesfull1) == String(NaN)){

        console.log('es error');
        mesfull1 = 0;
        console.log(mesfull1);

    }
    if( String(diafull1) == String(NaN)){

        console.log('es error');
        diafull1 = 0;
        console.log(diafull1);

    }

    // LOS DATOS
    $eliminados = $('#id_eliminado').val();
    console.log('eliminados: ');
    console.log($eliminados);
    elimina2 = $eliminados;

    if(String($cliente02)=='undefined' || String($cliente02)=='NaN' || String($cliente02)== '' ){
        cliente04 = 'nadita';
        console.log('entro en el if choto');
    }
    console.log('cliente04');
    console.log(cliente04);

    // user03 = $user02;
    console.log('user02');
    console.log($user02);
    console.log('user03');
    console.log(user03);
    if(user03==''){
        user03='nadita';
    }
    console.log('user03');
    console.log(user03);
    console.log('DATOS');
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('anofull1');
    console.log(anofull1);
    console.log('diafull2');
    console.log(diafull2);
    console.log('mesfull2');
    console.log(mesfull2);
    console.log('anofull2');
    console.log(anofull2);
    console.log('diafull1');
    console.log(diafull1);
    console.log('mesfull1');
    console.log(mesfull1);
    console.log('user03');
    console.log(user03);

    // cliente04 = cliente04.replace('-','');
    console.log('cliente04');
    console.log(cliente04);
    console.log('elimina2');
    console.log(elimina2);


    uurrll = [];
    var URLactual = window.location;
    uurrll = String(URLactual).split('admin');
    console.log(uurrll[0]+"ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2);
    // http://localhost/admin/reporte/reporteventa/
    // http://localhost:8000/admin/reporte/reporteventa/


    // para desarrollo
    //location.href ="http://localhost:8000/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // para produccion
    // location.href ="http://localhost/ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // PARA PRUEBA
    location.href = uurrll[0]+"ventasreportes03/"+diafull1+"/"+ mesfull1+"/"+anofull1+"/"+diafull2+"/"+mesfull2+"/"+anofull2+"/"+user03+"/"+cliente04+"/"+elimina2;
    // http://localhost:8000/

});