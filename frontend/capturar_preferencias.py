def capturar_preferencias():
    print("\n=============================================================================")
    print("**----Bienvenido a DescubreMuseo: El sistema de recomendación de museos---**")
    print("=============================================================================")
    print("\nPor favor, complete el siguiente cuestionario (21 preguntas) para obtener recomendaciones personalizadas")
    
    # Capturamos las preferencias del usuario
    print("\n1. Ingrese el distrito preferido:")
    distrito_especificado = opciones_distritos()

    print("\n2. Ingrese el día de la semana que desea visitar el museo: ")
    dia_especificado = opciones_dia()

    print("\n3. Ingrese la hora aproximada en la que desea visitar el museo: ")
    hora_especificada = opciones_hora()
    
    print("\n4. Ingrese la categoría de museo preferida: ")
    categoria_seleccionada = opciones_categoria()

    print("\n5. Indique si le interesa la concurrencia de visitantes en la hora seleccionada: ")
    concurrencia = opciones_concurrencia()
    
    print("\n6. Ingrese la tarifa que le interesa: ")
    tarifa_usuario = opciones_tarifa()

    print("\n7. Ingrese el rango de valoración del museo que le interesa: ")
    resena_usuario = opciones_resena()

    print("\n8. Indique si le interesa el descuento de la tarifa para niños: ")
    descuento_ninos = opciones_descuento_ninos()

    print("\n9. Indique si le interesa el descuento de la tarifa para ancianos: ")
    descuento_ancianos = opciones_descuento_ancianos()

    print("\n10. Indique si le interesa el descuento de la tarifa para discapacitados: ")
    descuento_discapacitados = opciones_descuento_discapacitados()

    #print("\n11. Indique si le interesa la disponibilidad de comida: ")
    #comida_disponible = opciones_comida_disponible()

    print("\n11. Indique si le interesa la facilidad de reservar su entrada con anticipación: ")
    reserva_usuario = opciones_reserva()

    print("\n12. Indique si le interesa la disponibilidad de estacionamiento: ")
    estacionamiento_usuario = opciones_estacionamiento()

    print("\n13. Indique si le interesa la disponibilidad de venta de objetos: ")
    venta_objetos_usuario = opciones_venta_objetos()

    print("\n14. Indique si le interesa el permiso para tomar fotos: ")
    permiso_foto_usuario = opciones_permiso_foto()

    print("\n15. Indique si le interesa que el museo cuente con medidas de accesibilidad para personas discapacitadas: ")
    accesibilidad_usuario = opciones_accesibilidad()

    print("\n16. Indique si le interesa la disponibilidad del servicio de guiado: ")
    servicio_guiado_usuario = opciones_servicio_guiado()

    print("\n17. Indique si le interesa la disponibilidad de visita virtual: ")
    visita_virtual_usuario = opciones_visita_virtual()

    print("\n18. Indique si le interesa la disponibilidad de una biblioteca: ")
    servicio_biblioteca_usuario = opciones_servicio_biblioteca()

    #print("\n20. Indique si le interesa la presencia del museo en las redes sociales: ")
    #presencia_redes_sociales = opciones_presencia_redes_sociales()

    #print("\n21. Indique si le interesa la existencia de medios para contactar al museo: ")
    #existencia_medios_comunicacion = opciones_existencia_medios_comunicacion()

    print("\n19. Indique si le interesa la disposición de un sitio web: ")
    sitio_web_existe = opciones_sitio_web()

    print("\n20. Indique si le interesa el número de restaurantes cerca: ")
    cantidad_rest_cerca = opciones_cantidad_restaurantes_cerca()

    print("\n21. Indique si le interesa el número de atracciones cerca: ")
    cantidad_atrac_cerca = opciones_cantidad_atracciones_cerca()
    
    # Almacenamos las preferencias en un diccionario o una lista
    preferencias = {
        'distrito_especificado': distrito_especificado,
        'dia_especificado': dia_especificado,
        'hora_especificada': hora_especificada,
        'categoria_especificada': categoria_seleccionada,
        'concurrencia': concurrencia,
        'tarifa_usuario': tarifa_usuario,
        'resena_usuario': resena_usuario,
        'descuento_ninos': descuento_ninos,
        'descuento_ancianos': descuento_ancianos,
        'descuento_discapacitados': descuento_discapacitados,
        #'comida_disponible': comida_disponible,
        'reserva_usuario': reserva_usuario,
        'estacionamiento_usuario': estacionamiento_usuario,
        'venta_objetos_usuario': venta_objetos_usuario,
        'permiso_foto_usuario': permiso_foto_usuario,
        'accesibilidad_usuario': accesibilidad_usuario,
        'servicio_guiado_usuario': servicio_guiado_usuario,
        'visita_virtual_usuario': visita_virtual_usuario,
        'servicio_biblioteca_usuario': servicio_biblioteca_usuario,
        #'presencia_redes_sociales': presencia_redes_sociales,
        #'existencia_medios_comunicacion': existencia_medios_comunicacion,
        'sitio_web_existe': sitio_web_existe,
        'cantidad_rest_cerca': cantidad_rest_cerca,
        'cantidad_atrac_cerca': cantidad_atrac_cerca
    }

    return preferencias


