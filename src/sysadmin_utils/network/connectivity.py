import requests


# Función que prueba la conexión a Internet
def test_internet_connection():
    try:
        # Intenta realizar una solicitud HTTP a Google
        requests.get("https://www.google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        # Si ocurre un error de conexión o timeout, imprime el mensaje de error
        print("Sin conexión a internet.")
    else:
        # Si la solicitud se realiza correctamente, imprime que hay conexión
        print("Con conexión a internet.")


if __name__ == "__main__":
    # Llama a la función para probar la conexión
    test_internet_connection()