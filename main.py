from frontend.capturar_preferencias import capturar_preferencias
from frontend.guardar_preferencias import generar_hecho_preferencia_clips, guardar_hecho_preferencia_clips

# Ejemplo de uso
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
print("\nHecho guardado correctamente")

