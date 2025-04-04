Este proyecto contiene pruebas automatizadas para la plataforma Commizzion, incluyendo pruebas de login, registro, admin de campañas, campañas, configuracion, wallet y panel.

📌 Requisitos Previos

Antes de ejecutar las pruebas automatizadas, asegúrate de tener instaladas las siguientes herramientas y dependencias:

1️⃣ Instalación de Python

Las pruebas están desarrolladas en Python, por lo que necesitas instalar la última versión estable de Python. Puedes descargarla desde:
https://www.python.org/downloads/

2️⃣ Instalación de pip (gestor de paquetes de Python)

Pip suele venir preinstalado con Python. Puedes verificar si está instalado ejecutando:

pip --version

Si no está instalado, sigue las instrucciones aquí: https://pip.pypa.io/en/stable/installation/

3️⃣ Creación de un Entorno Virtual (Opcional, pero Recomendado)

Para evitar conflictos entre paquetes, se recomienda crear un entorno virtual:

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows

4️⃣ Instalación de Dependencias

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

pip install -r requirements.txt

El archivo requirements.txt debe contener:

pytest
selenium
webdriver-manager

🚀 Ejecución de Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

pytest --browser chrome

Puedes cambiar chrome por firefox, edge o safari según el navegador que desees probar.

📁 Estructura del Proyecto

📂 tests/
 ├── __init__.py 
 ├── conftest.py                   # Configuración de pytest y drivers
 ├── test_campaigns.py             # Pruebas de campañas
 ├── test_login.py                 # Pruebas de inicio de sesión
 ├── test_signin.py                # Pruebas de registro
 ├── test_campaigns_management.py  # Pruebas de administrcion de campañas
 ├── test_configuration.py         # Pruebas de configuracion de la cuenta 
 ├── test_panel.py                 # Pruebas de panel

📂 Commizzion/
 ├── login.py                 # Página de inicio de sesión
 ├── signin.py                # Página de registro
 ├── campaigns.py             # Página de campañas
 ├── campaigns_management.py  # Página de administrcion de campañas
 ├── configuration.py         # Página de configuracion de la cuenta 
 ├── panel.py                 # Página de panel

📄 requirements.txt        # Lista de dependencias
📄 README.md               # Documentación del proyecto

🛠 Configuración Adicional

Si necesitas ejecutar las pruebas en un navegador específico, puedes modificar el parámetro --browser en pytest o establecerlo en el archivo de configuración.
