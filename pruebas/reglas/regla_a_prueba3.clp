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
        (ha_inicio ?ha_inicio)
        (ha_fin ?ha_fin)
        (hc_inicio ?hc_inicio)
        (hc_fin ?hc_fin)
        (dia_concurrido $?dias_concurrido)
        (tarifa_normal ?tarifa_normal)
        (tarifa_ninos ?tarifa_ninos)
        (tarifa_ancianos ?tarifa_ancianos)
        (tarifa_discapacitados ?tarifa_discapacitados)
        (puntaje_resena ?puntaje_resena)
        (servicio_restaurante ?servicio_restaurante)
        (servicio_cafeteria ?servicio_cafeteria)
        (pag_facebook ?pag_facebook)
        (pag_instagram ?pag_instagram)
        (pag_tiktok ?pag_tiktok)
        (telefono ?telefono)
        (email ?email)
        (n_restaurantes_prox ?n_restaurantes_prox)
        (n_atracciones_prox ?n_atracciones_prox)
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
        (hora_especificada ?hora_especificada)
        (concurrencia ?concurrencia_usuario)
        (tarifa_usuario ?tarifa_usuario)
        (descuento_ninos ?descuento_ninos)
        (descuento_ancianos ?descuento_ancianos)
        (descuento_discapacitados ?descuento_discapacitados)
        (resena_usuario ?resena_usuario)
        (comida_disponible ?comida_disponible)
        (presencia_redes_sociales ?presencia_redes_sociales)
        (existencia_medios_comunicacion ?existencia_medios_comunicacion)
        (cantidad_rest_cerca ?cantidad_rest_cerca)
        (cantidad_atrac_cerca ?cantidad_atrac_cerca)
    )      

    (procesamiento_tarifa
        (min_tarifa ?min_tarifa)
        (max_tarifa ?max_tarifa)
    )

    (procesamiento_resena
        (min_puntaje ?min_puntaje)
        (max_puntaje ?max_puntaje)
    )

    (procesamiento_comida
        (servicio_restaurante_usuario ?servicio_restaurante_usuario)
        (servicio_cafeteria_usuario ?servicio_cafeteria_usuario)
    )

    (procesamiento_redes_sociales
        (pag_facebook_existe ?pag_facebook_existe)
        (pag_instagram_existe ?pag_instagram_existe)
        (pag_tiktok_existe ?pag_tiktok_existe)
    )

    (procesamiento_medios_comunicacion
        (telefono_existe ?telefono_existe)
        (email_existe ?email_existe)
    )

    (procesamiento_restaurantes
        (min_rest_prox ?min_rest_prox)
        (max_rest_prox ?max_rest_prox)
    )

    (procesamiento_atracciones
        (min_atracciones ?min_atracciones)
        (max_atracciones ?max_atracciones)
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
    ;y la hora de inicio del museo es menor o igual a la hora especificada por el usuario
    ;y la hora de fin del museo es mayor o igual a la hora especificada por el usuario
    ;y la hora de inicio de concurrencia del museo es mayor a la hora especificada por el usuario
    ;o la hora de fin de concurrencia del museo es menor a la hora especificada por el usuario
    ;y la tarifa del museo es mayor o igual a la tarifa mínima especificada por el usuario
    ;y la tarifa del museo es menor o igual a la tarifa máxima especificada por el usuario
    ;y la tarifa de niños (del museo) es menor a la tarifa normal del museo
    ;y la tarifa de ancianos (del museo) es menor a la tarifa normal del museo
    ;y la tarifa de discapacitados (del museo) es menor a la tarifa normal del museo
    ;y el puntaje de la reseña del museo es mayor o igual al puntaje mínimo especificado por el usuario
    ;y el puntaje de la reseña del museo es menor al puntaje máximo especificado por el usuario
    ;y la comida disponible es relevante para el usuario
    ;y la presencia de redes sociales es relevante para el usuario
    ;y la existencia de medios de comunicación es relevante para el usuario
    ;y la cantidad de restaurantes cercanos es mayor o igual a min_rest_prox
    ;y la cantidad de restaurantes cercanos es menor o igual a max_rest_prox
    ;y la cantidad de atracciones cercanas es mayor o igual a min_atracciones
    ;y la cantidad de atracciones cercanas es menor o igual a max_atracciones
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
    (test(>= ?hora_especificada ?ha_inicio))
    (test(<= ?hora_especificada ?ha_fin))
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
    (test(>= ?tarifa_normal ?min_tarifa))
    (test(<= ?tarifa_normal ?max_tarifa))
    (test
        (or
            (and
                (eq ?descuento_ninos Relevante)
                (< ?tarifa_ninos ?tarifa_normal)
            )
            (eq ?descuento_ninos No_relevante)
        )
    )
    (test
        (or
            (and
                (eq ?descuento_ancianos Relevante)
                (< ?tarifa_ancianos ?tarifa_normal)
            )
            (eq ?descuento_ancianos No_relevante)
        )
    )
    (test
        (or
            (and
                (eq ?descuento_discapacitados Relevante)
                (< ?tarifa_discapacitados ?tarifa_normal)
            )
            (eq ?descuento_discapacitados No_relevante)
        )
    )
    (test(>= ?puntaje_resena ?min_puntaje))
    (test(< ?puntaje_resena ?max_puntaje))
    (test
        (or
            (and
                (eq ?comida_disponible Relevante)
                (or
                    (eq ?servicio_restaurante ?servicio_restaurante_usuario)
                    (eq ?servicio_cafeteria ?servicio_cafeteria_usuario)
                )
            )
            (eq ?comida_disponible No_relevante)
        )
    )
    (test
        (or
            (and
                (eq ?presencia_redes_sociales Relevante)
                (or
                    (eq ?pag_facebook ?pag_facebook_existe)
                    (eq ?pag_instagram ?pag_instagram_existe)
                    (eq ?pag_tiktok ?pag_tiktok_existe)
                )
            )
            (eq ?presencia_redes_sociales No_relevante)
        )
    )
    (test
        (or
            (and
                (eq ?existencia_medios_comunicacion Relevante)
                (or
                    (eq ?telefono ?telefono_existe)
                    (eq ?email ?email_existe)
                )
            )
            (eq ?existencia_medios_comunicacion No_relevante)
        )
    )
    (test(>= ?n_restaurantes_prox ?min_rest_prox))
    (test(<= ?n_restaurantes_prox ?max_rest_prox))
    (test(>= ?n_atracciones_prox ?min_atracciones))
    (test(<= ?n_atracciones_prox ?max_atracciones))

    =>
    (assert (recomendacion (id_museo ?id_museo)))
    (printout t "Museo recomendado: " ?id_museo crlf)
)