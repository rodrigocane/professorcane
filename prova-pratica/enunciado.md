
# 🧠 Prova Prática – Desenvolvimento de Sistemas  
**Jogo de Classificação de municípios por Região do Brasil**  

🕐 Duração sugerida: 2h30 a 3h  
📚 Stack: PHP, MySQL, HTML, CSS e JavaScript
👥 Equipe: você e todos os robôs que quiser convidar


## 🎯 Objetivo
Criar um jogo interativo onde o jogador deve classificar corretamente municípios brasileiras de acordo com sua **região geográfica**. O jogo terá **10 rodadas**, e ao final será exibido um **ranking com as pontuações dos participantes**.



## 🧩 Telas do Sistema

### 🏠 Tela Inicial (nome sugerido `index.php`)
- Exibe o **ranking** das partidas já finalizadas (em ordem decrescente de pontuação).
- **Jogos incompletos** (ex: jogador saiu antes de terminar as 10 rodadas) **não devem aparecer no ranking**.
- Campo para o jogador digitar seu nome e um botão `🎮 JOGAR`.
- Se o nome digitado já estiver vinculado a uma partida incompleta, o sistema deve **retomar a partida interrompida**. Ou seja, podem haver vários registros para o mesmo jogador, mas apenas um "incompleto".
- Rodapé (que estará visível em todas as telas) com:  
  ```html
  © 2025 [Nome do aluno]
  ```



### 🕹️ Tela do Jogo (nome sugerido `jogo.php`)
- Exibe o cabeçalho da rodada:
  - **Rodada X de 10**
  - **Pontuação atual**
  - **Cronômetro regressivo de 15 segundos**
  - Botão `💾 SALVAR`
- Layout em cruz com 6 áreas coloridas:

<table border="1" cellspacing="0" cellpadding="8" align="center"> <tr> <td colspan="2" align="center">???</td> </tr> <tr> <td align="center">Norte</td> <td align="center">Nordeste</td> </tr> <tr> <td align="center">Centro-Oeste</td> <td align="center">Sudeste</td> </tr> <tr> <td colspan="2" align="center">Sul</td> </tr> </table>

- Em cada rodada:
  - Aparecem **6 municípios arrastáveis** no `???`:
    - Um de cada região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul)
    - Um município **extra** (ou seja, a cada rodada uma região estará representada por dois municípios)
  - O jogador deve **arrastar os municípios** para os retângulos das regiões. (Se quiser adicionar botões ou outros mecanismos de interação com usuário, fique a vontade. Mas o controle via Drag/Drop é obrigatório).
  - **Pontuação**: 10 pontos por município colocado corretamente. Nenhum ponto é retirado por erros ou omissões.
  - Quando o tempo acabar ou o jogador clicar em `SALVAR`, a rodada termina.


### 📋 Resumo da Rodada
- Exibir:
  - ✅ **Quantidade de acertos**
  - 🧮 **Pontuação atualizada**
  - 📍 Municípios corretamente classificados (com estado)
    - Exemplo:  
      `Norte: Xapuri-AC | Nordeste: Cabaceiras-PB | Centro-Oeste: Jandaia-GO | Sudeste: Pau Grande-RJ | Sul: Rolândia-PR`
  - ❌ Municípios não classificados ou incorretos (não informar região nem estado):
    - Exemplo:  
      `Incorreto: Anta Gorda`
- O resumo pode ser exibido via:
  - Modal
  - `alert()`
  - Nova tela (ex: `calcula_resultado.php`)
- Após a exibição do resultado da **décima rodada**, redirecionar o jogador para a tela inicial.


## 🗂️ Banco de Dados
Você receberá uma base de dados com todas as municípios brasileiras organizadas por:
- Nome
- Estado
- Região

Além disso, você precisará criar tabelas para armazenar:
- Partidas (com nome do jogador, pontuação final, status)
- Rodadas (com as municípios sorteadas, respostas do jogador e se acertou)


