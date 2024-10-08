1. Variables a utilizar en las reglas
(deftemplate museo
    (slot nombre_museo)

    (slot distrito_especificado)
    (slot distrito)

    (slot dia_especificado)
    (slot dia_atencion)

    (slot hora_especificada)
    (slot ha_inicio)
    (slot ha_fin)

    (slot categoria_especificada)
    (slot categoria)

    (slot concurrencia)
    (slot dia_concurrido)
    (slot hc_inicio)
    (slot hc_fin)

    (slot tarifa_usuario)
    (slot min_tarifa)
    (slot max_tarifa)
    (slot tarifa_normal)
    
    (slot resena_usuario)
    (slot min_puntaje)
    (slot max_puntaje)
    (slot puntaje_resena)

    (slot descuento_ninos)
    (slot tarifa_ninos)

    (slot descuento_ancianos)
    (slot tarifa_ancianos)

    (slot descuento_discapacitados)
    (slot tarifa_discapacitados)

    (slot comida_disponible)
    (slot servicio_restaurante_usuario)
    (slot servicio_cafeteria_usuario)
    (slot servicio_restaurante)
    (slot servicio_cafeteria)

    (slot reserva_entrada)
    (slot reserva)

    (slot estacionamiento_usuario)
    (slot estacionamiento)

    (slot venta_objetos_usuario)
    (slot venta_objetos)

    (slot permiso_foto_usuario)
    (slot permiso_foto)

    (slot accesibilidad_usuario)
    (slot accesibilidad)

    (slot servicio_guiado_usuario)
    (slot servicio_guiado)

    (slot visita_virtual_usuario)
    (slot visita_virtual)

    (slot servicio_biblioteca_usuario)
    (slot servicio_biblioteca)

    (slot presencia_redes_sociales)
    (slot pag_facebook_existe)
    (slot pag_facebook)
    (slot pag_instagram_existe)
    (slot pag_instagram)
    (slot pag_tiktok_existe)
    (slot pag_tiktok)

    (slot existencia_medios_comunicacion)
    (slot telefono_existe)
    (slot telefono)
    (slot email_existe)
    (slot email)

    (slot sitio_web_existe)
    (slot sitio_web)

    (slot cantidad_rest_cerca)
    (slot min_rest_prox)
    (slot max_rest_prox)
    (slot n_restaurantes_prox)

    (slot cantidad_atrac_cerca)
    (slot min_atracciones)
    (slot max_atracciones)
    (slot n_atracciones_prox)
)

# 2. Reglas intermedias

# Reglas sobre tarifa
# Si tarifa_usuario = nula → min_tarifa=0 y max_tarifa=0
(defrule regla_tarifa_nula
    (museo (tarifa_usuario "nula"))
    =>
    (modify (museo (?min_tarifa 0) (?max_tarifa 0)))
)

# Si tarifa_usuario=barata → min_tarifa=0 y max_tarifa=15
(defrule regla_tarifa_barata
    (museo (tarifa_usuario "barata"))
    =>
    (assert (museo (min_tarifa 0) (max_tarifa 15)))
)

# Si tarifa_usuario=media → min_tarifa=15 y max_tarifa=30
(defrule regla_tarifa_media
    (museo (tarifa_usuario "media"))
    =>
    (assert (museo (min_tarifa 15) (max_tarifa 30)))
)

# Si tarifa_usuario=alta → min_tarifa=30 y max_tarifa=45
(defrule regla_tarifa_alta
    (museo (tarifa_usuario "alta"))
    =>
    (assert (museo (min_tarifa 30) (max_tarifa 45)))
)

# Si tarifa_usuario=muy_alta → min_tarifa=45 y max_tarifa=1000
(defrule regla_tarifa_muy_alta
    (museo (tarifa_usuario "muy_alta"))
    =>
    (assert (museo (min_tarifa 45) (max_tarifa 1000)))
)


# Reglas sobre reseña
# Si reseña_usuario=negativa → min_puntaje=0 y max_puntaje=1.25
(defrule regla_resena_negativa
    (museo(resena_usuario "negativa"))
    =>
    (assert (museo(min_puntaje 0)(max_puntaje 1.25)))
)

# Si reseña_usuario=neutral →  min_puntaje=1.25 y max_puntaje=2.5
(defrule regla_resena_neutral
    (museo(resena_usuario "neutral"))
    =>
    (assert (museo(min_puntaje 1.25)(max_puntaje 2.5)))
)

