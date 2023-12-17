import requests
from bs4 import BeautifulSoup as soup
import random
import colorama as color
import os
logo = color.Fore.RED + f"""
  ▄▄█▀▀▀█▄█▀███▀▀▀███▀███▄   ▀███▀              ▀████▀███▀▀▀██▄  
▄██▀     ▀█  ██    ▀█  ███▄    █                  ██   ██    ▀██▄
██▀       ▀  ██   █    █ ███   █                  ██   ██     ▀██
██           ██████    █  ▀██▄ █                  ██   ██      ██
██▄    ▀████ ██   █  ▄ █   ▀██▄█       █████      ██   ██     ▄██
▀██▄     ██  ██     ▄█ █     ███                  ██   ██    ▄██▀
  ▀▀███████▄█████████████▄    ██                ▄████▄████████▀

                        {color.Fore.CYAN}By: {color.Fore.YELLOW}Little.Kid                                                            
"""
def check():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    for gg in range(cantidad):
        pq = random.randint(100000000,999999999)
        url = f"https://www.roblox.com/users/{pq}/profile"
        rr = requests.get(url)
        if rr.status_code == 200:
            osi = soup(rr.text, "html.parser")
            titulo = osi.title.string
            print(f"{color.Fore.BLUE}{gg}  {color.Fore.GREEN}ID: {pq}{color.Fore.RESET} | {color.Fore.YELLOW}Nombre: {color.Fore.CYAN}{titulo}")
        else:
            print(f"{color.Fore.BLUE}{gg}  {color.Fore.GREEN}ID: {color.Fore.RED}{pq}")
cantidad = int(input(">> "))
if cantidad <= 100:
    check()
else:
    print("Cantidad maxima!")
