#Arquivo de rota de Autenticação

from fastapi import APIRouter

#Criando um roteador com o prefixo "auth" e a tag "auth" para organizar a documentação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

# No FastAPI, uma rota é definida usando um decorador "@auth_router.get" e uma função assíncrona que retorna a resposta
@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}