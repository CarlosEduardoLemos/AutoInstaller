import subprocess
import webbrowser
import requests

def verificar_site_no_ar(url):
    """Verifica se o site está no ar."""
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def instalar_aplicativos_windows(lista_aplicativos):
    """Instala aplicativos no Windows usando Winget."""
    for app, url in lista_aplicativos.items():
        print(f"Tentando instalar {app} via Winget no Windows...")
        if verificar_site_no_ar(url):
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
        else:
            print(f"O site {url} não está acessível. Não foi possível instalar {app}.\n")

def abrir_site_para_download(url):
    """Abre o site do aplicativo para download."""
    print(f"Abrindo o site: {url}")
    webbrowser.open(url)
