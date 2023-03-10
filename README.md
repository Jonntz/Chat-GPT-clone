# Chat-GPT-clone
 
 Chatbot de perguntas e respostas desenvolvido em Python utilizando a API do Chat-GPT da OpenAi

## Como usar este ChatBot

### Passo 1 - Clonando o projeto

  - Para clonar este projeto, abra o terminal e rode o comando "git clone https://github.com/Jonntz/Chat-GPT-clone.git" 
  - Também é possivel clonar clicando no botão verde logo acima dos arquivos

### Passo 2 - API Token da OpenAI
  
  Por motivos de segurança, não posso subir o projeto com minha API Key, então vou ensinar como gerar e configurar em um .env

  - Acesse o site da [OpenAI](https://platform.openai.com/signup) e crie sua conta
  - Depois de logado, clique no seu perfil do lado superior direito e clique em "View API Keys"
  - Então clique em "Create new Secret Key"
  - Copie a API Key antes de fechar a Janela
  
### Passo 3 - Configurando o .env

  - Abra o projeto que você clonou com o VS Code ou outro editor de texto
  - Crie um arquivo chamado .env na raiz do projeto
  - Abra o .env e escreva: `API_KEY=[cole aqui a API Key]` e salve
  
### Passo 4 - Instalando dependências e rodando o projeto

  Você precisará ter o Python instalado, caso não saiba instalar [siga este tutorial](https://python.org.br/instalacao-windows/)
  
  - Abra um terminal na pasta do projeto e digite `python -m venv venv`
  - Será criada uma pasta chamada "venv" na raiz, então ative a VirtualEnv com o comando `.\venv\Scripts\Activate.ps1`
  - Agora instale todas as dependências com o comando `pip install -r requirements.txt`
  - Pronto! Para rodar o projeto basta digitar `python start.py`
  
 **Na duvida contate um programador**
