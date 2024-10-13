(deftemplate procesamiento_tarifa
    (slot min_tarifa)
    (slot max_tarifa)
)

(deftemplate procesamiento_resena
    (slot min_puntaje)
    (slot max_puntaje)
)

(deftemplate procesamiento_comida
    (slot servicio_restaurante_usuario)
    (slot servicio_cafeteria_usuario)
)

(deftemplate procesamiento_redes_sociales
    (slot pag_facebook_existe)
    (slot pag_instagram_existe)
    (slot pag_tiktok_existe)
)

(deftemplate procesamiento_medios_comunicacion
    (slot telefono_existe)
    (slot email_existe)
)

(deftemplate procesamiento_restaurantes
    (slot min_rest_prox)
    (slot max_rest_prox)
)

(deftemplate procesamiento_atracciones
    (slot min_atracciones)
    (slot max_atracciones)
)