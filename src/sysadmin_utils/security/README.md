# Security Utils

Este módulo contiene herramientas enfocadas en la seguridad del sistema y el manejo de credenciales.

## Módulos

### `password_manager.py`
Generador de contraseñas criptográficamente seguras.
- Usa `secrets` (CSPRNG) en lugar de `random`.
- Permite personalizar longitud y uso de símbolos.

**Uso desde código:**
```python
from sysadmin_utils.security import password_manager
pwd = password_manager.generate_password(length=20)
```

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py gen-pass -l 20
```

### `malware_scanner.py`
Escáner básico de malware basado en firmas (hashes SHA-256).
- Compara archivos contra una lista de hashes conocidos.
- Escanea directorios de forma recursiva.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py scan-malware "C:/Ruta/A/Escanear"
```

### `hash_utils.py`
Utilidades para cálculo y verificación de integridad de archivos.
- Soporta SHA-256 y MD5.
- Permite verificar si un archivo está en una lista negra de hashes.

**Uso desde CLI:**
```bash
python src/sysadmin_utils/main.py hash-check "archivo.exe"
```
