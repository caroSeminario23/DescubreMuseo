(defrule rg_nueva1
    (museo (id_museo ?id_museo) (distrito ?distrito))
    (preferencias_usuario (distrito_especificado ?distrito_especificado))

    ;Si el distrito del museo es igual al distrito especificado por el usuario
    (test(eq ?distrito ?distrito_especificado))

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)

(defrule rg_nueva2
    (museo (id_museo ?id_museo) (distrito ?distrito) (categoria ?categoria))
    (preferencias_usuario (distrito_especificado ?distrito_especificado) (categoria_especificada ?categoria_especificada))

    ;Si el distrito del museo es igual al distrito especificado por el usuario
    ;y la categoria del museo es igual a la categoria especificada por el usuario
    (test(eq ?distrito ?distrito_especificado))
    (test(eq ?categoria ?categoria_especificada))

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)

(defrule rg_nueva3
    (museo (id_museo ?id_museo) (distrito ?distrito) (categoria ?categoria) (dia_atencion ?dia_atencion))
    (preferencias_usuario (distrito_especificado ?distrito_especificado) (categoria_especificada ?categoria_especificada) (dia_especificado ?dia_especificado))

    ;Si el distrito del museo es igual al distrito especificado por el usuario
    ;y la categoria del museo es igual a la categoria especificada por el usuario
    ;y el dia especificado por el usuario está dentro de los dias de atencion del museo
    (test(eq ?distrito ?distrito_especificado))
    (test(eq ?categoria ?categoria_especificada))
    (test(eq ?dia_atencion $? ?dia_especificado $?))
    ;(test(member$ ?dia_especificado ?dia_atencion))

    =>
    (printout t "Dia especificado: " ?dia_especificado crlf)
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)

;Funciona textos sin comillas
(defrule rg_nueva3
    (museo (id_museo ?id_museo) (distrito ?distrito) (categoria ?categoria) (dia_atencion $?dias_atencion))
    (preferencias_usuario (distrito_especificado ?distrito_especificado) (categoria_especificada ?categoria_especificada) (dia_especificado ?dia_especificado))

    (test (eq ?distrito ?distrito_especificado))
    (test (eq ?categoria ?categoria_especificada))
    (test (member$ ?dia_especificado ?dias_atencion))

    =>
    (printout t "Dia especificado: " ?dia_especificado crlf)
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)



(defrule rg_nueva4
    (museo (id_museo ?id_museo) (distrito ?distrito)
    (reserva_entrada ?reserva_entrada) (servicio_guiado ?servicio_guiado) 
    (servicio_biblioteca ?servicio_biblioteca) (venta_objetos ?venta_objetos) 
    (accesibilidad ?accesibilidad) (permiso_foto ?permiso_foto) 
    (estacionamiento ?estacionamiento) (visita_virtual ?visita_virtual)
    (sitio_web ?sitio_web))
    
    (preferencias_usuario (distrito_especificado ?distrito_especificado) 
    (reserva_usuario ?reserva_usuario) (servicio_guiado_usuario ?servicio_guiado_usuario)
    (servicio_biblioteca_usuario ?servicio_biblioteca_usuario) 
    (venta_objetos_usuario ?venta_objetos_usuario)
    (accesibilidad_usuario ?accesibilidad_usuario)
    (permiso_foto_usuario ?permiso_foto_usuario)
    (estacionamiento_usuario ?estacionamiento_usuario)
    (visita_virtual_usuario ?visita_virtual_usuario) (sitio_web_existe ?sitio_web_existe))
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

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)


//Ejemplo claude
; Definición de un template con un multislot de días
(deftemplate horario
   (multislot dias-atencion))

; Hecho de ejemplo
(deffacts datos-iniciales
   (horario (dias-atencion "Lunes" "Martes" "Miércoles"))
   (dia-buscar "Martes"))

; Regla que falla al usar member$
(defrule buscar-dia-incorrecto
   (horario (dias-atencion $?dias))
   (dia-buscar ?dia)
   (test (member$ ?dia ?dias))
   =>
   (printout t "Día " ?dia " encontrado (pero esta regla no se activará)." crlf))

; Regla que funciona correctamente
(defrule buscar-dia-correcto
   (horario (dias-atencion $?dias))
   (dia-buscar ?dia)
   (test (member$ (sym-cat ?dia) ?dias))
   =>
   (printout t "Día " ?dia " encontrado correctamente." crlf))

; Función para ejecutar el ejemplo
(deffunction ejecutar-ejemplo ()
   (reset)
   (run)
   (facts))