def opciones_distritos():
    distritos = {
        '1': 'Ate',
        '2': 'Barranco',
        '3': 'Callao',
        '4': 'Cercado de Lima',
        '5': 'Chorrillos',
        '6': 'Jesus María',
        '7': 'La Molina',
        '8': 'Lurin',
        '9': 'Miraflores',
        '10': 'Pueblo Libre',
        '11': 'San Borja',
        '12': 'San Isidro',
        '13': 'Surco',
        '14': 'No relevante'
    }

    print("Seleccione un distrito:")
    for key, value in distritos.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in distritos.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if distritos[opcion] != 'No relevante':
        distritos[opcion] = f'"{distritos[opcion]}"'
    else:
        distritos[opcion] = 'No_relevante'

    # Retornar el nombre del distrito seleccionado
    return distritos[opcion]


def opciones_dia():
    dias = {
        '1': 'Lunes',
        '2': 'Martes',
        '3': 'Miércoles',
        '4': 'Jueves',
        '5': 'Viernes',
        '6': 'Sábado',
        '7': 'Domingo',
        '8': 'No relevante'
    }

    print("Seleccione un día de la semana:")
    for key, value in dias.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in dias.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if dias[opcion] != 'No relevante':
        dias[opcion] = dias[opcion]
        #dias[opcion] = f'"{dias[opcion]}"'
    else:
        dias[opcion] = 'No_relevante'

    # Retornar el nombre del día seleccionado
    return dias[opcion]


def opciones_hora():
    horas = {
        '1': '08:00',
        '2': '09:00',
        '3': '10:00',
        '4': '11:00',
        '5': '12:00',
        '6': '13:00',
        '7': '14:00',
        '8': '15:00',
        '9': '16:00',
        '10': '17:00',
        '11': '18:00',
        '12': '19:00',
        '13': '20:00',
        '14': '21:00',
        '15': 'No relevante'
    }

    print("Seleccione una hora:")
    for key, value in horas.items():
        print(f"{key}. {value}")
    
    opcion = input("Ingrese el número de su elección: ")
    
    # Validar que la opción ingresada sea válida
    while opcion not in horas.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Guardar el número de la opción seleccionada. Por ejemplo: Si se tiene '10:00', se guarda 10
    if horas[opcion] != 'No relevante':
        horas[opcion] = str(int(horas[opcion][:2]))
    else:
        horas[opcion] = 'No_relevante'

    # Retornar la hora seleccionada
    return horas[opcion]
    

def opciones_categoria():
    categorias = {
        '1': 'Tématico',
        '2': 'Arqueológico',
        '3': 'Arte',
        '4': 'Histórico',
        '5': 'No relevante'
    }

    print("Seleccione una categoría de museo:")
    for key, value in categorias.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in categorias.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")
        
    # Agregar comillas dobles a la opción seleccionada
    if categorias[opcion] != 'No relevante':
        categorias[opcion] = categorias[opcion]
        #categorias[opcion] = f'"{categorias[opcion]}"'
    else:
        categorias[opcion] = 'No_relevante'

    # Retornar el nombre de la categoría seleccionada
    return categorias[opcion]


def opciones_concurrencia():
    concurrencia = {
        '1': 'Si',
        '2': 'No',
    }

    print("Seleccione una opción:")
    for key, value in concurrencia.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in concurrencia.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if concurrencia[opcion] == 'Si' else 'No_relevante'


def opciones_tarifa():
    tarifas = {
        '1': 'Nula',
        '2': 'Barata',
        '3': 'Media',
        '4': 'Alta',
        '5': 'Muy alta',
        '6': 'No relevante'
    }
    
    print("Seleccione una tarifa:")
    for key, value in tarifas.items():
        print(f"{key}. {value}")
        
    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in tarifas.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if tarifas[opcion] != 'No relevante':
        tarifas[opcion] = f'"{tarifas[opcion]}"'
    else:
        tarifas[opcion] = 'No_relevante'

    # Retornar el rango de tarifa seleccionado
    return tarifas[opcion]


def opciones_resena():
    resenas = {
        '1': 'Negativa',
        '2': 'Neutral',
        '3': 'Positiva',
        '4': 'Muy positiva',
        '5': 'No relevante'
    }

    print("Seleccione una reseña:")
    for key, value in resenas.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in resenas.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if resenas[opcion] != 'No relevante':
        resenas[opcion] = f'"{resenas[opcion]}"'
    else:
        resenas[opcion] = 'No_relevante'

    # Retornar la reseña seleccionada
    return resenas[opcion]


def opciones_descuento_ninos():
    descuentos_ninos = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in descuentos_ninos.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in descuentos_ninos.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if descuentos_ninos[opcion] == 'Si' else 'No_relevante'


