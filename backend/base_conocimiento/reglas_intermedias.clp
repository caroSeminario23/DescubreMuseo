; 2. REGLAS INTERMEDIAS

; Reglas sobre tarifa
; Si tarifa_usuario = nula → min_tarifa=0 y max_tarifa=0
(defrule regla_tarifa_nula
    (preferencias_usuario (tarifa_usuario "nula"))
    =>
    (assert (procesamiento_tarifa (min_tarifa 0) (max_tarifa 0)))
)

; Si tarifa_usuario=barata → min_tarifa=0 y max_tarifa=15
(defrule regla_tarifa_barata
    (preferencias_usuario (tarifa_usuario "barata"))
    =>
    (assert (procesamiento_tarifa (min_tarifa 0) (max_tarifa 15)))
)

; Si tarifa_usuario=media → min_tarifa=15 y max_tarifa=30
(defrule regla_tarifa_media
    (preferencias_usuario (tarifa_usuario "media"))
    =>
    (assert (procesamiento_tarifa (min_tarifa 15) (max_tarifa 30)))
)

; Si tarifa_usuario=alta → min_tarifa=30 y max_tarifa=45
(defrule regla_tarifa_alta
    (preferencias_usuario (tarifa_usuario "alta"))
    =>
    (assert (procesamiento_tarifa (min_tarifa 30) (max_tarifa 45)))
)

; Si tarifa_usuario=muy_alta → min_tarifa=45 y max_tarifa=1000
(defrule regla_tarifa_muy_alta
    (preferencias_usuario (tarifa_usuario "muy_alta"))
    =>
    (assert (procesamiento_tarifa (min_tarifa 45) (max_tarifa 1000)))
)


; Reglas sobre reseña
; Si reseña_usuario=negativa → min_puntaje=0 y max_puntaje=1.25
(defrule regla_resena_negativa
    (preferencias_usuario (resena_usuario "negativa"))
    =>
    (assert (procesamiento_resena (min_puntaje 0)(max_puntaje 1.25)))
)

; Si reseña_usuario=neutral → min_puntaje=1.25 y max_puntaje=2.5
(defrule regla_resena_neutral
    (preferencias_usuario (resena_usuario "neutral"))
    =>
    (assert (procesamiento_resena (min_puntaje 1.25)(max_puntaje 2.5)))
)

; Si reseña_usuario=positiva → min_puntaje=2.5 y max_puntaje=3.75
(defrule regla_resena_positiva
    (preferencias_usuario (resena_usuario "positiva"))
    =>
    (assert (procesamiento_resena (min_puntaje 2.5)(max_puntaje 3.75)))
)

; Si reseña_usuario=muy_positiva → min_puntaje=3.75 y max_puntaje=5.1
(defrule regla_resena_muy_positiva
    (preferencias_usuario (resena_usuario "muy_positiva"))
    =>
    (assert (procesamiento_resena (min_puntaje 3.75)(max_puntaje 5.1)))
)


; Reglas sobre servicios
; Si comida_disponible=True → servicio_restaurante_usuario=True
(defrule regla_servicio_restaurante
    (preferencias_usuario (comida_disponible TRUE))
    =>
    (assert (procesamiento_comida (servicio_restaurante_usuario TRUE)))
)

; Si comida_disponible=True → servicio_cafeteria_usuario=True
(defrule regla_servicio_cafeteria
    (preferencias_usuario (comida_disponible TRUE))
    =>
    (assert (procesamiento_comida (servicio_cafeteria_usuario TRUE)))
)


; Reglas sobre redes sociales y comunicación
; Si presencia_redes_sociales → pag_facebook_existe=True
(defrule regla_facebook
    (preferencias_usuario (presencia_redes_sociales TRUE))
    =>
    (assert (procesamiento_redes_sociales (pag_facebook_existe TRUE)))
)

; Si presencia_redes_sociales → pag_instagram_existe=True
(defrule regla_instagram
    (preferencias_usuario (presencia_redes_sociales TRUE))
    =>
    (assert (procesamiento_redes_sociales (pag_instagram_existe TRUE)))
)

