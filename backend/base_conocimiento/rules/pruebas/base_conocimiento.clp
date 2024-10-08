# 1. Variables a utilizar en el sistema experto
(deftemplate museo
    (slot distrito)

    (slot dia_especificado)
    (slot dia_atention)
    (slot abierto_dia_especificado)
    (slot ha_inicio)
    (slot ha_fin)
    (slot horario_disponible)


    (slot dia_concurrido)
    (slot concurrencia)
    (slot no_concurrido_dia_especificado)
    (slot hc_inicio)
    (slot hc_fin)
    (slot hora_especificada)
    (slot horario_no_concurrido)

    (slot categoria)

    (slot tarifa_nula)
    (slot tarifa_barata)
    (slot tarifa_media)
    (slot tarifa_alta)
    (slot tarifa_muy_alta)
    (slot tarifa_normal)
    (slot tarifa_normal_condicion)

    (slot puntaje_reseña)
    (slot reseña_negativa)
    (slot reseña_neutral)
    (slot reseña_positiva)
    (slot reseña_muy_positiva)
    (slot puntaje_reseña_condicion)

    (slot descuento_niños)
    (slot descuento_ancianos)
    (slot descuento_discapacitados)
    (slot tarifa_niños)
    (slot tarifa_ancianos)
    (slot tarifa_discapacitados)
    (slot descuento_niños_condicion)
    (slot descuento_ancianos_condicion)
    (slot descuento_discapacitados_condicion)
    (slot desigualdad_descuento_niños)
    (slot desigualdad_descuento_ancianos)
    (slot desigualdad_descuento_discapacitados)

    (slot comida_disponible)
    (slot servicio_restaurante)
    (slot servicio_cafeteria)

    (slot reserva_entrada)
    (slot estacionamiento)
    (slot venta_objetos)
    (slot permiso_foto)
    (slot accesibilidad)
    (slot servicio_guiado)
    (slot visita_virtual)
    (slot servicio_biblioteca)

    (slot pag_facebook_existe)
    (slot pag_instagram_existe)
    (slot pag_tiktok_existe)
    (slot telefono_existe)
    (slot email_existe)
    (slot sitio_web_existe)
    
    (slot ningun_restaurante_cerca)
    (slot pocos_restaurantes_cerca)
    (slot algunos_restaurantes_cerca)
    (slot muchos_restaurantes_cerca)
    (slot demasiados_restaurantes_cerca)
    (slot n_restaurantes_prox)
    (slot ningun_rest_prox_condicion)
    (slot pocos_rest_prox_condicion)
    (slot algunos_rest_prox_condicion)
    (slot muchos_rest_prox_condicion)
    (slot demasiados_rest_prox_condicion)
    (slot igualdad_ningun_rest_prox)
    (slot desigualdad_pocos_rest_prox1)
    (slot desigualdad_pocos_rest_prox2)
    (slot desigualdad_algunos_rest_prox1)
    (slot desigualdad_algunos_rest_prox2)
    (slot desigualdad_muchos_rest_prox1)
    (slot desigualdad_muchos_rest_prox2)
    (slot desigualdad_demasiados_rest_prox)

    (slot ninguna_atraccion_cerca)
    (slot pocas_atracciones_cerca)
    (slot algunas_atracciones_cerca)
    (slot muchas_atracciones_cerca)
    (slot demasiadas_atracciones_cerca)
    (slot n_atracciones_prox)
    (slot ninguna_atr_prox_condicion)
    (slot pocas_atr_prox_condicion)
    (slot algunas_atr_prox_condicion)
    (slot muchas_atr_prox_condicion)
    (slot demasiadas_atr_prox_condicion)
    (slot igualdad_ninguna_atr_prox)
    (slot desigualdad_pocas_atr_prox1)
    (slot desigualdad_pocas_atr_prox2)
    (slot desigualdad_algunas_atr_prox1)
    (slot desigualdad_algunas_atr_prox2)
    (slot desigualdad_muchas_atr_prox1)
    (slot desigualdad_muchas_atr_prox2)
    (slot desigualdad_demasiadas_atr_prox)
)



# 2. Reglas intermedias

# Reglas de día y hora
# Si dia_especificado=dia_atencion → abierto_dia_especificado=True
(defrule regla1
    (museo (dia_especificado ?dia_especificado) (dia_atention ?dia_atencion))
    =>
    (assert (museo (abierto_dia_especificado True)))
)

# Si concurrencia=relevante y (dia_especificado≠dia_concurrido) → no_concurrido_dia_especificado=True
(defrule regla2
    (museo (concurrencia relevante) (dia_especificado ?dia_especificado) (dia_concurrido ?dia_concurrido))
    (test (neq ?dia_especificado ?dia_concurrido))
    =>
    (assert (museo (no_concurrido_dia_especificado True)))
)