def opciones_descuento_ancianos():
    descuentos_ancianos = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in descuentos_ancianos.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in descuentos_ancianos.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if descuentos_ancianos[opcion] == 'Si' else 'No_relevante'


def opciones_descuento_discapacitados():
    descuentos_discapacitados = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in descuentos_discapacitados.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in descuentos_discapacitados.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if descuentos_discapacitados[opcion] == 'Si' else 'No_relevante'


def opciones_comida_disponible():
    comidas = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in comidas.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in comidas.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if comidas[opcion] == 'Si' else 'No_relevante'


def opciones_reserva():
    reservas = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in reservas.items():
        print(f"{key}. {value}")
        
    opcion = input("Ingrese el número de su elección: ")

    #Validar que la opción ingresada sea válida
    while opcion not in reservas.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")
        
    #Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if reservas[opcion] == 'Si' else 'No_relevante'


def opciones_estacionamiento():
    estacionamientos = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in estacionamientos.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")
    
    # Validar que la opción ingresada sea válida
    while opcion not in estacionamientos.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if estacionamientos[opcion] == 'Si' else 'No_relevante'
    

def opciones_venta_objetos():
    venta_objetos = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in venta_objetos.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in venta_objetos.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if venta_objetos[opcion] == 'Si' else 'No_relevante'


def opciones_permiso_foto():
    permiso_foto = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in permiso_foto.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in permiso_foto.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if permiso_foto[opcion] == 'Si' else 'No_relevante'


def opciones_accesibilidad():
    accesibilidad = {
        '1': 'Si',
        '2': 'No'
    }    

    print("Seleccione una opción:")
    for key, value in accesibilidad.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in accesibilidad.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if accesibilidad[opcion] == 'Si' else 'No_relevante'

    
def opciones_servicio_guiado():
    servicio_guiado = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in servicio_guiado.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")
    
    # Validar que la opción ingresada sea válida
    while opcion not in servicio_guiado.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if servicio_guiado[opcion] == 'Si' else 'No_relevante'


def opciones_visita_virtual():
    visita_virtual = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in visita_virtual.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in visita_virtual.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if visita_virtual[opcion] == 'Si' else 'No_relevante'


def opciones_servicio_biblioteca():
    servicio_biblioteca = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in servicio_biblioteca.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in servicio_biblioteca.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if servicio_biblioteca[opcion] == 'Si' else 'No_relevante'


def opciones_presencia_redes_sociales():
    redes_sociales = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in redes_sociales.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")
    
    # Validar que la opción ingresada sea válida
    while opcion not in redes_sociales.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if redes_sociales[opcion] == 'Si' else 'No_relevante'


def opciones_existencia_medios_comunicacion():
    medios_comunicacion = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in medios_comunicacion.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in medios_comunicacion.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'Relevante' if medios_comunicacion[opcion] == 'Si' else 'No_relevante'


def opciones_sitio_web():
    sitios_web = {
        '1': 'Si',
        '2': 'No'
    }

    print("Seleccione una opción:")
    for key, value in sitios_web.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in sitios_web.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Retornar Retornar Relevante si la opción es 1, No relevante si la opción es 2
    return 'TRUE' if sitios_web[opcion] == 'Si' else 'No_relevante'


def opciones_cantidad_restaurantes_cerca():
    restaurantes = {
        '1': 'Ninguno',
        '2': 'Pocos',
        '3': 'Algunos',
        '4': 'Muchos',
        '5': 'Demasiados',
        '6': 'No relevante'
    }

    print("Seleccione una opción:")
    for key, value in restaurantes.items():
        print(f"{key}. {value}")

    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in restaurantes.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if restaurantes[opcion] != 'No relevante':
        restaurantes[opcion] = f'"{restaurantes[opcion]}"'
    else:
        restaurantes[opcion] = 'No_relevante'

    # Retornar el nombre de la categoría seleccionada
    return restaurantes[opcion]


def opciones_cantidad_atracciones_cerca():
    cantidad_atracciones = {
        '1': 'Ninguno',
        '2': 'Pocos',
        '3': 'Algunos',
        '4': 'Muchos',
        '5': 'Demasiados',
        '6': 'No relevante'
    }
    
    print("Seleccione la cantidad de atracciones:")
    for key, value in cantidad_atracciones.items():
        print(f"{key}. {value}")
    
    opcion = input("Ingrese el número de su elección: ")

    # Validar que la opción ingresada sea válida
    while opcion not in cantidad_atracciones.keys():
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Ingrese el número de su elección: ")

    # Agregar comillas dobles a la opción seleccionada
    if cantidad_atracciones[opcion] != 'No relevante':
        cantidad_atracciones[opcion] = f'"{cantidad_atracciones[opcion]}"'
    else:
        cantidad_atracciones[opcion] = 'No_relevante'

    # Retornar el nombre de la cantidad de atracciones seleccionada
    return cantidad_atracciones[opcion]


# Ejemplo de uso
#preferencias_usuario = capturar_preferencias()
#print("Preferencias capturadas:", preferencias_usuario)