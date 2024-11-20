import subprocess
import webbrowser
import os
import requests

def verificar_site_no_ar(url):
    """Verifica se o site está no ar."""
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def executar_como_administrador_linux():
    """Verifica se o script está sendo executado como root no Linux."""
    if os.geteuid() != 0:
        print("Este script precisa ser executado como root no Linux.")
        return False
    return True

def instalar_aplicativos_linux(lista_aplicativos):
    """Instala aplicativos no Linux usando apt."""
    for app, url in lista_aplicativos.items():
        print(f"Tentando instalar {app} via apt no Linux...")
        if verificar_site_no_ar(url):
            try:
                subprocess.run(
                    ["sudo", "apt", "update"], check=True
                )
                subprocess.run(
                    ["sudo", "apt", "install", "-y", app], check=True
                )
                print(f"{app} instalado com sucesso!\n")
            except subprocess.CalledProcessError:
                print(f"Erro ao instalar {app} via apt. Abrindo o site oficial para download.\n")
                abrir_site_para_download(url)
        else:
            print(f"O site {url} não está acessível. Não foi possível instalar {app}.\n")

def abrir_site_para_download(url):
    """Abre o site do aplicativo para download."""
    print(f"Abrindo o site: {url}")
    webbrowser.open(url)
