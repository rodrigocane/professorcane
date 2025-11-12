import random

palavras = [
    "abacaxi", "abismo", "abelha", "abobora", "acender", "acolher", "acordar", "adeus", "admirar", "alegria", "algoritmo", "alicate", "almofada", "amarelo", "amassar", "amizade", "amostra", "andarilho", "anelado", 
    "aniversario", "apertar", "aprender", "aracnideo", "arejado", "armazem", "arranhar", "assembleia", "atitude", "atrasar", "atualizar", "aumentar", "automação", "aventura", "baguete", "bagunceiro", "balaustrada", "banheiro", "barulho", 
    "batom", "beleza", "bicicleta", "biscoito", "brasileiro", "brinquedo", "bronzeado", "cadastro", "cafezal", "caldeira", "camiseta", "caneta", "caranguejo", "carinho", "carnaval", "carteira", "casaco", "cágado", "interface", 
    "castanha", "cebola", "celular", "cerebro", "cimento", "cinzento", "cobertor", "colher", "comando", "computador", "conectar", "corrigir", "coruja", "costume", "cristal", "cruzado", "dentista", "desenhar", "desejar", "código", 
    "detalhe", "dinheiro", "distante", "divertido", "doceiro", "dominar", "dureza", "elefante", "embriagar", "empanado", "empolgar", "encantar", "enrolado", "entropia", "enxame", "escada", "esmalte", "espacato", "espelho", "estrela", "fagulha", "fantasma", 
    "farmacia", "felicidade", "feriado", "figurado", "floresta", "formigueiro", "fortaleza", "fragancia", "frangueira", "geladeira", "girassol", "goiaba", "goleiro", "governo", "gramado", "gratidao", "grelhado", "guardiao", "gulosa",
    "harmonia", "horizonte", "hospital", "impressao", "incendio", "inseto", "inverno", "janela", "jardineiro", "joaninha", "jornal", "julgador", "justica", "labirinto", "ladeira", "lambida", "lanterna", "lavanderia", "lenhador",
    "leopardo", "limonada", "linguica", "literario", "livraria", "loterica", "macaneta", "madeira", "magnolia", "malandro", "mamifero", "mandioca", "manivela", "manobra", "marcador", "marreco", "martelo", "mascote", 
    "medalhao", "melancia", "mensagem", "mentirosa", "mergulho", "mexerica", "maionese", "milagre", "minhoca", "molinete", "montanha", "morcego", "mordida", "mosaico", "motociclo", "movimento", "musculoso", "navalha", "necessario", 
    "nebuloso", "negocio", "negrume", "nervoso", "nobreza", "noturno", "nublado", "oceano", "ofensivo", "olecrano", "olhar", "ombro", "opiniao", "operario", "organizar", "ornamento", "ossosso", "otimismo", "paciente",
    "palavra", "palhaco", "palestra", "palmada", "panqueca", "papelada", "parafuso", "parede", "pastelaria", "pato", "peculiar", "pedreiro", "peixeiro", "pelicano", "pendente", "perfume", "perigoso", "permissao", "persiana", 
    "petroleo", "picareta", "pimenta", "pincelada", "pingente", "pioneiro", "pirata", "picles", "planeta", "plastico", "poluente", "ponteiro", "porquinho", "portaria", "posicao", "prazer", "presente", "pretensao", "progresso",  "programador",
    "protetor", "quadrado", "queimado", "quilombo", "rabugento", "racharia", "rapadura", "rebanho", "recado", "recheado", "recolher", "recordar", "refrigerar", "refugio", "relampago", "relogio", "remendo", "renovado", "piroga", "regeneração",
    "repousar", "resposta", "retirada", "reuniao", "revolver", "ribeirao", "rigidez", "risada", "robusto", "rodeado", "romance", "roseiral", "rotativo", "sabedoria", "sabonete", "sacerdote", "salgueiro", "salpicar", 
    "salsicha", "sanfonia", "sapateiro", "sarjeta", "saudavel", "segredo", "serelepe", "serenata", "serpente", "sinalizar", "sobrinho", "solucao", "sombra", "sorrir", "sortudo", "sucesso", "suficiente", "tabelado", "tabuleiro", 
    "talento", "tamborim", "tangerina", "tapete", "teclado", "telefone", "temperar", "tentador", "termometro", "tijolada", "tolerante", "torneira", "torrente", "traduzir", "tranquilo", "transição", "travesseiro", "triangulo", 
    "triciclo", "trilheiro", "trombeta", "turbina", "uniforme", "universo", "urgente", "usuario", "utensilio", "vacinado", "vagalume", "valente", "valioso", "varanda", "vassoura", "velocista", "venenoso", "verdade", 
    "vermelho", "vestuario", "viaduto", "viagem", "vibrador", "vidraceiro", "vigiante", "vilarejo", "vinagre", "violino", "vitamina", "voadora", "volante", "vontade", "vulcancia", "xadrez", "zangado", "zombaria" 
] 


def proxima():
    return random.choice(palavras)
