from fastapi import FastAPI  

app = FastAPI() #Criando uma instância basica do FastAPI

#Importando os roteadores de autenticação 
from auth_routes import auth_router   #auth_router significa roteador de rotas de autenticação
#Importando os roteadores de pedidos
from order_routes import order_router #order_router significa roteador de rotas de pedido

app.include_router(auth_router)
app.include_router(order_router)

# Para rodar o servidor localmente, use o comando no terminal: uvicorn main:app --reload
# O parâmetro –reload reinicia automaticamente o servidor a cada alteração no código