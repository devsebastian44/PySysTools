import os
import time
from pathlib import Path


def monitor_changes(folder_path: Path, log_file: Path):
    """
    Logs files and directories in a folder to a log file.
    """
    folder_path = Path(folder_path)
    log_file = Path(log_file)

    if not folder_path.exists():
        print(f"Folder not found: {folder_path}")
        return

    # Verificar si el archivo de registro existe
    if not log_file.exists():
        log_file.touch()

    # Obtener la fecha y hora actual
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    print(f"Logging changes for {folder_path} to {log_file}...")

    # Abrir el archivo de registro en modo de escritura (append)
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'--- Estado de carpeta {folder_path} ({current_time}) ---\n')

        # Recorrer los archivos y subcarpetas de la carpeta
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                mod_time = os.path.getmtime(file_path)
                fmt_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
                f.write(f'Archivo: {file_path} ({fmt_time})\n')

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                mod_time = os.path.getmtime(dir_path)
                fmt_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
                f.write(f'Carpeta: {dir_path} ({fmt_time})\n')

        f.write('\n')


if __name__ == "__main__":
    # Example usage
    monitor_changes(Path("."), Path("changes.log"))
