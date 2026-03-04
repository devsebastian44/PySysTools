# PySysTools - Enterprise SysAdmin & Security Operations

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Ready-brightgreen)

## 🎯 Objetivo Técnico y Profesional

**PySysTools** es una suite modular y escalable diseñada para ingenieros de DevSecOps y Administradores de Sistemas. Su objetivo es automatizar operaciones de infraestructura, escanear vulnerabilidades y gestionar redes mediante un enfoque de **Seguridad por Diseño (Security by Design)**.
Este proyecto está orientado tanto para laboratorios privados de investigación y despliegues empresariales (utilizando GitLab como fuente de verdad y canalización de CI/CD), como para demostraciones públicas en portafolios (GitHub).

> **Enfoque Ético:** Las herramientas de seguridad incluidas (ej. escáneres de malware, analistas de hash) deben usarse de manera legal y ética. El autor no asume responsabilidad por el mal uso de las capacidades ofensivas/defensivas provistas.

## 🏛️ Arquitectura del Repositorio

La arquitectura sigue principios de Clean Code y está claramente estructurada para un enfoque Enterprise:

```text
/
├── configs/          # Configuraciones base y plantillas JSON/YAML (No sensibles)
├── data/             # Muestras CSV y estructuras de datos para tests
├── diagrams/         # Diagramas Mermaid (Arquitectura, Flujos)
├── docs/             # Documentación técnica extendida
├── examples/         # Ejemplos de integración de la librería
├── scripts/          # Automatizaciones operativas (incluye publish_public.ps1)
├── src/              # Código fuente principal de la suite
│   └── sysadmin_utils/
│       ├── data/     
│       ├── network/  
│       ├── security/ 
│       ├── system/   
│       ├── ui/       
│       └── utils/
├── tests/            # Suite de pruebas unitarias y de integración (Excluido de GitHub)
└── .gitlab-ci.yml    # Pipeline CI/CD Privado (Linting, Unit Testing, SAST)
```

## 🔄 Flujo DevSecOps y Separación de Entornos (GitLab -> GitHub)

Este repositorio emplea una estrategia avanzada de separación de entornos mitigando el riesgo de fuga de datos o exposición de componentes críticos:

### GitLab (Laboratorio Privado - Source of Truth)
En **GitLab** reside el entorno completo de trabajo. Esto incluye ramas de desarrollo, pruebas unitarias (`tests/`), scripts de integración privada, configuraciones reales, pipeline de CI/CD activo (`.gitlab-ci.yml`) y automatización profunda.

### GitHub (Portafolio Público Sanitizado)
En **GitHub (rama `public`)** reside la versión depurada y presentable. Se excluyen pruebas, infraestructura privada, secretos y configuraciones.

### `publish_public.ps1`: Automatización de Sanitización
El flujo oficial se apoya en el script `scripts/publish_public.ps1` que funciona como un guardián de publicación:
1. **Verificación & Limpieza:** Asegura que estemos en la rama principal limpios e indexa con GitLab.
2. **Aislamiento de Rama:** Crea una rama temporal (`public`).
3. **Purgado de Seguridad:** Elimina forzosamente carpetas críticas del caché del repositorio (`tests/`, `configs/`, CI interno) para que no sean expuestas.
4. **Despliegue GitHub:** Empuja esta versión completamente sanitizada (pero funcional a nivel demostrativo) de forma forzada a GitHub.
5. **Restauración:** Devuelve el espacio de trabajo local al estado de laboratorio privado intacto.


## 🚀 Instalación y Acceso

> [!IMPORTANT]
> El repositorio completo con todo el código funcional está disponible en **GitLab** para acceso completo.

https://gitlab.com/group-programming-lab/PySysTools.git

## 🚀 Uso General del CLI

El proyecto emplea un CLI orquestador:

```bash
# Instalación en el entorno
pip install -e .

# CLI General de Seguridad
sysadmin_utils gen-pass -l 20
sysadmin_utils scan-malware "C:/Downloads"

# Redes
sysadmin_utils net-monitor
```

## 🤝 Contribución
Las contribuciones se aceptan mediante PRs en la rama pública (o interna si tienes acceso al GitLab original). Se aplicará linter `flake8`, pruebas con `pytest` y revisión estática de seguridad (`bandit`).

## 📄 Licencia
Distribuido bajo la Licencia MIT.