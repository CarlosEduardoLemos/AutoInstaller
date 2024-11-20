from scripts.os_verifier import verificar_sistema_operacional
from scripts.installer_windows import instalar_aplicativos_windows
from scripts.installer_linux import executar_como_administrador_linux, instalar_aplicativos_linux

# Dicionário de aplicativos
aplicativos = {
    "Google.Chrome": "https://www.google.com/chrome/",
    "code": "https://code.visualstudio.com/",  # VSCode
    "7zip": "https://www.7-zip.org/"
}

# Verifica o sistema operacional
sistema = verificar_sistema_operacional()

if sistema == "Windows":
    print("Sistema identificado: Windows.")
    instalar_aplicativos_windows(aplicativos)
elif sistema == "Linux":
    print("Sistema identificado: Linux baseado no Debian.")
    if executar_como_administrador_linux():
        instalar_aplicativos_linux(aplicativos)
    else:
        print("Execute o script como root para continuar.")
else:
    print("Sistema operacional não suportado. O programa será encerrado.")
