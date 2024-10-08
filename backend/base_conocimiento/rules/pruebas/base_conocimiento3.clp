







; 2. Reglas intermedias

; Reglas sobre tarifa
; Si tarifa_usuario = nula → min_tarifa=0 y max_tarifa=0
(defrule regla_tarifa_nula
    (preferencias_usuario (tarifa_usuario "nula"))
    =>
    (assert (procesamiento_datos_museo (min_tarifa 0) (max_tarifa 0)))
)











(assert (datos_museo_solicitados (tarifa_usuario "nula")))


(facts) "Permite ver los hechos activos"
(rules) "Permite ver las reglas activas"
(run) "Permite ejecutar el sistema"
(agenda) "Permite ver las reglas activas"
(reset) "Permite reiniciar el sistema"
(clear) "Permite limpiar la pantalla"
(refresh) "Permite volver a solicitar una regla"
(ppdefrule) "Permite ver una regla"
(ppdeftemplate) "Permite ver una plantilla"
(ppdeffacts) "Permite ver los hechos"