# Si reseña_usuario=positiva → min_puntaje=2.5 y max_puntaje=3.75
(defrule regla_resena_positiva
    (museo(resena_usuario "positiva"))
    =>
    (assert (museo(min_puntaje 2.5)(max_puntaje 3.75)))
)

# Si reseña_usuario=muy_positiva → min_puntaje=3.75 y max_puntaje=5.1
(defrule regla_resena_muy_positiva
    (museo(resena_usuario "muy_positiva"))
    =>
    (assert (museo(min_puntaje 3.75)(max_puntaje 5.1)))
)


# Reglas sobre servicios
# Si comida_disponible=True → servicio_restaurante_usuario=True
(defrule regla_servicio_restaurante
    (museo (comida_disponible True))
    =>
    (assert (museo (servicio_restaurante_usuario True)))
)

# Si comida_disponible=True → servicio_cafeteria_usuario=True
(defrule regla_servicio_cafeteria
    (museo (comida_disponible True))
    =>
    (assert (museo (servicio_cafeteria_usuario True)))
)


# Reglas sobre redes sociales y comunicación
# Si presencia_redes_sociales → pag_facebook_existe=True
(defrule regla_facebook
    (museo (presencia_redes_sociales True))
    =>
    (assert (museo (pag_facebook_existe True)))
)
# Si presencia_redes_sociales → pag_instagram_existe=True
(defrule regla_instagram
    (museo (presencia_redes_sociales True))
    =>
    (assert (museo (pag_instagram_existe True)))
)

# Si presencia_redes_sociales → pag_tiktok_existe=True
(defrule regla_tiktok
    (museo (presencia_redes_sociales True))
    =>
    (assert (museo (pag_tiktok_existe True)))
)

# Si existencia_medios_comunicacion → telefono_existe=True
(defrule regla_telefono
    (museo (existencia_medios_comunicacion True))
    =>
    (assert (museo (telefono_existe True)))
)

# Si existencia_medios_comunicacion → email_existe=True
(defrule regla_email
    (museo (existencia_medios_comunicacion True))
    =>
    (assert (museo (email_existe True)))
)


# Sobre restaurantes cercanos
# Si cantidad_rest_cerca=ningun → min_rest_prox=0 y max_rest_prox=0
(defrule regla_rest_cerca_ningun
    (museo (cantidad_rest_cerca "ningun"))
    =>
    (assert (museo (min_rest_prox 0) (max_rest_prox 0)))
)

# Si cantidad_rest_cerca=pocos → min_rest_prox=0 y max_rest_prox=1000
(defrule regla_rest_cerca_pocos
    (museo (cantidad_rest_cerca "pocos"))
    =>
    (assert (museo (min_rest_prox 0) (max_rest_prox 1000)))
)

# Si cantidad_rest_cerca=algunos → min_rest_prox=1000 y max_rest_prox=2000
(defrule regla_rest_cerca_algunos
    (museo (cantidad_rest_cerca "algunos"))
    =>
    (assert (museo (min_rest_prox 1000) (max_rest_prox 2000)))
)

# Si cantidad_rest_cerca=muchos → min_rest_prox=2000 y max_rest_prox=3000
(defrule regla_rest_cerca_muchos
    (museo (cantidad_rest_cerca "muchos"))
    =>
    (assert (museo (min_rest_prox 2000) (max_rest_prox 3000)))
)

# Si cantidad_rest_cerca=demasiados → min_rest_prox=3000 y max_rest_prox=10000
(defrule regla_rest_cerca_demasiados
    (museo (cantidad_rest_cerca "demasiados"))
    =>
    (assert (museo (min_rest_prox 3000) (max_rest_prox 10000)))
)


# Sobre atracciones cercanas
# Si cantidad_atrac_cerca=ningun → min_atracciones=0 y max_atracciones=0
(defrule regla_atrac_cerca_ningun
    (museo (cantidad_atrac_cerca "ningun"))
    =>
    (assert (museo (min_atracciones 0) (max_atracciones 0)))
)

# Si cantidad_atrac_cerca=pocos → min_atracciones=0 y max_atracciones=100
(defrule regla_atrac_cerca_pocos
    (museo (cantidad_atrac_cerca "pocos"))
    =>
    (assert (museo (min_atracciones 0) (max_atracciones 100)))
)

# Si cantidad_atrac_cerca=algunos → min_atracciones=100 y max_atracciones=200
(defrule regla_atrac_cerca_algunos
    (museo (cantidad_atrac_cerca "algunos"))
    =>
    (assert (museo (min_atracciones 100) (max_atracciones 200)))
)

