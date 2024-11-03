# Guía de Ayuda: Uso de Git en los Katas de Ironhack

## Índice
1. [Introducción](#introducción)
2. [Clonación del Repositorio](#clonación-del-repositorio)
3. [Verificación Inicial](#verificación-inicial)
4. [Creación de una Nueva Rama](#creación-de-una-nueva-rama)
5. [Comandos Básicos de Git](#comandos-básicos-de-git)
6. [Abrir un Pull Request](#abrir-un-pull-request)
7. [Conclusión](#conclusión)

---

## Introducción

Bienvenidos a la guía de uso de Git para los Katas de Ironhack. Esta guía está diseñada para que sigas un paso a paso claro y evites errores comunes. Asegúrate de seguir cada paso con atención.

---

## Clonación del Repositorio

1. **Solo la primera vez**: Clona este repositorio en tu carpeta `ironhack/katas`:
   
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

   Reemplaza `<URL_DEL_REPOSITORIO>` con la URL del repositorio que se te haya proporcionado.

---

## Verificación Inicial

1. 🚨 **Antes de comenzar una nueva tarea** 🚨: Abre la terminal y ejecuta:

   ```bash
   git status
   ```

1.1 🚨 **Verifica si estás en la rama principal** 🚨:

   - Si no estás en la rama `main`, cambia a la rama principal con:

   ```bash
   git checkout main
   ```

1.2 🚨 **Si estás en una rama local y tienes cambios sin confirmar** 🚨: Ejecuta los siguientes comandos para guardar tus cambios:

   ```bash
   git add .
   git commit -m "cambios no confirmados"
   git push
   git checkout main
   ```

1.3 🚨 **Verifica que ahora estés en la rama principal** 🚨:

   ```bash
   git status
   ```

   Luego, asegúrate de que tu rama principal esté actualizada:

   ```bash
   git pull origin main
   ```

---

## Creación de una Nueva Rama

2. Una vez que estés en la carpeta del proyecto Katas, crea una nueva rama para comenzar una nueva tarea:

   ```bash
   git checkout -b <kata_nombre-mi_nombre>
   ```

   **Ejemplo:** `git checkout -b kata-vowel-count-victor`

---

## Comandos Básicos de Git

3. Guarda tus cambios regularmente utilizando:

   ```bash
   git add <archivos-a-agregar>
   git commit -m "lab-iniciado"
   git push origin <nombre-de-la-rama>
   ```

   **Al finalizar, realiza un último commit de la siguiente manera:**

   ```bash
   git add <archivos-a-agregar>
   git commit -m "kata-terminada"
   git push origin <nombre-de-la-rama>
   ```

---

## Abrir un Pull Request

4. 🚨 **Finalmente, abre un Pull Request** 🚨:

   - Ve a la interfaz del repositorio en GitHub y selecciona tu rama para hacer un Pull Request hacia `main`.

   - Escribe un título descriptivo como:

   ```
   kata ejemplo [tu nombre]
   ```

   El equipo docente revisará tu rama y realizará la fusión de la mejor.

---

## Conclusión

**Para trabajar en las tareas posteriores**, crea una nueva rama para cada nueva tarea siguiendo el mismo procedimiento. 

### ¡Feliz codificación!
