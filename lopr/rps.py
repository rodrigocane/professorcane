#fiz com o https://www.programiz.com/python-programming/online-compiler/
import random
import time
from abc import ABC, abstractmethod
from collections import Counter

# Utilidades
VENCEDORES = {
    ('R', 'S'): 1,
    ('S', 'P'): 1,
    ('P', 'R'): 1,
    ('S', 'R'): 2,
    ('P', 'S'): 2,
    ('R', 'P'): 2,
}

def calcular_vencedor(j1, j2):
    if j1 == j2:
        return 0
    return VENCEDORES.get((j1, j2), 0)

def normalizar_peca(p):
    return p.upper()

# Classe Base para jogadores
class JogadorBase(ABC):
    def __init__(self):
        self.id_jogador = None  # será 1 ou 2
        self.pecas = None

    def set_id(self, id_jogador):
        self.id_jogador = id_jogador
    
    def set_pecas_iniciais(self, iniciais):
        self.pecas = iniciais
        
    @abstractmethod
    def escolher_jogada(self, historico):
        pass

# Jogador Aleatório
class JogadorAleatorio(JogadorBase):
    def escolher_jogada(self, historico):
        return random.choice(self.pecas)

class JogadorAbundante(JogadorBase):
    def escolher_jogada(self, historico):
        contagem = Counter(self.pecas)
        if not contagem:
            return 'R'  # fallback pra evitar erro se lista estiver vazia
        ordenadas = sorted(contagem.items())
        # Pega a mais "abundante" e com maior prioridade (última da ordenação)
        escolha = ordenadas[-1][0]
        return escolha        
        
class JogadorP1(JogadorBase):
    def escolher_jogada(self, historico):
        return self.pecas[1]

class JogadorTeimoso(JogadorBase):
    def escolher_jogada(self, historico):
        # Ver a última jogada desse jogador no histórico
        ultima = None
        for rodada in reversed(historico):
            if self.id_jogador == 1:
                ultima = rodada['jogador1_escolha']
            else:
                ultima = rodada['jogador2_escolha']
            if ultima:
                break

        # Se ele nunca jogou, escolhe qualquer peça (por padrão, 'R')
        if ultima is None:
            for p in ['R', 'P', 'S']:
                if p in self.pecas:
                    return p
            return self.pecas[0]  # fallback

        # Se ainda tiver a peça da última jogada, repete
        if ultima in self.pecas:
            return ultima

        # Se não tiver, escolhe qualquer outra peça que tenha
        return random.choice(self.pecas) if self.pecas else 'R'
        
class JogadorSequencial(JogadorBase):
    ordem = ['R', 'P', 'S']

    def escolher_jogada(self, historico):
        # Ver qual foi sua última jogada
        ult_jogada = None
        for rodada in reversed(historico):
            if self.id_jogador == 1:
                ult_jogada = rodada['jogador1_escolha']
            else:
                ult_jogada = rodada['jogador2_escolha']
            if ult_jogada in self.ordem:
                break

        # Determinar próxima da sequência
        if ult_jogada is None:
            proxima = 'R'
        else:
            try:
                idx = self.ordem.index(ult_jogada)
                proxima = self.ordem[(idx + 1) % 3]
            except ValueError:
                proxima = 'R'

        # Se tiver a peça, joga ela
        if self.pecas.count(proxima) > 0:
            return proxima

        # Se não tiver, joga a primeira que tiver da ordem
        for p in self.ordem:
            if p in self.pecas:
                return p

        # fallback
        return self.pecas[0] if self.pecas else 'R'

class JogadorNaoMexeGanhando(JogadorBase):
    def __init__(self):
        self.ultima_jogada = 'S'  # Começa com Tesoura

    def escolher_jogada(self, historico):
        ordem = ['R', 'P', 'S']  # ordem reversa
        prioridades = list(reversed(ordem))  # S > P > R

        if historico:
            ultima_rodada = historico[-1]
            if self.id_jogador == 1:
                minha = ultima_rodada['jogador1_escolha']
                oponente = ultima_rodada['jogador2_escolha']
                resultado = ultima_rodada['resultado']
                ganhei = resultado == '1' or resultado == '='
            else:
                minha = ultima_rodada['jogador2_escolha']
                oponente = ultima_rodada['jogador1_escolha']
                resultado = ultima_rodada['resultado']
                ganhei = resultado == '2' or resultado == '='

            # Continua com a mesma jogada se ganhou ou empatou e ainda tem a peça
            if ganhei and self.ultima_jogada in self.pecas:
                return self.ultima_jogada

        # Troca a jogada: pega a próxima disponível em ordem S → P → R
        for p in prioridades:
            if p in self.pecas:
                self.ultima_jogada = p
                return p

        return self.pecas[0]  # fallback se tudo der errado

