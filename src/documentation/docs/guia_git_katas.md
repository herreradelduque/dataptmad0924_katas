# Guía de Ayuda: Uso de Git en los Katas de Ironhack

## Índice
1. [Introducción](#introducción)
2. [Comprobación Inicial](#verificación-inicial)
3. [Creación de una Nueva Rama](#creación-de-una-nueva-rama)
4. [Comandos Básicos de Git](#comandos-básicos-de-git)
5. [Abrir un Pull Request](#abrir-un-pull-request)
6. [Conclusión](#conclusión)

---

## Introducción

Bienvenidos a la guía de uso de Git para los Katas de Ironhack. Esta guía está diseñada para que sigas un paso a paso claro y evites errores comunes. Asegúrate de seguir cada paso con atención.

---

## Comprobación Inicial

1.  **Antes de comenzar una nueva tarea** : Abre la terminal y ejecuta:

   ```
   git status
   ```

1.1  **Verifica si estás en la rama main** :

   - Si no estás en la rama `main`, cambia a la rama principal con:

   ```
   git checkout main
   ```

1.2  **Si estás en una rama local y tienes cambios sin confirmar** : Ejecuta los siguientes comandos para guardar tus cambios:

   ```
   git add .
   ```

   ```
   git commit -m "trabajo pendiente"
   ```

   ```
   git push
   ```
   ```
   git checkout main
   ```

1.3  **Verifica que ahora estés en la rama main** :

   ```
   git status
   ```

   Luego, asegúrate de que tu rama principal esté actualizada:

   ```
   git pull origin main
   ```

---

## Creación de una Nueva Rama

2. Una vez que estés en la carpeta del proyecto Katas, crea una nueva rama para comenzar una nueva tarea:

   ```
   git checkout -b <kata_nombre-mi_nombre>
   ```

   **Ejemplo:** `git checkout -b kata-vowel-count-victor`

---

## Comandos Básicos de Git

3. Guarda tus cambios regularmente utilizando:

   ```
   git add <archivos-a-agregar>
   ```

   ```
   git commit -m "lab-started"
   ```

   ```
   git push origin <nombre-de-la-rama>
   ```

   **Al finalizar, realiza un último commit de la siguiente manera:**

   ```
   git add <archivos-a-agregar>
   ```

   ```
   git commit -m "kata-finished"
   ```

   ```
   git push origin <nombre-de-la-rama>
   ```

---

## Abrir una Pull Request

4.  **Finalmente, abre una Pull Request** :

   - Ve a la interfaz del repositorio en GitHub y selecciona tu rama para hacer un Pull Request hacia `main`.

   - Escribe un título descriptivo como:

   ```
   kata ejemplo [tu nombre]
   ```

   El equipo docente revisará tu rama y realizará la fusión de la mejor.

---

## Conclusión

**Para trabajar en las tareas futuras**, crea una nueva rama para cada nueva tarea siguiendo el mismo procedimiento. 

### ¡Happy conding!

```mermaid
flowchart TD
    A[Inicio] --> B{¿Preparado para comenzar?}
    B -->|Sí| C[Ejecutar git status]
    B -->|No| Z[Terminar]
    C --> D{¿Estás en la rama main?}
    D -->|Sí| E[Realizar cambios en la rama]
    D -->|No| F[Ejecutar git checkout main]
    F --> G{¿Hay cambios sin confirmar?}
    G -->|Sí| H[Ejecutar git add .]
    G -->|No| I[Ejecutar git checkout main]
    H --> J[Ejecutar git commit con mensaje: trabajo pendiente]
    J --> K[Ejecutar git push]
    K --> L[Ejecutar git checkout main]
    L --> M[Verificar git status]
    M --> N[Ejecutar git pull origin main]
    N --> O[Crear nueva rama]
    O --> P[Ejecutar git checkout -b kata_nombre-mi_nombre]
    P --> Q[Guardar cambios]
    Q --> R[Ejecutar git add archivos-a-agregar]
    R --> S[Ejecutar git commit con mensaje: lab-started]
    S --> T[Ejecutar git push origin nombre-de-la-rama]
    T --> U[Al finalizar, realizar último commit]
    U --> V[Ejecutar git add archivos-a-agregar]
    V --> W[Ejecutar git commit con mensaje: kata-finished]
    W --> X[Ejecutar git push origin nombre-de-la-rama]
    X --> Y[Abrir Pull Request]
    Y --> Z[Escribir título descriptivo: kata ejemplo tu nombre]
    Z --> AA[Revisión y fusión por el equipo docente]
    AA --> AB[Fin]

classDef textoImportante color:#ff0000, font-weight:bold;

class C textoImportante;

```
