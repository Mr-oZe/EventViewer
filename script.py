import os
import evtx

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Ruta de la carpeta EVTX (puedes modificarla según sea necesario)
directorio_evtx = os.path.join(directorio_actual, 'eventviewer')

# Recorrer el directorio de forma recursiva
for nombre_directorio, dirs, ficheros in os.walk(directorio_evtx):
    for nombre_fichero in ficheros:
        # Comprobar si el archivo tiene la extensión .evtx
        if nombre_fichero.endswith('.evtx'):
            ruta_completa = os.path.join(nombre_directorio, nombre_fichero)
            print(f"Leyendo archivo: {ruta_completa}")
            # Aquí puedes añadir el flujo de lectura del archivo EVTX
            with evtx.Evtx(ruta_completa) as log:
                for record in log.records():
                    print(record.xml())  # O cualquier otro procesamiento que necesites
        else:
            print(f"No es un archivo evtx: {nombre_fichero}")
