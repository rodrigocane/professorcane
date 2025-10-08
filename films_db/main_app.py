from dbcon import *
from models import *
from dal import *

if __name__ == '__main__':
    inicializar_banco_dados()
    
    filmes = FilmeDAL().listar_todos()
    for filme in filmes:
        # Usamos o método to_dict() para imprimir um formato JSON-like
        print(filme.to_dict())