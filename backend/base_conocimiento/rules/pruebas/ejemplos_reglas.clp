-----------------------------------------------------

chat_regla general 3 - ¡¡¡Funciona NO TOCAR!!!

(defrule regla_general3
    ;; Definir el hecho de preferencias_usuario
    (preferencias_usuario 
        (distrito_especificado ?distrito_especificado)
        (dia_especificado ?dia1)
        (categoria_especificada ?categoria_especificada)
        (estacionamiento_usuario ?estacionamiento1)
        (venta_objetos_usuario ?venta_objetos1)
        (permiso_foto_usuario ?permiso_foto1) 
        (accesibilidad_usuario ?accesibilidad1)
        (servicio_guiado_usuario ?servicio_guiado1)
        (visita_virtual_usuario ?visita_virtual1)
        (servicio_biblioteca_usuario ?servicio_biblioteca1)
        (sitio_web_existe ?sitio_web1)
    )
    ;; Definir el hecho de museo
    (museo 
        (id_museo ?id_museo)
        (distrito ?distrito)
        (dia_atencion ?dia2)
        (dia_concurrido ?dia)
        (categoria ?categoria)
        (estacionamiento ?estacionamiento2)
        (venta_objetos ?venta_objetos2)
        (permiso_foto ?permiso_foto2)
        (accesibilidad ?accesibilidad2)
        (servicio_guiado ?servicio_guiado2)
        (visita_virtual ?visita_virtual2)
        (servicio_biblioteca ?servicio_biblioteca2)
        (sitio_web ?sitio_web2)
    )
    =>
    ;; Condiciones lógicas usando 'or' en la regla
    (if (or (eq ?distrito_especificado ?distrito)
            (eq ?distrito_especificado "no relevante")) then
        (if (or (eq ?categoria_especificada ?categoria)
                (eq ?categoria_especificada "no relevante")) then
            (printout t "Museo recomendado 2: " ?id_museo crlf)
        )
    )
)

-----------------------------------------------------

(assert(museo(id_museo 1) (distrito "San Borja") 
    (dia_atencion "Lunes")
    (categoria "Historia") (estacionamiento TRUE) 
    (venta_objetos TRUE) (permiso_foto TRUE) (accesibilidad TRUE) 
    (servicio_guiado TRUE) (visita_virtual TRUE) 
    (servicio_biblioteca TRUE) (sitio_web TRUE)))

(assert(museo(id_museo 2) (distrito "San Borja") 
    (dia_atencion "Martes")
    (categoria "Historia") (estacionamiento TRUE) 
    (venta_objetos TRUE) (permiso_foto TRUE) (accesibilidad TRUE) 
    (servicio_guiado TRUE) (visita_virtual TRUE) 
    (servicio_biblioteca TRUE) (sitio_web TRUE)))

(assert(museo(id_museo 3) (distrito "Magdalena del Mar")
    (dia_atencion "Lunes")
    (categoria "Arte") (estacionamiento TRUE) 
    (venta_objetos TRUE) (permiso_foto TRUE) (accesibilidad TRUE) 
    (servicio_guiado TRUE) (visita_virtual TRUE) 
    (servicio_biblioteca TRUE) (sitio_web TRUE)))

(assert(museo(id_museo 4) (distrito "Cercado de Lima")
    (dia_atencion "Martes")
    (categoria "Arte") (estacionamiento TRUE) 
    (venta_objetos TRUE) (permiso_foto TRUE) (accesibilidad TRUE) 
    (servicio_guiado TRUE) (visita_virtual TRUE) 
    (servicio_biblioteca TRUE) (sitio_web TRUE)))

-----------------------------------------------------

(assert(preferencias_usuario(distrito_especificado "San Borja") (categoria_especificada "no relevante")))
(assert(preferencias_usuario(distrito_especificado "Magdalena del Mar") (categoria_especificada "no relevante")))
(assert(preferencias_usuario(distrito_especificado "Cercado de Lima") (categoria_especificada "no relevante")))
(assert(preferencias_usuario(categoria_especificada "Historia") (distrito_especificado "no relevante")))
(assert(preferencias_usuario(categoria_especificada "Arte") (distrito_especificado "no relevante")))
(assert(preferencias_usuario(distrito_especificado "San Borja") (categoria_especificada "Historia")))

-----------------------------------------------------

(deftemplate esperancito
    (slot nivel_dulzura)
    (slot nombre)
)

(deftemplate encontrar_caracteristica
    (slot nivel_dulzura)
)

(defrule regla_cute
    (esperancito (nivel_dulzura ?dulzura) (nombre ?nombre))
    (encontrar_caracteristica (nivel_dulzura ?dulzura))
    =>
    (printout t ?nombre " tiene un nivel de dulzura = " ?dulzura crlf)
)

(assert(esperancito (nivel_dulzura 10) (nombre "Jamil")))
(assert(encontrar_caracteristica (nivel_dulzura 10)))

-----------------------------------------------------

# ESTRUCTURA DE CONSOLA CLIPS

(clear) ; Limpia el entorno
(deftemplate esperancito
    (slot nivel_dulzura)
    (slot nombre))
(deftemplate encontrar_caracteristica
    (slot nivel_dulzura))
(defrule regla_cute
    (esperancito (nivel_dulzura ?dulzura) (nombre ?nombre))
    (encontrar_caracteristica (nivel_dulzura ?dulzura))
    =>
    (printout t ?nombre " tiene un nivel de dulzura = " ?dulzura crlf))

(assert(esperancito (nivel_dulzura 10) (nombre "Jamil")))
(assert(encontrar_caracteristica (nivel_dulzura 10)))
(run) ; Ejecuta las reglas

----------------------------------------------------------

(deftemplate esperancito
    (slot nombre)
    (slot nivel_dulzura)
)

(defrule regla_cute
    (esperancito (nombre ?nombre) (nivel_dulzura 10))
    =>
    (printout t ?nombre " tiene un nivel de dulzura = 10 " crlf)
)


(deffacts esperancito
    (esperancito (nombre "Jamil") (nivel_dulzura 10))
)

----------------------------------------------------------