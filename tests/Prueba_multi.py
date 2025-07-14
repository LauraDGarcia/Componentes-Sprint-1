import requests
import random
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# Lista de User-Agents comunes
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0) Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11) Chrome/91.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.1) Chrome/90.0",
]

# Datos del link
url_base = "https://dev-bk-redirect-vm.inlazetest.com/"  # ejemplo: https://redirect.commizzion.com/url
slug = "888sport"
prom_code = "1853431"
link = f"{url_base}/{slug}/{prom_code}"

# Generador de fingerprints falsos
def generar_headers():
    ua = UserAgent()
    return {
        "User-Agent": ua.random,
        "Accept-Language": random.choice(["es-CO", "en-US", "pt-BR"])
    }

# Simular 100 clics únicos
for i in range(100):
    headers = generar_headers()
    response = requests.get(link, headers=headers)
    print(f"Clic {i+1} - Status: {response.status_code}")
