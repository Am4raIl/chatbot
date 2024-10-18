import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Criar conta no Groq
# Criar API Key
# Criar arquivo .env e rodar o comando "pip install python-dotenv" no terminal
# No arquivo .env escrever: "API_KEY=sua_api_key_aqui"

load_dotenv()
api_key = os.getenv('API_KEY')
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens):
  mensagens_modelo = [('system', 'Você é um assistente virtual chamado AMABOT')]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  answer = chain.invoke({})
  return answer.content

print("Seja bem-vindo ao AmaBot")
mensagens = []
while True:
  pergunta = input("Pergunta: ")
  if(pergunta.lower() == 'sair'):
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print("AmaBot: ", resposta)
print("Obrigado por utilizar o AmaBot! Até logo!")
print(mensagens)
