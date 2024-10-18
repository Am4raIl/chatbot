import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

# Criar conta no Groq
# Criar API Key
# Criar arquivo .env e rodar o comando "pip install python-dotenv" no terminal
# No arquivo .env escrever: "API_KEY=sua_api_key_aqui"

load_dotenv()
api_key = os.getenv('API_KEY')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

path = 'CAMINHO_DO_ARQUIVO' # É possível pegar o caminho de um Google Drive rodando o código pelo Google Colab
loader = PyPDFLoader(path)
docs = loader.load()

documento = ''
for doc in docs:
  documento += doc.page_content

# Mesmo processo mas ao inves de analizar um pdf, analisar um video no youtube
# link = input("Digite o link do video do youtube: ")
# loader = YoutubeLoader.from_youtube_url(link)
# docs = loader.load()

# documento = ''
# for doc in docs:
#   documento += doc.page_content

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente virtual chamado AmaBot e possui as seguintes informações para formular uma resposta: {informacoes}.'),
    ('user', '{input}')
])
chain = template | chat

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura (em metros): ")
peso = input("Digite seu peso (em kg): ")
atividade = input("Digite com que frequencia você pratica atividades físicas: ")
objetivo = input("Digite seu objetivo com a dieta: ")

resposta = chain.invoke({'informacoes': documento, 'input': f'Olá, meu nome é {nome}. Faça uma dieta pra mim que tenho idade {idade}, altura {altura}, , peso {peso}, pratico atividades fisicas na frequencia {atividade} e tenho o objetivo {objetivo} com a dieta.'})
print(resposta.content)