; Si presencia_redes_sociales → pag_tiktok_existe=True
(defrule regla_tiktok
    (preferencias_usuario (presencia_redes_sociales TRUE))
    =>
    (assert (procesamiento_redes_sociales (pag_tiktok_existe TRUE)))
)

; Si existencia_medios_comunicacion → telefono_existe=True
(defrule regla_telefono
    (preferencias_usuario (existencia_medios_comunicacion TRUE))
    =>
    (assert (procesamiento_medios_comunicacion (telefono_existe TRUE)))
)

; Si existencia_medios_comunicacion → email_existe=True
(defrule regla_email
    (preferencias_usuario (existencia_medios_comunicacion TRUE))
    =>
    (assert (procesamiento_medios_comunicacion (email_existe TRUE)))
)


; Reglas sobre restaurantes cercanos
; Si cantidad_rest_cerca=ningun → min_rest_prox=0 y max_rest_prox=0
(defrule regla_rest_cerca_ningun
    (preferencias_usuario (cantidad_rest_cerca "ningun"))
    =>
    (assert (procesamiento_restaurantes (min_rest_prox 0) (max_rest_prox 0)))
)

; Si cantidad_rest_cerca=pocos → min_rest_prox=0 y max_rest_prox=1000
(defrule regla_rest_cerca_pocos
    (preferencias_usuario (cantidad_rest_cerca "pocos"))
    =>
    (assert (procesamiento_restaurantes (min_rest_prox 0) (max_rest_prox 1000)))
)

; Si cantidad_rest_cerca=algunos → min_rest_prox=1000 y max_rest_prox=2000
(defrule regla_rest_cerca_algunos
    (preferencias_usuario (cantidad_rest_cerca "algunos"))
    =>
    (assert (procesamiento_restaurantes (min_rest_prox 1000) (max_rest_prox 2000)))
)

; Si cantidad_rest_cerca=muchos → min_rest_prox=2000 y max_rest_prox=3000
(defrule regla_rest_cerca_muchos
    (preferencias_usuario (cantidad_rest_cerca "muchos"))
    =>
    (assert (procesamiento_restaurantes (min_rest_prox 2000) (max_rest_prox 3000)))
)

; Si cantidad_rest_cerca=demasiados → min_rest_prox=3000 y max_rest_prox=10000
(defrule regla_rest_cerca_demasiados
    (preferencias_usuario (cantidad_rest_cerca "demasiados"))
    =>
    (assert (procesamiento_restaurantes (min_rest_prox 3000) (max_rest_prox 10000)))
)


; Reglas sobre atracciones cercanas
; Si cantidad_atrac_cerca=ningun → min_atracciones=0 y max_atracciones=0
(defrule regla_atrac_cerca_ningun
    (preferencias_usuario (cantidad_atrac_cerca "ningun"))
    =>
    (assert (procesamiento_atracciones (min_atracciones 0) (max_atracciones 0)))
)

; Si cantidad_atrac_cerca=pocos → min_atracciones=0 y max_atracciones=100
(defrule regla_atrac_cerca_pocos
    (preferencias_usuario (cantidad_atrac_cerca "pocos"))
    =>
    (assert (procesamiento_atracciones (min_atracciones 0) (max_atracciones 100)))
)

; Si cantidad_atrac_cerca=algunos → min_atracciones=100 y max_atracciones=200
(defrule regla_atrac_cerca_algunos
    (preferencias_usuario (cantidad_atrac_cerca "algunos"))
    =>
    (assert (procesamiento_atracciones (min_atracciones 100) (max_atracciones 200)))
)

; Si cantidad_atrac_cerca=muchos → min_atracciones=200 y max_atracciones=300
(defrule regla_atrac_cerca_muchos
    (preferencias_usuario (cantidad_atrac_cerca "muchos"))
    =>
    (assert (procesamiento_atracciones (min_atracciones 200) (max_atracciones 300)))
)

; Si cantidad_atrac_cerca=demasiados → min_atracciones=300 y max_atracciones=10000
(defrule regla_atrac_cerca_demasiados
    (preferencias_usuario (cantidad_atrac_cerca "demasiados"))
    =>
    (assert (procesamiento_atracciones (min_atracciones 300) (max_atracciones 10000)))
)