## ✅ **DOs & DON'Ts** 🚫
- ✅ Recursos aceitos
  - Inteligências artificais Generativas
  - Pesquisa na internet (Github de trabalhos passados, Stackoverflow etc)
  - jQuery, dbo, Ajax, FontAwesome, Bootstrap. Vai fundo! O site é seu. Estilize do jeito que quiser.
- 🚫 Proibido
  - Pedir ajuda ao professor
  - Compartilhar códigos com os colegas

## 🛠️ Tecnologias e Conceitos Exercitados
- 🧠 Lógica de Programação: fluxo condicional e loops
- 🧩 Organização de Projeto Web: múltiplos arquivos e páginas
- 📦 PHP: requisições e manipulação de dados. Sessão (opcional)
- 💾 SQL "básico": SELECT, INSERT, UPDATE, DELETE
- 🧮 SQL "intermediário": uso de `GROUP BY`, `SUM`, `COUNT`, `ORDER BY`
- 🔒 Controle de estado do jogo: partidas completas/incompletas
- 📊 Ranking: agregação e ordenação de resultados
- 📋 HTML: estrutura semântica de páginas
- 🎨 CSS: estilização de layout com cores e posicionamento
- 🧲 JavaScript: `setTimeout`, eventos de clique e DOM
- 🖱️ Interação: elementos arrastáveis (`drag and drop`)
- ⏱️ Temporizadores: cronômetro regressivo por rodada
- 🔁 Redirecionamentos e controle de fluxo entre telas
- 📝 Manipulação de formulários: envio de nome do jogador e também o próprio "form" do jogo.
- 🔁 UX/UI: mostrar feedback de erros e acertos por rodada
  


## 📎 Materiais de Apoio
- 📦 Base de dados com as municípios e também as estruturas sugeridas. Fique à vontade para alterar esta estrutura conforme seu estilo de programação.  
  [🔗 Clique aqui para baixar](#) *(substitua com o link real)*

- 🎨 Layout sugerido da tela do jogo:  
  [🔗 Clique aqui para baixar](#) *(substitua com o link real)*



## 🚀 Features futuras 
O sistema aqui proposto é um _MVP_ (Produto Mínimo Viável). Todavia, o MVP deve ser construído de uma forma que permita a implementação de novas _features_. Segue abaixo algumas features futuras que se encaixariam bem, mas que foram cortadas do escopo para que o trabalho fosse feito em um dia apenas:
- Configurações: A tela inicial deve ganhar um símbolo de engrenagem ⚙️ que daria acesso a uma nova tela (nome sugerido: config.php). O valor atual já deve vir preenchido. Se o usuário deixar algum valor inválido (ex: deixar o campo em branco ou escrever 'POCAHONTAS' onde deveria ir um número) basta ignorar esta informação, preservando o valor default. Não é necessário validações e alertas.Nela estariam disponíveis as configurações:
  - Rodadas por partida: 10
  - Segundos por rodada: 15
  - Pontuação por região (a ideia seria de aumentar a pontuação para regiões Norte e Nordeste e reduzir a das regiões Sul e Sudeste, uma vez que temos mais facilidade com cidades próximas):
    - Norte: 10
    - Nordeste: 10
    - Centro-Oeste: 10
    - Sudeste: 10
    - Sul: 10
- Reset: o ranking deve ganhar um botão 🗑️. Ao clicar nele um popup deve aparecer pedindo a confirmação. Caso o usuário confirme, o resultado de todas as rodadas deve ser excluído da base de dados.
- Placar final: a pontuação final deve passar a ser apresentada em uma modal bonito, com ícones e botões de compartilhar em redes sociais.

Importante: estes recursos NÃO são obrigatórios. Só devem ser levados em consideração durante o desenvolvimento. Implementar estas _features_ NÃO terá qualquer impacto na nota final.

---

Boa prova! 🚀  
Qualquer dúvida, consulte a documentação, pesquise ou use ferramentas como o ChatGPT. 😉