# Si cantidad_atrac_cerca=muchos → min_atracciones=200 y max_atracciones=300
(defrule regla_atrac_cerca_muchos
    (museo (cantidad_atrac_cerca "muchos"))
    =>
    (assert (museo (min_atracciones 200) (max_atracciones 300)))
)

# Si cantidad_atrac_cerca=demasiados → min_atracciones=300 y max_atracciones=10000
(defrule regla_atrac_cerca_demasiados
    (museo (cantidad_atrac_cerca "demasiados"))
    =>
    (assert (museo (min_atracciones 300) (max_atracciones 10000)))
)


# 3. Regla general
# Si (distrito=distrito_especificado o distrito=no relevante) y 
# [(dia_especificado=dia_atencion) y (ha_inicio≤hora_especificada≤ha_fin)] o [(dia_especificado=no relevante) o (hora_especificada=no relevante)] o [(dia_especificado=dia_atencion) y (hora_especificada=no relevante)] o [(dia_especificado=no relevante) y (ha_inicio≤hora_especificada≤ha_fin)] y 
# (categoria=categoria_especificada o categoria=no relevante) y 
# {[(concurrencia=relevante) y (dia_especificado≠dia_concurrido)] y [(hora_especificada<hc_inicio o hora_especificada>hc_fin)] o concurrencia=no relevante} y
# [(min_tarifa=0 y max_tarifa=0 y tarifa_normal=min_tarifa) o (min_tarifa<tarifa_normal≤max_tarifa) o tarifa_usuario=no relevante] y
# (min_puntaje≤puntaje_reseña<max_puntaje o reseña_usuario=no relevante) y 
# {[descuento_niños=True y (tarifa_ninos<tarifa_normal)] o descuento_niños=no relevante} y 
# {[descuento_ancianos=True y (tarifa_ancianos<tarifa_normal)] o descuento_ancianos=no relevante} y 
# {[descuento_discapacitados=True y (tarifa_discapacitados<tarifa_normal)] o descuento_discapacitados=no relevante} y
# [(servicio_restaurante_usuario=servicio_restaurante) o (servicio_restaurante_usuario=no relevante) o (servicio_cafeteria_usuario=servicio_cafeteria) o (servicio_cafeteria_usuario=no relevante)] y 
# [(reserva_entrada=True y reserva_entrada=reserva) o reserva_entrada=no relevante] y
# [(estacionamiento_usuario=True y estacionamiento_usuario=estacionamiento) o estacionamiento_usuario=no relevante] y 
# [(venta_objetos_usuario=True y venta_objetos_usuario=venta_objetos) o venta_objetos_usuario=no relevante] y 
# [(permiso_foto_usuario=True y permiso_foto_usuario=permiso_foto) o permiso_foto_usuario=no relevante] y 
# [(accesibilidad_usuario=True y accesibilidad_usuario=accesibilidad) o accesibilidad_usuario=no relevante] y 
# [(servicio_guiado_usuario=True y servicio_guiado_usuario=servicio_guiado) o servicio_guiado_usuario=no relevante] y 
# [(visita_virtual_usuario=True y visita_virtual_usuario=visita_virtual) o visita_virtual_usuario=no relevante] y
# [(servicio_biblioteca_usuario=True y servicio_biblioteca_usuario=servicio_biblioteca) o servicio_biblioteca_usuario=no relevante] y
# [(pag_facebook_existe=True y pag_facebook no está vacío) o (pag_instagram_existe=True y pag_instagram no está vacío) o (pag_tiktok_existe=True y pag_tiktok no está vacío) o (pag_facebook_existe=no relevante) o (pag_instagram_existe=no relevante) o (pag_tiktok_existe=no relevante)]
# [(telefono_existe=True y telefono no está vacío) o (email_existe=True o email no está vacío) o (telefono=no relevante) o (email=no relevante)] y 
# [(sitio_web_existe=True o sitio_web no está vacío) o (sitio_web=no relevante)] y 
# {[(min_rest_prox=0 y max_rest_prox=0 y n_restaurantes_prox=min_rest_prox) o (min_rest_prox<n_restaurantes_prox≤max_rest_prox)] o cantidad_rest_cerca=no relevante} y
# {[(min_atracciones=0 y max_atracciones=0 y n_atracciones_prox=min_atracciones) o (min_atracciones<n_atracciones_prox≤max_atracciones)] o cantidad_atrac_cerca=no relevante} y
# → nombre_museo


