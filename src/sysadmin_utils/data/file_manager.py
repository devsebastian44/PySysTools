import tkinter as tk  # Biblioteca para crear interfaces gráficas de usuario.
from tkinter import filedialog  # Módulo de tkinter para cuadros de diálogo.


# Función para abrir un cuadro de diálogo para seleccionar un archivo.
# Permite al usuario elegir un archivo desde su sistema de archivos.
def abrir_archivo():
    archivo = filedialog.askopenfilename(
        initialdir="/",  # Directorio inicial para mostrar.
        title="Seleccionar archivo",  # Título del cuadro de diálogo.
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))  # Filtros para tipos de archivo.
    )
    print("Archivo seleccionado:", archivo)  # Imprime la ruta del archivo seleccionado.


# Función para abrir un cuadro de diálogo para seleccionar un directorio.
# Permite al usuario elegir una carpeta desde su sistema de archivos.
def abrir_directorio():
    directorio = filedialog.askdirectory(
        initialdir="/",  # Directorio inicial para mostrar.
        title="Seleccionar directorio"  # Título del cuadro de diálogo.
    )
    print("Directorio seleccionado:", directorio)  # Imprime la ruta del directorio seleccionado.


# Crear la ventana principal de la aplicación.
ventana = tk.Tk()  # Inicializa la ventana principal.
ventana.title("Gestor de archivos")  # Título de la ventana.

# Botón para abrir el cuadro de diálogo de selección de archivo.
boton_archivo = tk.Button(
    ventana,  # Ventana en la que se coloca el botón.
    text="Seleccionar archivo",  # Texto que muestra el botón.
    command=abrir_archivo  # Función que se ejecutará al hacer clic.
)
boton_archivo.pack()  # Agrega el botón a la ventana.

# Botón para abrir el cuadro de diálogo de selección de directorio.
boton_directorio = tk.Button(
    ventana,  # Ventana en la que se coloca el botón.
    text="Seleccionar directorio",  # Texto que muestra el botón.
    command=abrir_directorio  # Función que se ejecutará al hacer clic.
)
boton_directorio.pack()  # Agrega el botón a la ventana.

# Ejecuta el bucle principal de la aplicación.
ventana.mainloop()  # Mantiene abierta la ventana hasta que se cierre.