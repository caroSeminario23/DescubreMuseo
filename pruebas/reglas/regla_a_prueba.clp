; FUNCIONA CORRECTAMENTE
(defrule rg_nueva4
    (museo 
        (id_museo ?id_museo) 
        (distrito ?distrito)
        (reserva_entrada ?reserva_entrada) 
        (servicio_guiado ?servicio_guiado) 
        (servicio_biblioteca ?servicio_biblioteca) 
        (venta_objetos ?venta_objetos) 
        (accesibilidad ?accesibilidad) 
        (permiso_foto ?permiso_foto) 
        (estacionamiento ?estacionamiento) 
        (visita_virtual ?visita_virtual)
        (sitio_web ?sitio_web)
        (categoria $?categorias)
        (dia_atencion $?dias_atencion)
    )
    
    (preferencias_usuario 
        (distrito_especificado ?distrito_especificado) 
        (dia_especificado ?dia_especificado)
        (categoria_especificada ?categoria_especificada)
        (reserva_usuario ?reserva_usuario)
        (estacionamiento_usuario ?estacionamiento_usuario)
        (venta_objetos_usuario ?venta_objetos_usuario)
        (permiso_foto_usuario ?permiso_foto_usuario)
        (accesibilidad_usuario ?accesibilidad_usuario)
        (servicio_guiado_usuario ?servicio_guiado_usuario)
        (visita_virtual_usuario ?visita_virtual_usuario)
        (servicio_biblioteca_usuario ?servicio_biblioteca_usuario)
        (sitio_web_existe ?sitio_web_existe)
    )      

    ;Si el distrito del museo es igual al distrito especificado por el usuario
    ;y la reserva del museo es igual a la reserva especificada por el usuario
    ;y el servicio guiado del museo es igual al servicio guiado especificado por el usuario
    ;y el servicio de biblioteca del museo es igual al servicio de biblioteca especificado por el usuario
    ;y la venta de objetos del museo es igual a la venta de objetos especificada por el usuario
    ;y la accesibilidad del museo es igual a la accesibilidad especificada por el usuario
    ;y el permiso de foto del museo es igual al permiso de foto especificado por el usuario
    ;y el estacionamiento del museo es igual al estacionamiento especificado por el usuario
    ;y la visita virtual del museo es igual a la visita virtual especificada por el usuario
    ;y el sitio web del museo es igual al sitio web especificado por el usuario
    (test(eq ?distrito ?distrito_especificado))
    (test(eq ?reserva_entrada ?reserva_usuario))
    (test(eq ?servicio_guiado ?servicio_guiado_usuario))
    (test(eq ?servicio_biblioteca ?servicio_biblioteca_usuario))
    (test(eq ?venta_objetos ?venta_objetos_usuario))
    (test(eq ?accesibilidad ?accesibilidad_usuario))
    (test(eq ?permiso_foto ?permiso_foto_usuario))
    (test(eq ?estacionamiento ?estacionamiento_usuario))
    (test(eq ?visita_virtual ?visita_virtual_usuario))
    (test(eq ?sitio_web ?sitio_web_existe))
    (test(member$ ?categoria_especificada ?categorias))
    (test(member$ ?dia_especificado ?dias_atencion))

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)