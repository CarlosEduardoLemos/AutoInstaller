import subprocess
import webbrowser
import platform
import os


def verificar_sistema_operacional():
    """Verifica o sistema operacional e retorna o tipo."""
    so = platform.system()
    if so == "Windows":
        print("Sistema operacional compatível: Windows.")
        return "Windows"
    elif so == "Linux":
        print("Sistema operacional compatível: Linux baseado em Debian.")
        return "Linux"
    else:
        print(f"Sistema operacional incompatível: {so}. Este script só funciona em Windows ou Linux baseado no Debian.")
        return None


def executar_como_administrador_linux():
    """Verifica se o script está sendo executado como root no Linux."""
    if os.geteuid() != 0:
        print("Este script precisa ser executado como root no Linux.")
        return False
    return True


def instalar_aplicativos_windows(lista_aplicativos):
    """Instala aplicativos no Windows usando Winget."""
    for app, url in lista_aplicativos.items():
        print(f"Tentando instalar {app} via Winget no Windows...")
        try:
            subprocess.run(
                [
                    "winget", "install", "--id", app, "-e", "--silent", "--accept-package-agreements", "--accept-source-agreements"
                ],
                check=True
            )
            print(f"{app} instalado com sucesso!\n")
        except subprocess.CalledProcessError:
            print(f"Erro ao instalar {app} via Winget. Abrindo o site oficial para download.\n")
            abrir_site_para_download(url)


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


# Dicionário de aplicativos: Nome do pacote no gerenciador e URL do site oficial
aplicativos = {
    # Para Windows (Winget ID) ou Linux (apt package name)
    "Google.Chrome": "https://www.google.com/chrome/",
    "code": "https://code.visualstudio.com/",  # VSCode (nome do pacote no apt e Winget)
    "7zip": "https://www.7-zip.org/"  # Nome fictício no apt
}


# Verifica o sistema operacional antes de continuar
sistema = verificar_sistema_operacional()
if sistema == "Windows":
    instalar_aplicativos_windows(aplicativos)
elif sistema == "Linux":
    if executar_como_administrador_linux():
        instalar_aplicativos_linux(aplicativos)
    else:
        print("Encerrando o programa. Execute como root para prosseguir.")
else:
    print("Sistema operacional incompatível. Encerrando o programa.")
