from enum import Enum

class OpcoesOpiniao(Enum):
    NAO_POSSO_OPINAR = 'Não posso opinar'
    NAO_VI_SEM_INTERESSE = 'Não vi e não tenho interesse'
    NAO_VI_COM_INTERESSE = 'Não vi e tenho interesse em ver'
    VI_NAO_GOSTEI = 'Vi e não gostei'
    VI_GOSTEI = 'Vi e gostei'
    
    # Adicionando um método auxiliar para melhor usabilidade
    @classmethod
    def values_list(cls):
        """Retorna uma lista dos valores de string da ENUM."""
        return [e.value for e in cls]

class Filme:
    def __init__(self, id, titulo_original, titulo_portugues, ano_lancamento, link, opiniao):
        self.id = id
        self.titulo_original = titulo_original
        self.titulo_portugues = titulo_portugues
        self.ano_lancamento = ano_lancamento
        self.link = link
        try:
            self.opiniao = OpcoesOpiniao(opiniao)
        except ValueError:
            self.opiniao = OpcoesOpiniao.NAO_POSSO_OPINAR 

    def __repr__(self):
        return f"<Filme id={self.id} titulo='{self.titulo_original}'>"

    # Método opcional, mas útil para serialização rápida
    def to_dict(self):
        return {
            'id': self.id,
            'titulo_original': self.titulo_original,
            'titulo_portugues': self.titulo_portugues,
            'ano_lancamento': self.ano_lancamento,
            'link': self.link,
            'opiniao': self.opiniao
        }