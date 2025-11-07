# Proyecto: Grupo7 - Funciones Python

Este proyecto es parte de la **Actividad Grupal Clase 9** en **Metodología de Sistemas II**. El objetivo es practicar el trabajo colaborativo usando **Git**, **GitHub Actions** para pruebas automáticas, y fusión de código en GitHub.

## Objetivo

Crear un repositorio donde cada integrante aporte una función matemática en Python, junto con su respectivo test. El flujo de trabajo incluye automatizar las pruebas mediante GitHub Actions cada vez que se suban cambios.

## Estructura

- **main.py**: Archivo principal que importa y ejecuta las funciones.
- **funciones/**: Carpeta con las funciones individuales.
- **tests/**: Carpeta con los tests de las funciones.
- **.github/workflows/test.yml**: Configuración de GitHub Actions para ejecutar las pruebas.

## Integrantes

- Lider de grupo: [Antonio Riveros](https://github.com/Antonio-Riveros).
- Colaboradora : [Zarza Tania](https://github.com/MaguiZarza).
- Colaborador : [Agustin Silva](https://github.com/agussilva88).
- Colaboradora : [Belén Delgado](https://github.com/BelDelgado).

## Flujo de Trabajo

1. **Creación del Repositorio**: Se creó un repositorio llamado `grupo7-funciones-python` y se clonó en las máquinas locales.
2. **Automatización con GitHub Actions**: Se configuró el flujo de trabajo para ejecutar pruebas automáticas en cada push a cualquier rama.
3. **Trabajo en Ramas**: Cada integrante creó una rama con su apellido, agregó su función y test correspondiente.
4. **Pull Requests**: Después de crear las ramas, se hicieron PRs para revisar y fusionar los cambios en `main`.
5. **Verificación Final**: Se comprobó que el flujo de pruebas automáticas se ejecutara correctamente en GitHub Actions.
