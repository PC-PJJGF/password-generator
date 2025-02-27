# Password Generator

Este proyecto de **Password Generator** permite generar contraseñas seguras de forma aleatoria, que incluyen una combinación de letras mayúsculas, minúsculas, números y caracteres especiales. Además, el programa ofrece la opción de guardar las contraseñas generadas en un archivo para su posterior consulta y generar nuevas contraseñas según sea necesario.

## Funcionalidades

- **Generación de contraseñas seguras**: Permite generar contraseñas de longitud ajustable (mínimo 8 caracteres) que cumplen con los estándares de seguridad.
- **Validación de contraseñas**: Asegura que la contraseña generada tenga al menos una letra minúscula, una mayúscula, un número y un carácter especial.
- **Guardar contraseñas**: Los resultados pueden ser guardados en un archivo de texto para tener un registro de las contraseñas generadas.
- **Generar nueva contraseña**: Permite generar contraseñas múltiples en una misma sesión.

## Estructura del Proyecto

```bash
    password-generator/
    │
    ├── data/                   # Archivos con las contraseñas guardadas
    │   └── passwords.txt       # Archivo de texto con las contraseñas generadas
    ├── generator/              # Lógica principal del generador de contraseñas
    │   ├── generator.py        # Funciones para generar y validar contraseñas
    │   ├── utils.py            # Funciones auxiliares (entrada y guardado de contraseñas)
    │   └── __init__.py         # Archivo de inicialización para el paquete
    ├── main.py                 # Archivo principal que ejecuta el generador de contraseñas
    ├── .gitattributes          # Configuración de Git
    ├── .gitignore              # Archivos y carpetas a ignorar por Git
    └── requirements.txt        # Dependencias del proyecto (si es necesario en el futuro)
```

## Instalación
1. Clona este repositorio

```bash
    git clone https://github.com/PC-PJJGF/password-generator.git
    cd password-generator
```

2. Crea y activa el entorno virtual

```bash
    python -m venv .venv
    .\.venv\Scripts\activate  # Windows
    source .venv/Scripts/activate  # Linux/MacOS
```

3. Instala las dependencias (solo si es necesario)

```bash
    pip install -r requirements.txt
```

## Uso

1. Ejecuta el **script** principal

```bash
    python main.py
```

2. El programa te pedirá que ingreses

    - El tamaño de la contraseña (mínimo 8 caracteres).
    - Si deseas guardar la contraseña generada en un archivo.
    - Si deseas generar otra contraseña.

3. El programa generará y mostrará la contraseña, y preguntará si deseas guardarla en un archivo de texto.

### Requisitos

Este proyecto utiliza las siguientes librerías de Python:

- `random`: Para generar contraseñas aleatorias.
- `string`: Para trabajar con cadenas de caracteres.
- `re`: Para trabajar con expresiones regulares.
