; 1. PLANTILLAS
(deftemplate preferencias_usuario
    (slot distrito_especificado)
    (slot dia_especificado)
    (slot hora_especificada)
    (slot categoria_especificada)
    (slot concurrencia)
    (slot tarifa_usuario)
    (slot resena_usuario)
    (slot descuento_ninos)
    (slot descuento_ancianos)
    (slot descuento_discapacitados)
    (slot comida_disponible)
    (slot reserva_entrada)
    (slot estacionamiento_usuario)
    (slot venta_objetos_usuario)
    (slot permiso_foto_usuario)
    (slot accesibilidad_usuario)
    (slot servicio_guiado_usuario)
    (slot visita_virtual_usuario)
    (slot servicio_biblioteca_usuario)
    (slot presencia_redes_sociales)
    (slot existencia_medios_comunicacion)
    (slot sitio_web_existe)
    (slot cantidad_rest_cerca)
    (slot cantidad_atrac_cerca)
)

(deftemplate procesamiento_tarifa
    (slot min-tarifa)
    (slot max-tarifa)
)

(deftemplate procesamiento_puntaje
    (slot min-puntaje)
    (slot max-puntaje)
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

(deftemplate museo
    (slot id_museo)
    (slot distrito)
    (slot puntaje_resena)
    (slor ha_inicio)
    (slot ha_fin)
    (slot hc_inicio)
    (slot hc_fin)
    (slot tarifa_normal)
    (slot tarifa_ninos)
    (slot tarifa_ancianos)
    (slot tarifa_discapacitados)
    (slot reserva_entrada)
    (slot servicio_restaurante)
    (slot servicio_cafeteria)
    (slot servicio_guiado)
    (slot servicio_biblioteca)
    (slot venta_objetos)
    (slot accesibilidad)
    (slot permiso_foto)
    (slot estacionamiento)
    (slot visita_virtual)
    (slot n_restaurantes_prox)
    (slot n_atracciones_prox)
    (slot telefono)
    (slot email)
    (slot sitio_web)
    (slot pag_facebook)
    (slot pag_instagram)
    (slot pag_tiktok)
    (slot categoria)
    (slot dia_atencion)
    (slot dia_concurrido)
)

(deftemplate recomendacion
    (slot id_museo)
)