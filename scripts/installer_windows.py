import subprocess
import webbrowser

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


def abrir_site_para_download(url):
    """Abre o site do aplicativo para download."""
    print(f"Abrindo o site: {url}")
    webbrowser.open(url)
