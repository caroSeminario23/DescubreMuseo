(defrule rg_superior1
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
        (ha_inicio ?ha_inicio)
        (ha_fin ?ha_fin)
        (tarifa_normal ?tarifa_normal)
        (tarifa_ninos ?tarifa_ninos)
        (tarifa_ancianos ?tarifa_ancianos)
        (tarifa_discapacitados ?tarifa_discapacitados)
        (puntaje_resena ?puntaje_resena)
        ;(telefono ?telefono)
        ;(email ?email)
        ;(servicio_restaurante ?servicio_restaurante)
        ;(servicio_cafeteria ?servicio_cafeteria)
        ;(pag_facebook ?pag_facebook)
        ;(pag_instagram ?pag_instagram)
        ;(pag_tiktok ?pag_tiktok)
        (n_restaurantes_prox ?n_restaurantes_prox)
        (n_atracciones_prox ?n_atracciones_prox)
        (hc_inicio ?hc_inicio)
        (hc_fin ?hc_fin)
        (dia_concurrido $?dias_concurrido)
    )

    (preferencias_usuario
        (distrito_especificado ?distrito_especificado)
        (reserva_usuario ?reserva_usuario)
        (estacionamiento_usuario ?estacionamiento_usuario)
        (venta_objetos_usuario ?venta_objetos_usuario)
        (permiso_foto_usuario ?permiso_foto_usuario)
        (accesibilidad_usuario ?accesibilidad_usuario)
        (servicio_guiado_usuario ?servicio_guiado_usuario)
        (visita_virtual_usuario ?visita_virtual_usuario)
        (servicio_biblioteca_usuario ?servicio_biblioteca_usuario)
        (sitio_web_existe ?sitio_web_existe)
        (categoria_especificada ?categoria_especificada)
        (dia_especificado ?dia_especificado)
        (hora_especificada ?hora_especificada)
        (tarifa_usuario ?tarifa_usuario)
        (descuento_ninos ?descuento_ninos)
        (descuento_ancianos ?descuento_ancianos)
        (descuento_discapacitados ?descuento_discapacitados)
        (resena_usuario ?resena_usuario)
        ;(existencia_medios_comunicacion ?existencia_medios_comunicacion)
        ;(comida_disponible ?comida_disponible)
        ;(presencia_redes_sociales ?presencia_redes_sociales)
        (cantidad_rest_cerca ?cantidad_rest_cerca)
        (cantidad_atrac_cerca ?cantidad_atrac_cerca)
        (concurrencia ?concurrencia_usuario)
    )

    (procesamiento_tarifa
        (min_tarifa ?min_tarifa)
        (max_tarifa ?max_tarifa)
    )

    (procesamiento_resena
        (min_puntaje ?min_puntaje)
        (max_puntaje ?max_puntaje)
    )

    ;(procesamiento_medios_comunicacion
    ;    (telefono_existe ?telefono_existe)
    ;    (email_existe ?email_existe)
    ;)

    ;(procesamiento_comida
    ;    (servicio_restaurante_usuario ?servicio_restaurante_usuario)
    ;    (servicio_cafeteria_usuario ?servicio_cafeteria_usuario)
    ;)

    ;(procesamiento_redes_sociales
    ;    (pag_facebook_existe ?pag_facebook_existe)
    ;    (pag_instagram_existe ?pag_instagram_existe)
    ;    (pag_tiktok_existe ?pag_tiktok_existe)
    ;)

    (procesamiento_restaurantes
        (min_rest_prox ?min_rest_prox)
        (max_rest_prox ?max_rest_prox)
    )

    (procesamiento_atracciones
        (min_atracciones ?min_atracciones)
        (max_atracciones ?max_atracciones)
    )

    ;Si el distrito del museo es igual al distrito especificado por el usuario
    (test
        (or 
            (eq ?distrito ?distrito_especificado)
            (eq ?distrito_especificado No_relevante)
        )
    )
    (test
        (or
            (eq ?reserva_entrada ?reserva_usuario)
            (eq ?reserva_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?servicio_guiado ?servicio_guiado_usuario)
            (eq ?servicio_guiado_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?servicio_biblioteca ?servicio_biblioteca_usuario)
            (eq ?servicio_biblioteca_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?venta_objetos ?venta_objetos_usuario)
            (eq ?venta_objetos_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?accesibilidad ?accesibilidad_usuario)
            (eq ?accesibilidad_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?permiso_foto ?permiso_foto_usuario)
            (eq ?permiso_foto_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?estacionamiento ?estacionamiento_usuario)
            (eq ?estacionamiento_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?visita_virtual ?visita_virtual_usuario)
            (eq ?visita_virtual_usuario No_relevante)
        )
    )
    (test
        (or
            (eq ?sitio_web ?sitio_web_existe)
            (eq ?sitio_web_existe No_relevante)
        )
    )
    (test
        (or
            (eq ?categoria_especificada No_relevante)
            (member$ ?categoria_especificada ?categorias)
        )
    )
    (test
        (or
            (eq ?dia_especificado No_relevante)
            (member$ ?dia_especificado ?dias_atencion)
        )
    )
    (test
        (or
            (eq ?hora_especificada No_relevante)
            (and
                (>= ?hora_especificada ?ha_inicio)
                (<= ?hora_especificada ?ha_fin)
            )
        )
    )
    (test
        (and
            (>= ?tarifa_normal ?min_tarifa)
            (<= ?tarifa_normal ?max_tarifa)
        )
    )
    (test
        (or
            (eq ?descuento_ninos No_relevante)
            (and
                (eq ?descuento_ninos Relevante)
                (< ?tarifa_ninos ?tarifa_normal)
            )
        )
    )
    (test
        (or
            (eq ?descuento_ancianos No_relevante)
            (and
                (eq ?descuento_ancianos Relevante)
                (< ?tarifa_ancianos ?tarifa_normal)
            )
        )
    )
    (test
        (or
            (eq ?descuento_discapacitados No_relevante)
            (and
                (eq ?descuento_discapacitados Relevante)
                (< ?tarifa_discapacitados ?tarifa_normal)
            )
        )
    )
    (test
        (and
            (>= ?puntaje_resena ?min_puntaje)
            (<= ?puntaje_resena ?max_puntaje)
        )
    )
    ;(test
    ;    (and
    ;        (eq ?existencia_medios_comunicacion Relevante)
    ;        (or
    ;            (eq ?telefono ?telefono_existe)
    ;            (eq ?email ?email_existe)
    ;        )
    ;    )
    ;)
    ;(test
    ;    (and
    ;        (eq ?comida_disponible Relevante)
    ;        (or
    ;            (eq ?servicio_restaurante ?servicio_restaurante_usuario)
    ;            (eq ?servicio_cafeteria ?servicio_cafeteria_usuario)
    ;        )
    ;    )
    ;)
    ;(test
    ;    (and
    ;        (eq ?presencia_redes_sociales Relevante)
    ;        (or
    ;            (eq ?pag_facebook ?pag_facebook_existe)
    ;            (eq ?pag_instagram ?pag_instagram_existe)
    ;            (eq ?pag_tiktok ?pag_tiktok_existe)
    ;        )
    ;    )
    ;)
    (test
        (and
            (>= ?n_restaurantes_prox ?min_rest_prox)
            (<= ?n_restaurantes_prox ?max_rest_prox)
        )
    )
    (test
        (and
            (>= ?n_atracciones_prox ?min_atracciones)
            (<= ?n_atracciones_prox ?max_atracciones)
        )
    )
    (test
        (or
            (and
                (eq ?concurrencia_usuario Relevante)
                (not (member$ ?dia_especificado ?dias_concurrido))
                (or
                    (< ?hora_especificada ?hc_inicio)
                    (>= ?hora_especificada ?hc_fin)
                )
            )
            (eq ?concurrencia_usuario No_relevante)
        )
    )

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)