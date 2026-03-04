# UI Utils

Componentes de interfaz de usuario y notificaciones.

## Módulos

### `notifications.py`
Sistema de notificaciones nativas de Windows (Toast).
- Usa `winotify`.
- Soporta iconos, sonidos y acciones (botones).

**Ejemplo de uso:**
```python
from sysadmin_utils.ui.notifications import send_notification

send_notification(
    title="Alerta de Sistema",
    message="El proceso ha finalizado correctamente.",
    action_label="Ver Logs",
    action_link="C:/Logs/app.log"
)
```

### `window.py`
Utilidades para creación de ventanas simples con Tkinter.

### `calendar_view.py`
Visualizador de calendario por consola.

### `screenshot.py`
Herramienta para captura de pantalla.

