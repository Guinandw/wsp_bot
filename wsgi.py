from app import application

from dotenv import load_dotenv
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Ejecutar la aplicación Flask
if __name__ == "__main__":
    application.run(host="127.0.0.1", port=5000, debug=True)