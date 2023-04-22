import datetime

# Función para obtener la fecha y hora actual en el formato deseado
def obtener_fecha_hora():
    now = datetime.datetime.now()
    fecha = now.strftime("%d/%m/%y, %H:%M:%S")
    return fecha

# Función para escribir en el archivo
def escribir_conversacion(usuario, mensaje):
    with open("conversaciones.txt", "a") as archivo:
        fecha_hora = obtener_fecha_hora()
        linea = f"[{fecha_hora}] {usuario}: {mensaje}\n"
        archivo.write(linea)

# Pedir al usuario que ingrese las conversaciones para "Usuario"
while True:
    mensaje = input("Usuario: ")
    escribir_conversacion("Usuario", mensaje)

    mensaje = input("Champella: ")
    escribir_conversacion("Champella", mensaje)
