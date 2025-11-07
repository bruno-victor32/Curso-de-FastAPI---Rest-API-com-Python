#Arquivo de rota de Pedidos

from fastapi import APIRouter

#Criando um roteador com o prefixo "pedidos" e a tag "pedidos" para organizar a documentação
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

# No FastAPI, uma rota é definida usando um decorador "@order_router.get" e uma função assíncrona que retorna a resposta
@order_router.get("/")
async def pedidos():
    #As docstrings nas funções das rotas (texto entre “””) aparecem na documentação automática, ajudando a explicar o propósito da rota, parâmetros e possíveis erros.
    """ 
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas de pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota de pedidos"}