import os
import time
import datetime


def modificar_fecha_carpeta(ruta_carpeta, nueva_fecha):
    """
    Modifies the access and modification time of a file or folder.
    """
    # Convierte la nueva fecha en formato de tiempo de época (timestamp).
    nueva_fecha_tiempo = time.mktime(nueva_fecha.timetuple())

    # Modifica la fecha de acceso y modificación de la carpeta o archivo.
    os.utime(ruta_carpeta, (nueva_fecha_tiempo, nueva_fecha_tiempo))
    print("Fecha de creación modificada con éxito.")


if __name__ == "__main__":
    # Example usage
    # Ruta actual del archivo o carpeta.
    ruta = 'D:\\Descargas\\Carpeta'
    # Nueva fecha de creación (ejemplo: 4 de junio de 2023 a las 10:19 PM).
    fecha = datetime.datetime(2023, 6, 4, 22, 19)
    
    if os.path.exists(ruta):
        modificar_fecha_carpeta(ruta, fecha)
    else:
        print(f"Path not found: {ruta}")
