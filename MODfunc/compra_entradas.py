from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# URL de la página web que quieres abrir
url = "https://www.puntoticket.com/Account/SignIn?ReturnUrl=%2fCompra%2fCategoriaTicket%3fEventoID%3dFV2024%26CalID%3d1%26CategoriaTicket%3d8&EventoID=FV2024&CalID=1&CategoriaTicket=8"

# Lista de agentes de usuario para simular diferentes dispositivos y navegadores
user_agents = [
    # Simula un iPhone X
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    # Simula un iPad
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    # Simula Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    # Simula Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    # Simula Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
]

# Lista para almacenar las instancias del navegador
drivers = []

for user_agent in user_agents:
    # Configura las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")

    drivers.append(webdriver.Chrome(options=chrome_options))

    # Abre la URL con la última instancia del navegador añadida
    drivers[-1].get(url)

    # Aquí puedes agregar cualquier acción adicional que quieras realizar en la página web

# Espera 60 segundos antes de terminar el script
a = input()
