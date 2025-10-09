from dbcon import *
from models import *
from dal import *

if __name__ == '__main__':
    inicializar_banco_dados()

    dal = FilmeDAL()
    
    velozes = Filme(None, "The Fast and the Furious", "Velozes e Furiosos", 2001, None, OpcoesOpiniao.VI_GOSTEI)
    dal.adicionar(velozes)

    brokeback = Filme(id=None, link=None, opiniao=OpcoesOpiniao.VI_NAO_GOSTEI, ano_lancamento=2005, titulo_original="Brokeback Mountain", titulo_portugues="O Segredo de Brokeback Mountain")
    dal.adicionar(brokeback)
    
    django = dal.buscar_por_titulo("Dja")
    django.opiniao = OpcoesOpiniao.VI_GOSTEI
    dal.atualizar(django)

    profanacao = dal.buscar_por_titulo("Episode IX")
    dal.deletar(profanacao.id) #Deletando esse filme profano que nunca deveria ter sido feito

    chapeu = Filme(None, "Hoodwinked!", "Deu a Louca na Chapeuzinho", 2005, None, OpcoesOpiniao.NAO_VI_SEM_INTERESSE)
    dal.adicionar(chapeu)

    sharknado = Filme(None, "Sharknado", "Sharknado", 2013, None, OpcoesOpiniao.NAO_VI_SEM_INTERESSE)
    dal.adicionar(sharknado)

    filmes = dal.listar_todos()
    filmes.sort(key=lambda item: item.titulo_original)
    for filme in filmes:
        # Usamos o método to_dict() para imprimir um formato JSON-like
        print(filme.to_dict())
        print()