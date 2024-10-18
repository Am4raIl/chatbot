import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

# Criar conta no Groq
# Criar API Key
# Criar arquivo .env e rodar o comando "pip install python-dotenv" no terminal
# No arquivo .env escrever: "API_KEY=sua_api_key_aqui"

load_dotenv()
api_key = os.getenv('API_KEY')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(msgs, document):
    msgs_system = """Você é um assistente amigável chamado AmaBot.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}"""
    msgs_modelo = [('system', msgs_system)] + msgs  # Concatenar as mensagens do usuário
    template = ChatPromptTemplate.from_messages(msgs_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': document}).content

def carrega_site():
    url_site = input("Digite o link do site: ")
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''  # Inicializar a variável documento
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_pdf():
    path_pdf = input("Digite o caminho do PDF: ")
    loader = PyPDFLoader(path_pdf)
    lista_documentos = loader.load()
    documento = ''  # Inicializar a variável documento
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_youtube():
    url_video = input("Digite o link do vídeo do YouTube: ")
    loader = YoutubeLoader.from_youtube_url(url_video, language=['pt'])
    lista_documentos = loader.load()
    documento = ''  # Inicializar a variável documento
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

print("Seja bem-vindo ao AmaBot!")
texto_selecao = """
Digite 1 para carregar um site
Digite 2 para carregar um PDF
Digite 3 para carregar um vídeo do YouTube
"""

while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    elif selecao == '2':
        documento = carrega_pdf()
        break
    elif selecao == '3':
        documento = carrega_youtube()
        break
    else:
        print("Opção inválida. Tente novamente. Digite um valor entre 1 e 3.")

mensagens = []
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print("AmaBot: ", resposta)