(defrule regla_general
   (museo
      (distrito_especificado ?distrito_especificado)
      (distrito ?distrito)
      (dia_especificado ?dia_especificado)
      (dia_atencion ?dia_atencion)
      (hora_especificada ?hora_especificada)
      (ha_inicio ?ha_inicio)
      (ha_fin ?ha_fin)
      (categoria_especificada ?categoria_especificada)
      (categoria ?categoria)
      (concurrencia ?concurrencia)
      (dia_concurrido ?dia_concurrido)
      (hc_inicio ?hc_inicio)
      (hc_fin ?hc_fin)
      (tarifa_usuario ?tarifa_usuario)
      (min_tarifa ?min_tarifa)
      (max_tarifa ?max_tarifa)
      (tarifa_normal ?tarifa_normal)
      (resena_usuario ?resena_usuario)
      (min_puntaje ?min_puntaje)
      (max_puntaje ?max_puntaje)
      (puntaje_resena ?puntaje_resena)
      (descuento_ninos ?descuento_ninos)
      (tarifa_ninos ?tarifa_ninos)
      (descuento_ancianos ?descuento_ancianos)
      (tarifa_ancianos ?tarifa_ancianos)
      (descuento_discapacitados ?descuento_discapacitados)
      (tarifa_discapacitados ?tarifa_discapacitados)
      (servicio_restaurante_usuario ?servicio_restaurante_usuario)
      (servicio_restaurante ?servicio_restaurante)
      (servicio_cafeteria_usuario ?servicio_cafeteria_usuario)
      (servicio_cafeteria ?servicio_cafeteria)
      (reserva_entrada ?reserva_entrada)
      (reserva ?reserva)
      (estacionamiento_usuario ?estacionamiento_usuario)
      (estacionamiento ?estacionamiento)
      (venta_objetos_usuario ?venta_objetos_usuario)
      (venta_objetos ?venta_objetos)
      (permiso_foto_usuario ?permiso_foto_usuario)
      (permiso_foto ?permiso_foto)
      (accesibilidad_usuario ?accesibilidad_usuario)
      (accesibilidad ?accesibilidad)
      (servicio_guiado_usuario ?servicio_guiado_usuario)
      (servicio_guiado ?servicio_guiado)
      (visita_virtual_usuario ?visita_virtual_usuario)
      (visita_virtual ?visita_virtual)
      (servicio_biblioteca_usuario ?servicio_biblioteca_usuario)
      (servicio_biblioteca ?servicio_biblioteca)
      (pag_facebook_existe ?pag_facebook_existe)
      (pag_facebook ?pag_facebook)
      (pag_instagram_existe ?pag_instagram_existe)
      (pag_instagram ?pag_instagram)
      (pag_tiktok_existe ?pag_tiktok_existe)
      (pag_tiktok ?pag_tiktok)
      (telefono_existe ?telefono_existe)
      (telefono ?telefono)
      (email_existe ?email_existe)
      (email ?email)
      (sitio_web_existe ?sitio_web_existe)
      (sitio_web ?sitio_web)
      (cantidad_rest_cerca ?cantidad_rest_cerca)
      (min_rest_prox ?min_rest_prox)
      (max_rest_prox ?max_rest_prox)
      (n_restaurantes_prox ?n_restaurantes_prox)
      (cantidad_atrac_cerca ?cantidad_atrac_cerca)
      (min_atracciones ?min_atracciones)
      (max_atracciones ?max_atracciones)
      (n_atracciones_prox ?n_atracciones_prox))

   ;; Condiciones para el distrito
   (or (eq ?distrito_especificado ?distrito)
       (eq ?distrito_especificado "no relevante"))

   ;; Condiciones para el día y la hora de atención
   (or (and (eq ?dia_especificado ?dia_atencion)
            (<= ?ha_inicio ?hora_especificada ?ha_fin))
       (eq ?dia_especificado "no relevante")
       (eq ?hora_especificada "no relevante"))

   ;; Condiciones para la categoría
   (or (eq ?categoria_especificada ?categoria)
       (eq ?categoria_especificada "no relevante"))

   ;; Condiciones para la concurrencia
   (or (and (eq ?concurrencia "relevante")
            (neq ?dia_especificado ?dia_concurrido)
            (or (< ?hora_especificada ?hc_inicio)
                (> ?hora_especificada ?hc_fin)))
       (eq ?concurrencia "no relevante"))

   ;; Condiciones para la tarifa
   (or (and (eq ?min_tarifa 0)
            (eq ?max_tarifa 0)
            (eq ?tarifa_normal ?min_tarifa))
       (and (< ?min_tarifa ?tarifa_normal)
            (<= ?tarifa_normal ?max_tarifa))
       (eq ?tarifa_usuario "no relevante"))

   ;; Condiciones para la reseña
   (or (and (<= ?min_puntaje ?puntaje_resena)
            (< ?puntaje_resena ?max_puntaje))
       (eq ?resena_usuario "no relevante"))

   ;; Condiciones para descuentos (niños, ancianos, discapacitados)
   (or (and (eq ?descuento_ninos "True")
            (< ?tarifa_ninos ?tarifa_normal))
       (eq ?descuento_ninos "no relevante"))

   ;; Agregar más condiciones según la lógica de "relevante/no relevante"
   ;; ...

   =>
   ;; Acción desencadenada al cumplir las condiciones
   (assert (museo (nombre_museo ?nombre_museo)))
)






