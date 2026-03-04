"""
Ejemplo de uso programático de la librería sysadmin_utils.
Este script muestra cómo importar usar las herramientas en tus propios scripts.
"""

from sysadmin_utils.security import password_manager
from sysadmin_utils.system import formatting
from pathlib import Path

def main():
    print("--- Demo SysAdmin Utils ---")

    # 1. Generar una contraseña
    print("\n[Security] Generando contraseña para nueva DB...")
    db_pass = password_manager.generate_password(length=24)
    print(f"Password: {db_pass}")

    # 2. Simular organización de una carpeta
    dummy_dir = Path("dummy_downloads")
    dummy_dir.mkdir(exist_ok=True)
    (dummy_dir / "foto.jpg").touch()
    (dummy_dir / "documento.pdf").touch()
    
    print(f"\n[System] Organizando {dummy_dir}...")
    formatting.organize_directory(dummy_dir, verbose=True)
    
    # Limpieza (opcional, para el demo)
    import shutil
    shutil.rmtree(dummy_dir)
    print("\n[Demo] Limpieza completada.")

if __name__ == "__main__":
    main()
