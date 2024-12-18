# Auto Installer for Windows e Linux

## Descrição  
Este script automatiza a instalação de aplicativos no Windows usando o gerenciador de pacotes **Winget** e no Linux usando o **apt**. Ele verifica o sistema operacional, garante que o script está sendo executado com privilégios de administrador (no caso do Linux), e tenta instalar os aplicativos de forma silenciosa. Caso o gerenciador de pacotes não consiga instalar um aplicativo, o script abre o site oficial para que o download manual seja realizado.

## Funcionalidades  
1. **Verificação do Sistema Operacional**  
   - Confirma se o sistema operacional é Windows ou Linux baseado em Debian. Se não for, o script informa a incompatibilidade e encerra a execução.

2. **Execução como Administrador (Linux)**  
   - Verifica se o script está sendo executado com privilégios de administrador no Linux.
   - Se não estiver, o script exibe uma mensagem e interrompe o processo.

3. **Instalação de Aplicativos via Winget (Windows)**  
   - Utiliza o **Winget** para instalar os aplicativos de forma silenciosa e aceita automaticamente os acordos de licença.
   - Caso o aplicativo não possa ser instalado, o script redireciona para o site oficial.

4. **Instalação de Aplicativos via apt (Linux)**  
   - Utiliza o **apt** para instalar os aplicativos de forma silenciosa.
   - Caso o aplicativo não possa ser instalado, o script redireciona para o site oficial.

5. **Redirecionamento para Download Manual**  
   - Abre o navegador para o site oficial do aplicativo caso a instalação via gerenciador de pacotes falhe.

## Pré-requisitos  
1. **Winget Instalado (Windows)**  
   - Certifique-se de que o Winget está instalado e configurado. Você pode verificar executando `winget --version` no terminal.

2. **Privilégios de Administrador (Linux)**  
   - O script precisa ser executado com privilégios de administrador para instalar aplicativos corretamente no Linux.

3. **Python 3.x**  
   - Instale o Python 3.x e garanta que o módulo `webbrowser` está disponível (ele é padrão no Python).

## Como Usar  
1. Clone ou baixe o script no seu computador:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Abra um terminal como administrador (no caso do Linux).  
3. Navegue até o diretório onde o script está salvo.
4. Execute o script:
   ```bash
   python auto_installer_windows.py
   ```

## Configuração do Script  
Os aplicativos a serem instalados estão definidos no dicionário `aplicativos` dentro do código. Cada entrada do dicionário contém:  
- O **ID** do aplicativo no Winget (para Windows) ou o nome do pacote no apt (para Linux).  
- O **URL** oficial do site do aplicativo.  

### Exemplo de Dicionário:
```python
aplicativos = {
    "Google.Chrome": "https://www.google.com/chrome/",
    "Microsoft.VisualStudioCode": "https://code.visualstudio.com/",
    "7zip.7zip": "https://www.7-zip.org/"
}
```

Para adicionar novos aplicativos:
1. Verifique o **ID** do aplicativo executando:
   ```bash
   winget search <nome_do_aplicativo>  # Para Windows
   ```
   ou
   ```bash
   apt search <nome_do_aplicativo>  # Para Linux
   ```
2. Adicione o **ID** ou o nome do pacote e o **URL oficial** ao dicionário.

## Explicação do Código  
### Funções
- **`verificar_sistema_operacional()`**  
  Verifica se o sistema operacional é Windows ou Linux baseado em Debian. Se não for, exibe uma mensagem e encerra a execução.

- **`executar_como_administrador_linux()`**  
  Confirma que o script está sendo executado com privilégios de administrador no Linux. Caso contrário, solicita que o usuário reinicie o script com os privilégios necessários.

- **`instalar_aplicativos_windows(lista_aplicativos)`**  
  Percorre a lista de aplicativos, tentando instalá-los via Winget no Windows. Se a instalação falhar, chama a função `abrir_site_para_download`.

- **`instalar_aplicativos_linux(lista_aplicativos)`**  
  Percorre a lista de aplicativos, tentando instalá-los via apt no Linux. Se a instalação falhar, chama a função `abrir_site_para_download`.

- **`abrir_site_para_download(url)`**  
  Abre o navegador padrão no URL fornecido, permitindo o download manual do aplicativo.

### Parâmetros do Winget
O script utiliza os seguintes parâmetros para instalar aplicativos no Windows:  
- **`--id`**: Identifica o aplicativo no repositório Winget.  
- **`-e`**: Garante que o ID é exato (match preciso).  
- **`--silent`**: Instala o aplicativo silenciosamente, sem interações do usuário.  
- **`--accept-package-agreements`**: Aceita automaticamente os termos de uso.  
- **`--accept-source-agreements`**: Aceita os acordos de fonte de pacotes.

## Exemplo de Execução  
Se o dicionário contém os seguintes aplicativos:  
```python
aplicativos = {
    "Google.Chrome": "https://www.google.com/chrome/",
    "7zip.7zip": "https://www.7-zip.org/"
}
```

O script:  
1. Verifica se o sistema é Windows ou Linux baseado em Debian.  
2. Garante que está sendo executado como administrador (no caso do Linux).  
3. Tenta instalar o Google Chrome e o 7-Zip usando o Winget (no Windows) ou apt (no Linux).  
4. Se o gerenciador de pacotes falhar, abre os sites oficiais dos aplicativos no navegador.
