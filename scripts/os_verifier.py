import platform

def verificar_sistema_operacional():
    """Verifica o sistema operacional e retorna o tipo."""
    so = platform.system()
    if so == "Windows":
        return "Windows"
    elif so == "Linux":
        return "Linux"
    else:
        return None