(defrule regla_general
    (museo (distrito distrito_especificado) (distrito "no relevante")
           (dia_atencion dia_especificado) (dia_atencion ?dia_atencion)
           (hora_especificada ?hora_especificada) (ha_inicio ?ha_inicio) (ha_fin ?ha_fin)
           (categoria_especificada ?categoria_especificada) (categoria ?categoria)
           (concurrencia ?concurrencia) (dia_concurrido ?dia_concurrido) (hc_inicio ?hc_inicio) (hc_fin ?hc_fin)
           (tarifa_usuario ?tarifa_usuario) (min_tarifa ?min_tarifa) (max_tarifa ?max_tarifa) (tarifa_normal ?tarifa_normal)
           (resena_usuario ?resena_usuario) (min_puntaje ?min_puntaje) (max_puntaje ?max_puntaje) (puntaje_resena ?puntaje_resena)
           (descuento_ninos ?descuento_ninos) (tarifa_ninos ?tarifa_ninos)
           (descuento_ancianos ?descuento_ancianos) (tarifa_ancianos ?tarifa_ancianos)
           (descuento_discapacitados ?descuento_discapacitados) (tarifa_discapacitados ?tarifa_discapacitados)
           (servicio_restaurante_usuario ?servicio_restaurante_usuario) (servicio_restaurante ?servicio_restaurante)
           (servicio_cafeteria_usuario ?servicio_cafeteria_usuario) (servicio_cafeteria ?servicio_cafeteria)
           (reserva_entrada ?reserva_entrada) (reserva ?reserva)
           (estacionamiento_usuario ?estacionamiento_usuario) (estacionamiento ?estacionamiento)
           (venta_objetos_usuario ?venta_objetos_usuario) (venta_objetos ?venta_objetos)
           (permiso_foto_usuario ?permiso_foto_usuario) (permiso_foto ?permiso_foto)
           (accesibilidad_usuario ?accesibilidad_usuario) (accesibilidad ?accesibilidad)
           (servicio_guiado_usuario ?servicio_guiado_usuario) (servicio_guiado ?servicio_guiado)
           (visita_virtual_usuario ?visita_virtual_usuario) (visita_virtual ?visita_virtual)
           (servicio_biblioteca_usuario ?servicio_biblioteca_usuario) (servicio_biblioteca ?servicio_biblioteca)
           (pag_facebook_existe ?pag_facebook_existe) (pag_facebook ?pag_facebook)
           (pag_instagram_existe ?pag_instagram_existe) (pag_instagram ?pag_instagram)
           (pag_tiktok_existe ?pag_tiktok_existe) (pag_tiktok ?pag_tiktok)
           (existencia_medios_comunicacion ?existencia_medios_comunicacion)
           (telefono_existe ?telefono_existe) (telefono ?telefono)
           (email_existe ?email_existe) (email ?email)
           (sitio_web_existe ?sitio_web_existe) (sitio_web ?sitio_web)
           (cantidad_rest_cerca ?cantidad_rest_cerca) (min_rest_prox ?min_rest_prox) (max_rest_prox ?max_rest_prox) (n_restaurantes_prox ?n_restaurantes_prox)
           (cantidad_atrac_cerca ?cantidad_atrac_cerca) (min_atracciones ?min_atracciones) (max_atracciones ?max_atracciones) (n_atracciones_prox ?n_atracciones_prox)
    =>
    assert (museo (nombre_museo ?nombre_museo))
    
#(printout t "Nombre del museo recomedado: " ?nombre_museo crlf)