# Si abierto_dia_especificado=True y (ha_inicio≤hora_especificada≤ha_fin) → horario_disponible=True
(defrule regla3
    (museo (abierto_dia_especificado True) (ha_inicio ?ha_inicio) (ha_fin ?ha_fin) (hora_especificada ?hora_especificada))
    (test (and (<= ?ha_inicio ?hora_especificada) (<= ?hora_especificada ?ha_fin)))
    =>
    (assert (museo (horario_disponible True)))
)

# Si no_concurrido_dia_especificado=True y (hora_especificada<hc_inicio y hora_especificada>hc_fin) → horario_no_concurrido=True
(defrule regla4
    (museo (no_concurrido_dia_especificado True) (hc_inicio ?hc_inicio) (hc_fin ?hc_fin) (hora_especificada ?hora_especificada))
    (test (or (< ?hora_especificada ?hc_inicio) (> ?hora_especificada ?hc_fin)))
    =>
    (assert (museo (horario_no_concurrido True)))
)


# Reglas de tarifa
# Si tarifa nula=True → tarifa_normal=0
(defrule regla5
    (museo (tarifa_nula True))
    =>
    (assert (museo (tarifa_normal_condicion (min 0) (max 0)))
)

# Si tarifa barata=True → 0<tarifa_normal≤15
(defrule regla6
    (museo (tarifa_barata True))
    =>
    (assert (tarifa_normal_condicion (min 0) (max 15)))
)

# Si tarifa media=True → 15<tarifa_normal≤30 
(defrule regla7
    (museo (tarifa_media True))
    =>
    (assert (tarifa_normal_condicion (min 15) (max 30)))
)

# Si tarifa alta=True → 30<tarifa_normal≤45
(defrule regla8
    (museo (tarifa_alta True))
    =>
    (assert (tarifa_normal_condicion (min 30) (max 45)))
)

# Si tarifa muy alta=True → tarifa_normal >45
(defrule regla9
    (museo (tarifa_muy_alta True))
    =>
    (assert (tarifa_normal_condicion (min 45)))
)

# Reglas de reseña
# Si reseña_negativa=True → 0≤puntaje_reseña≤1.25
(defrule regla10
    (museo (reseña_negativa True))
    =>
    (assert (puntaje_reseña_condicion (min 0) (max 1.25)))
)

# Si reseña_neutral=True → 1.25≤puntaje_reseña≤2.5
(defrule regla11
    (museo (reseña_neutral True))
    =>
    (assert (puntaje_reseña_condicion (min 1.25) (max 2.5)))
)

# Si reseña_positiva=True → 2.5≤puntaje_reseña≤3.75
(defrule regla12
    (museo (reseña_positiva True))
    =>
    (assert (puntaje_reseña_condicion (min 2.5) (max 3.75)))
)

# Si reseña_muy_positiva=True → 3.75≤puntaje_reseña≤5 
(defrule regla13
    (museo (reseña_muy_positiva True))
    =>
    (assert (puntaje_reseña_condicion (min 3.75) (max 5)))
)


# Reglas de descuento
# Si descuento_niños=True → tarifa_ninos<tarifa_normal
(defrule regla14
    (museo (descuento_niños True) (tarifa_niños ?tarifa_niños) (tarifa_normal ?tarifa_normal))
    #(test (< ?tarifa_niños ?tarifa_normal))
    =>
    (assert (descuento_niños_condicion (tarifa_niños ?tarifa_niños) (tarifa_normal ?tarifa_normal)))
    (assert (desigualdad_descuento_niños (tarifa_niños ?tarifa_niños) (tarifa_normal ?tarifa_normal))) # Guarda la desiguadad
)

# Si descuento_ancianos=True → tarifa_ancianos<tarifa_normal
(defrule regla15
    (museo (descuento_ancianos True) (tarifa_ancianos ?tarifa_ancianos) (tarifa_normal ?tarifa_normal))
    #(test (< ?tarifa_ancianos ?tarifa_normal))
    =>
    (assert (descuento_ancianos_condicion (tarifa_ancianos ?tarifa_ancianos) (tarifa_normal ?tarifa_normal)))
    (assert (desigualdad_descuento_ancianos (tarifa_ancianos ?tarifa_ancianos) (tarifa_normal ?tarifa_normal))) # Guarda la desiguadad
)

# Si descuento_discapacitados=True → tarifa_discapacitados<tarifa_normal
(defrule regla16
    (museo (descuento_discapacitados True) (tarifa_discapacitados ?tarifa_discapacitados) (tarifa_normal ?tarifa_normal))
    #(test (< ?tarifa_discapacitados ?tarifa_normal))
    =>
    (assert (descuento_discapacitados_condicion (tarifa_discapacitados ?tarifa_discapacitados) (tarifa_normal ?tarifa_normal)))
    (assert (desigualdad_descuento_discapacitados (tarifa_discapacitados ?tarifa_discapacitados) (tarifa_normal ?tarifa_normal))) # Guarda la desiguadad
)


# Reglas de servicios
# Si comida_disponible=True → servicio_restaurante=True
(defrule regla17
    (museo (comida_disponible True))
    =>
    (assert (museo (servicio_restaurante True)))
)

# Si comida_disponible=True → servicio_cafeteria=True
(defrule regla18
    (museo (comida_disponible True))
    =>
    (assert (museo (servicio_cafeteria True)))
)


# Reglas de restaurantes cercanos
# Si ningun_restaurante_cerca → n_restaurantes_prox=0
(defrule regla19
    (museo (ningun_restaurante_cerca True) (n_restaurantes_prox ?n_restaurantes_prox))
    =>
    (assert (ningun_rest_prox_condicion (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (igualdad_ningun_rest_prox (n_restaurantes_prox ?n_restaurantes_prox)))
)

# Si pocos_restaurantes_cerca → 0<n_restaurantes_prox≤1000
(defrule regla20
    (museo (pocos_restaurantes_cerca True) (n_restaurantes_prox ?n_restaurantes_prox))
    =>
    (assert (pocos_rest_prox_condicion (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_pocos_rest_prox1 (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_pocos_rest_prox2 (n_restaurantes_prox ?n_restaurantes_prox)))
)

# Si algunos_restaurantes_cerca → 1000<n_restaurantes_prox≤2000
(defrule regla21
    (museo (algunos_restaurantes_cerca True) (n_restaurantes_prox ?n_restaurantes_prox))
    =>
    (assert (algunos_rest_prox_condicion (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_algunos_rest_prox1 (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_algunos_rest_prox2 (n_restaurantes_prox ?n_restaurantes_prox)))
)

# Si muchos_restaurantes_cerca → 2000<n_restaurantes_prox≤3000
(defrule regla22
    (museo (muchos_restaurantes_cerca True) (n_restaurantes_prox ?n_restaurantes_prox))
    =>
    (assert (muchos_rest_prox_condicion (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_muchos_rest_prox1 (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_muchos_rest_prox2 (n_restaurantes_prox ?n_restaurantes_prox)))
)

# Si demasiados_restaurantes_cerca → n_restaurantes_prox>3000
(defrule regla23
    (museo (demasiados_restaurantes_cerca True) (n_restaurantes_prox ?n_restaurantes_prox))
    =>
    (assert (demasiados_rest_prox_condicion (n_restaurantes_prox ?n_restaurantes_prox)))
    (assert (desigualdad_demasiados_rest_prox (n_restaurantes_prox ?n_restaurantes_prox)))
)


# Reglas de atracciones cercanas
# Si ninguna_atraccion_cerca → n_atracciones_prox=0
(defrule regla24
    (museo (ninguna_atraccion_cerca True) (n_atracciones_prox ?n_atracciones_prox))
    =>
    (assert (ninguna_atr_prox_condicion (n_atracciones_prox ?n_atracciones_prox)))
    (assert (igualdad_ninguna_atr_prox (n_atracciones_prox ?n_atracciones_prox)))
)

# Si pocas_atracciones_cerca → 0<n_atracciones_prox≤100
(defrule regla25
    (museo (pocas_atracciones_cerca True) (n_atracciones_prox ?n_atracciones_prox))
    =>
    (assert (pocas_atr_prox_condicion (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_pocas_atr_prox1 (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_pocas_atr_prox2 (n_atracciones_prox ?n_atracciones_prox)))
)

# Si algunas_atracciones_cerca → 100<n_atracciones_prox≤200
(defrule regla26
    (museo (algunas_atracciones_cerca True) (n_atracciones_prox ?n_atracciones_prox))
    =>
    (assert (algunas_atr_prox_condicion (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_algunas_atr_prox1 (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_algunas_atr_prox2 (n_atracciones_prox ?n_atracciones_prox)))
)

# Si muchas_atracciones_cerca → 200<n_atracciones_prox≤300
(defrule regla27
    (museo (muchas_atracciones_cerca True) (n_atracciones_prox ?n_atracciones_prox))
    =>
    (assert (muchas_atr_prox_condicion (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_muchas_atr_prox1 (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_muchas_atr_prox2 (n_atracciones_prox ?n_atracciones_prox)))
)

# Si demasiadas_atracciones_cerca → n_atracciones_prox>300
(defrule regla28
    (museo (demasiadas_atracciones_cerca True) (n_atracciones_prox ?n_atracciones_prox))
    =>
    (assert (demasiadas_atr_prox_condicion (n_atracciones_prox ?n_atracciones_prox)))
    (assert (desigualdad_demasiadas_atr_prox (n_atracciones_prox ?n_atracciones_prox)))
)