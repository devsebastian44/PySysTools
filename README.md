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

## 🔄 Flujo DevSecOps y Separación de Entornos (GitLab Laboratorio Público -> GitHub Portafolio)

Este repositorio emplea una estrategia de separación de entornos optimizada para diferentes casos de uso:

### GitLab (Laboratorio Público Completo)
En **GitLab** reside el entorno completo de trabajo con todo el código fuente. Este repositorio es público y funciona como el laboratorio principal donde se encuentra:
- Todo el código fuente completo y funcional
- Ramas de desarrollo y experimentación
- Pruebas unitarias y de integración (`tests/`)
- Scripts de automatización y configuraciones
- Pipeline de CI/CD activo (`.gitlab-ci.yml`)
- Documentación técnica completa
- Ejemplos de integración

### GitHub (Portafolio Optimizado)
En **GitHub** reside una versión optimizada para portafolio y demostraciones rápidas. Esta versión está diseñada para:
- Presentación profesional del proyecto
- Demostraciones ligeras sin dependencias complejas
- Acceso rápido a las funcionalidades principales
- Integración sencilla en otros proyectos

### Estrategia de Sincronización
El flujo mantiene ambos repositorios actualizados mediante:
1. **Desarrollo Principal:** Todo el trabajo se realiza en GitLab
2. **Publicación Automática:** Script `publish_public.ps1` sincroniza las versiones optimizadas
3. **Mantenimiento:** GitHub se mantiene como una vitrina del proyecto, mientras que GitLab es el ecosistema completo de desarrollo

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