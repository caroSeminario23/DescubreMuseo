from capturar_preferencias import capturar_preferencias

# Ejemplo de uso
preferencias_usuario = capturar_preferencias()

# Imprimir las preferencias capturadas por el usuario línea por línea si es que
# está guardado como un diccionario

print("\nPreferencias del usuario:")
if isinstance(preferencias_usuario, dict):
    for key, value in preferencias_usuario.items():
        print(f"{key}: {value}")