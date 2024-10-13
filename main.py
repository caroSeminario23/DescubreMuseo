from frontend.capturar_preferencias import capturar_preferencias
from frontend.guardar_preferencias import generar_hecho_preferencia_clips, guardar_hecho_preferencia_clips
from backend.procesamiento.hechos_todos_museos import convertir_museos_hechos
from backend.procesamiento.cargar_reglas_hechos import cargar_clips
from backend.procesamiento.identificar_recomendaciones import identificar_recomendaciones
from backend.procesamiento.buscar_museos_recomendados import mostrar_opciones_museos_recomendados

'''# Convertir los museos en hechos
convertir_museos_hechos()'''

'''# Ejemplo de uso
preferencias_usuario = capturar_preferencias()

# Imprimir las preferencias capturadas por el usuario línea por línea si es que está guardado como un diccionario
print("\nPreferencias del usuario:\n")
if isinstance(preferencias_usuario, dict):
    for key, value in preferencias_usuario.items():
        print(f"{key}: {value}")

# Generar el hecho en formato CLIPS
hecho_clips = generar_hecho_preferencia_clips(preferencias_usuario)

# Guardar el hecho en un archivo .clp
guardar_hecho_preferencia_clips(hecho_clips)
print("\nHecho guardado correctamente")'''

# Cargar los hechos y reglas en CLIPS
museos_recomendados = identificar_recomendaciones()

if museos_recomendados == []:
    print("No se encontraron museos recomendados")
    print("Por favor, intenta con otras preferencias")
    print("Gracias por usar nuestro sistema")
else:
    # Imprimir los museos recomendados
    mostrar_opciones_museos_recomendados(museos_recomendados)

    print("\n\nProceso finalizado")