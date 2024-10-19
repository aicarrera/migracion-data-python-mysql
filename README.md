# Migración de Datos: Python y MySQL

## Descarga de Datasets

Descargue el dataset seleccionado desde los siguientes enlaces, el link al dataset en kaggle proporcionado en el proyecto para retail, es el mismo proporcionado a continuación. Sin embargo, para el de Iowa, el dataset de Kaggle daba problemas y era muy grande (+20 millones) se recomienda bajar esta versión, las columnas son las mismas. 

- **IOWA**: [Descargar IOWA](https://drive.google.com/file/d/19Hiz1GR3LwiUvonhj-k-zBZmllVcPEHm/view?usp=sharing)
- **RETAIL**: [Descargar RETAIL](https://drive.google.com/file/d/1_Cer6NjpQoYvX-J6d8H-873DR4DeagGK/view?usp=sharing)

## Creación de Esquema en MySQL

1. Cree un nuevo esquema en MySQL con el número de su grupo y el dataset seleccionado. 
   - **Ejemplo**: `grupo_1_iowa`

## Ejecución de Archivos

1. **Ejecutar archivo .sql**:
   - Ejecute el archivo `.sql` de creación de tabla correspondiente al dataset seleccionado, disponible en este repositorio.

2. **Ejecutar archivo Python**:
   - Ejecute el archivo Python relacionado con el dataset seleccionado.

## Requisitos

- Asegúrese de instalar las librerías necesarias antes de ejecutar el archivo Python. Puede usar el siguiente comando:

   ```bash
   pip install -r requirements.txt


## Configuración de conexión:
No olvide cambiar el nombre de la base de datos en el archivo Python.
Modifique el usuario y la contraseña si es necesario. Si está utilizando Docker y no ha cambiado el usuario y contraseña, deberían ser los valores predeterminados.
