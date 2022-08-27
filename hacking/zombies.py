## Zombies 
# Author : Mrx04programmer
# Github : https://github.com/mrx04programmer
import requests, platform, random, string, os
from dev.colors import *
## T and ZMB Is the extension for Module Zombies

r = requests
host_objective = None
sh = os.system
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36)'
def create_zombie(name, host, port):
    print(f"{O}[+] {W}Creating zombie {name}")
    try:
        connector = r.get(f'http://{host}:{port}', timeout=10.000)
        if connector.status_code != 200:
            print(f"{R}[!] {W}Zombie not created")
        else:
            f = open(f'zombie_{name}.yml', 'w')
            f.write(f"host: {host}:{port}\nHeaders:")
            f.write(f"{str(connector.headers)}")
            f.close()
            print(f"{G}[+] Zombie created successful !")
    except Exception as e:
        print(f"{R}[!] {W}Zombie not created !.\nBecause {e}")
def create_zombie_without_port(name, host):
    print(f"{O}[+] {W}Creating zombie {name}")
    try:
        connector = r.get(f'http://{host}', timeout=10.000)
        if connector.status_code != 200:
            print(f"{R}[!] {W}Zombie not created")
        else:
            f = open(f'zombie_{name}.yml', 'w')
            f.write(f"host: {host}\nHeaders:")
            f.write(f"{str(connector.headers)}")
            f.close()
            print(f"{G}[+] Zombie created successful !")
    except Exception as e:
        print(f"{R}[!] {W}Zombie not created ! .\nBecause {e}")
def cookies_generator(platform, user):
    pass # beta
def zombiesAttack(zombie, objective_with_or_without_port, method):
    try:
        user = zombie
        objective = objective_with_or_without_port
        print(f"{O}[START] {G}{zombie} >> {P}{objective}")
        # Spoof
        headers = {'user-agent': user_agent}
        if 'g' in method:
            connector = r.get(f'http://{objective}', headers=headers)
        else:
            connector = r.post(f'https://{objective}', headers=headers)

        print(f"{G}[INFO] {W} Using User Agent: {user_agent}")
        #print(f"{G}[INFO] {W} Code ETAG : {O}{str(connector.headers['etag'])}")
        print(f"{G}[SERVER] {W} Connected with http://{objective} successful !, use commands:")
        print("1. For Send data -> {'user': 'admin', 'password': 'admin'")
        print("2. export file html -> export")
        while True:
            payload = input(f'{R}term@{objective}/{user}>> {W}')
            if payload == 'exit':
                print(f"{R} Bye...")
                exit()
            elif 'export'in payload:
                f = open('output.html', 'w')
                f.write(str(connector.text))
                f.close()
                
            elif 'g' in method:
                connector = r.get(f'http://{objective}', headers=headers, data=payload)
            else:
                connector = r.post(f'https://{objective}', headers=headers, data=payload)
            print(f"{G}{connector.text}")


    except Exception:
        print(f"{R}[INFO] {W} Web not vulnerable")
        #print(f"{R}[INFO] {W} Web not vulnerable, {e}")
def clearZombies():
    if platform.system() == '':
        sh('rm *.yml')
    elif 'w' in platform.system() or 'W' in platform.system():
        sh('rmdir *.yml')
    else:
        sh('rm *.yml')