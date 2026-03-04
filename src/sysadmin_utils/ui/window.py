import tkinter as tk


def create_simple_window():
    """Creates a basic GUI window."""
    ventana = tk.Tk()
    ventana.title("Hola Mundo")
    ventana.geometry("400x300")
    ventana.mainloop()


if __name__ == "__main__":
    create_simple_window()