# Jogador via input
class JogadorUsuario(JogadorBase):
    def escolher_jogada(self, historico):
        while True:
            escolha = input(f"Suas peças: {''.join(sorted(self.pecas))}. Escolha (R, P ou S): ")
            escolha = normalizar_peca(escolha)
            if escolha in self.pecas:
                return escolha
            print("Escolha inválida. Tente novamente.")

# Jogo principal
class Jogo:
    def __init__(self, jogador1:JogadorBase, jogador2:JogadorBase, max_jogadas = 100, verboso=True):
        self.j1 = jogador1
        self.j2 = jogador2
        self.verboso = verboso
        self.j1.set_id(1)
        self.j2.set_id(2)
        self.max_jogadas = max_jogadas
        self.partida_atual = 0
        self.vencedores = [0,0]

    def imprimir_estado(self, j1_pecas, j2_pecas, jogada1, jogada2, resultado):
        if not self.verboso:
            return
        
        seta = "="
        if resultado == 1:
            seta = ">"
        elif resultado == 2:
            seta = "<"
        print(f"Rodada {self.rodada:02d}: [{jogada1} {seta} {jogada2}] ({''.join(sorted(j1_pecas))} X {''.join(sorted(j2_pecas))})")

    def acabou(self):
        tipos_j1 = set(self.j1.pecas)
        tipos_j2 = set(self.j2.pecas)
        return len(tipos_j1) == 1 or len(tipos_j2) == 1 or self.rodada >= self.max_jogadas

    def vencedor_final(self):
        if len(set(self.j1.pecas)) == 1 and len(set(self.j2.pecas)) != 1:
            return 2
        elif len(set(self.j2.pecas)) == 1 and len(set(self.j1.pecas)) != 1:
            return 1
        elif self.rodada >= self.max_jogadas:
            if len(self.j1.pecas) > len(self.j2.pecas):
                return 1
            elif len(self.j2.pecas) > len(self.j1.pecas):
                return 2
            else:
                return 0  # empate
        return 0  # ainda não acabou
    
    def jogar(self, partidas=10):
        inicio = time.perf_counter()
        for i in range(partidas):
            if self.verboso:
                print(f"Iniciando partida {self.partida_atual+1}")
            vencedor_rodada = self.jogar_rodada()
            if vencedor_rodada > 0:
                self.vencedores[vencedor_rodada-1] += 1
        
        if self.verboso:
            print("-------Placar final-------")
        print(f"{self.j1.__class__.__name__} [{self.vencedores[0]} X {self.vencedores[1]}] {self.j2.__class__.__name__}", end='. ')
        fim = time.perf_counter()
        print(f"Tempo de jogo: {fim - inicio:.3f} segundos")
    
    def jogar_rodada(self):
        self.historico = []
        self.pecas_acumuladas = []
        self.rodada = 0
        self.j1.set_pecas_iniciais(list('RRRPPPSSS'))
        self.j2.set_pecas_iniciais(list('RRRPPPSSS'))
        while not self.acabou():
            self.rodada += 1
            j1_peca = self.j1.escolher_jogada(self.historico)
            j2_peca = self.j2.escolher_jogada(self.historico)

            j1_peca = normalizar_peca(j1_peca)
            j2_peca = normalizar_peca(j2_peca)

            resultado = calcular_vencedor(j1_peca, j2_peca)

            if resultado == 0:
                # empate
                self.j1.pecas.remove(j1_peca)
                self.j2.pecas.remove(j2_peca)
                self.pecas_acumuladas.extend([j1_peca, j2_peca])
            elif resultado == 1:
                self.j2.pecas.remove(j2_peca)
                self.j1.pecas.append(j2_peca)  # ganhou peça do outro
                self.j1.pecas.extend(self.pecas_acumuladas)
                self.pecas_acumuladas.clear()
            elif resultado == 2:
                self.j1.pecas.remove(j1_peca)
                self.j2.pecas.append(j1_peca)  # ganhou peça do outro
                self.j2.pecas.extend(self.pecas_acumuladas)
                self.pecas_acumuladas.clear()

            self.imprimir_estado(self.j1.pecas, self.j2.pecas, j1_peca, j2_peca, resultado)

            self.historico.append({
                'rodada': self.rodada,
                'jogador1_escolha': j1_peca,
                'jogador2_escolha': j2_peca,
                'resultado': resultado,
                'pecas_jogador1': self.j1.pecas.copy(),
                'pecas_jogador2': self.j2.pecas.copy(),
                'acumuladas': self.pecas_acumuladas.copy(),
            })

        vencedor = self.vencedor_final()
        if self.verboso:
            print("\nFim de jogo!")
            
            if vencedor == 1:
                print("Jogador 1 venceu!")
            elif vencedor == 2:
                print("Jogador 2 venceu!")
            else:
                print("Empate!")
                
            print() 
        return vencedor

#Insira seu jogador aqui

if __name__ == "__main__":    
  #escolha os jogadores  
  jogo = Jogo(JogadorSequencial(), JogadorNaoMexeGanhando(), 10, False)
  jogo.jogar(1000)
