import tkinter as tk
from tkinter import filedialog


# Función para abrir un cuadro de diálogo para seleccionar un archivo.
# Permite al usuario elegir un archivo desde su sistema de archivos.
def abrir_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        initialdir="./",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    print("Archivo seleccionado:", archivo)


# Función para abrir un cuadro de diálogo para seleccionar un directorio.
# Permite al usuario elegir una carpeta desde su sistema de archivos.
def abrir_directorio():
    directorio = filedialog.askdirectory(
        title="Seleccionar carpeta",
        initialdir="./"
    )
    print("Directorio seleccionado:", directorio)


# Crear la ventana principal de la aplicación.
ventana = tk.Tk()
ventana.title("Gestor de archivos")
ventana.geometry("300x200")

# Crear botones para abrir archivos y directorios.
btn_archivo = tk.Button(
    ventana,
    text="Abrir archivo",
    command=abrir_archivo
)
btn_archivo.pack(pady=20)

btn_directorio = tk.Button(
    ventana,
    text="Abrir carpeta",
    command=abrir_directorio
)
btn_directorio.pack(pady=20)


if __name__ == "__main__":
    ventana.mainloop()
