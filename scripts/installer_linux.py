import subprocess
import webbrowser
import os

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


def abrir_site_para_download(url):
    """Abre o site do aplicativo para download."""
    print(f"Abrindo o site: {url}")
    webbrowser.open(url)
