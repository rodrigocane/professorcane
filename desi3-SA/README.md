# 🚀 **Situação de Aprendizagem - Desenvolvimento de Sistemas** 🚀

## 🧭 **Contexto** 🧭
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Na Situação de Aprendizagem deste semestre vocês desenvolverão um sistema de **CRM** (**C**ustomer **R**elationship **M**anagement) agnóstico, que pode ser usado pela sua mãe que vende Avon, pelo seu tio que vende marmita ou pelo barbeiro descolado da sua esquina. Esse sistema também poderia ser “acoplado” ao sistema do mercadinho do seu bairro ou talvez até ao próprio SENAI!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O sistema será de uso “interno” de um determinado empreendimento e/ou grupo econômico, podendo ser hospedado na nuvem ou em servidor local. Ou seja, não há uma preocupação quanto à usabilidade para usuários leigos, uma vez que espera-se que os usuários sejam treinados para utilizar o sistema.


## ⚙️ **Funcionalidades** ⚙️
- 🔑 Usuários (Controle de sessão e de acessos)
  	- DDL (Scripts para criação das tabelas de usuário já com ADM cadastrado) 📂
	- Login/Logout
	- Primeiro login ADM (troca de senha 🔑)
	- Convite de usuário (e-mail 📧) ⚠
	- Cadastro de usuário
		- Busca cep (AJAX)📬
		- validação de e-mail 📧
	- Esqueci minha senha 🔑 (e-mail 📧 & token uso unico)
	- Gestão de usuários
		- Perfis: ADM (1 só), Supervisor e usuário
    		- Rotinas "perigosas"/"importantes" serão acessíveis apenas pelo ADM e pelos supervisores ⚠
	- Logs do sistema ⚠
- 👥 Clientes (CRUD)
  	- DDL (Scripts para criação das tabelas de clientes) 📂
	- Cadastro de cliente
   		- Campos a seu critério, mas não esqueça dos básicos
		- Busca cep (AJAX)📬
		- Validação de e-mail 📧
	- Listagem de clientes (paginação)
	- Alteração de cliente (usuário comum só pode alterar cliente que ele cadastrou) ⚠
	- Exclusão de Cliente (usuário comum só pode excluir cliente que ele cadastrou) ⚠
	- Importar ↙️ (Rodada bônus 📈)
- 💌 Relacionamento (Recursos que realmente geram valor)
	- Listagem de clientes (filtros) [complementando a funcionalidade desenvolvida no "módulo" Clientes]
	- Exportar [precisa pelo menos uma] ↗️
   		- PDF
		- Excel (Rodada bônus 📈)
		- JSON (Rodada bônus📈)
	- Histórico/Anotações/Comentários sobre Clientes
	- Pesquisa NPS (e-mail 📧 & token unico) (Rodada bônus 📈) ⚠
- 💻 API REST
  	- Rotas 🗺️
		- GET
		- GET id
		- POST
		- PUT
		- DELETE
  	  	- GET com filtros (Rodada bônus 📈)
	- Gestão de acesso (desenvolver algum recurso de segurança para acesso a API) ⚠


## 🤝 **Equipe** 🤝
- **Membros:** de um a quatro membros. Quanto mais membros, mais completo deverá ser o seu sistema.
- **Funcionalidades obrigatórias de acordo com a qtde de membros:**
  - (1) 👤: "Clientes" [👥]
  - (2) 👤👤: "Clientes" e "Login" [👥🔑]
  - (3) 👤👤👤: "Login", "Clientes" e "Relacionamento" [👥🔑💌]
  - (4) 👤👤👤👤: TUDO!!! [👥🔑💌💻]

## 📦 **Entregáveis** 📦
1. Sistema funcional, commitado no GIT em repositório acessível pelo professor. Os commits devem ser feitos ao longo do semestre e por todos os integrantes da equipe. 🚀
2. Apresentação de ATÉ 15 minutos, focada na usibilidade e nos diferenciais do seu trabalho em específico 🕒
3. ~~Documentação~~ não quero documentação "oficial" não. 📕

## 🎖️ **Critérios de Qualidade** 🎖️ 
- 🌎 Globais
  - Qualquer processo de exclusão de informação deve incluir uma reafirmação de intenção antes (ex: Realmente deseja excluir cliente "Dayane Giovanni"?)
  - Inputs de formulários devem ter validação de "conteúdo" e de obrigatoriedade
    - Ex: Nome do cliente não pode ser vazio (é obrigatório) mas também deve ter uma qtde mínima de caracteres.
    - EX2: E-mail tipo "c#zao" não deve ser aceito. Um e-mail válido deve ter pelo menos um caracter antes do @, um e somente um @, duas partes depois do @ e a última parte deve ter pelo menos dois caracteres.
    - EX3: Se houver um campo que é numérico, não deve ser aceito caracteres.
  - Senhas não devem ser exibidas nem armazenadas em claro. Ou seja, criptografia na hora de salvar a senha. Se houver um e-mail de "Esqueci minha senha" não envie um e-mail tipo "Sua senha é c@iog0st0z".
- 👥 Clientes (CRUD)
  - Existem cidades de CEP único. Existem CEPs que podem estar desatualizados na API. Sendo assim, qualquer automação no preenchimento de Rua/Bairro/Cidade etc deve ser meramente "sugestão" (ou seja, serve pra agilizar o processo mas os campos ainda devem ser editáveis e ainda devem ser armazenados em banco).
  - Na Listagem de clientes não devem ser exibidos todos os dados do cliente, somente os mais pertinentes. Se o CPF for exibido, o ideal é ocultar os últimos caracteres (pelo menos na tela principal).
  - Caso você faça a importação de dados via tela, não esqueça de confrontar com os clientes já existentes e exibir uma tela de "crítica". Ou seja, uma tela listando os clientes a serem importados e se já existem no sistema ou não com um checkbox de confirmação para cada cliente.
- 🔑 Usuários (Controle de sessão e de acessos)
  - A partir do momento que há um controle de acesso, nenhuma página do sistema (mesmo as do CRUD) devem ser acessíveis para usuários não logados. Qualquer tentativa deve redirecionar o usuário para a tela de login.
  - Tenha sempre em sessão o perfil do usuário. Algumas funcionalidades só serão acessíveis aos "super usuários" (ADM e supervisores).
  - O ideal seria o e-mail de "convite" conter um link com token único, mas também será aceito se o e-mail da pessoa só ficar numa lista de usuários que podem se cadastrar.
  - Logs do sistema: Sim... tudo que é função que altera dados deve ser logada. A exibição em tela pode ser bem simples, mas é importante que os dados estejam lá e que seja possível filtrar o período do log.
- 💌 Relacionamento
  - Deve ser possível usar mais de um filtro por vez. Ex: quero filtrar apenas clientes nascidos entre 1990 e 1999 E que sejam do gênero masculino.
  - Exportação em PDF pode ser tão simples quanto aquela do balanço, ou seja, na verdade é uma tela HTML normal mas "otimizada" para caber em folha de papel, sem muitas cores, de fundo preferencialmente branco e sem nenhum botão de ação. Aí é só chamar o window.print() que é sucesso!
  - Histórico/Anotação pode ser bem simples. A ideia é poder anotar coisas como "Cliente só compra parcelado" ou "Digital Influencer - lembrar de mandar promoções primeiro pra esse cliente".
  - Pesquisa NPS é uma pesquisa de satisfação com algumas perguntas objetivas e nota de 0 a 10. A ideia é mandar um link pra pessoa abrir uma página com um token. Esse token será a "autenticação", ou seja, não devem ser usuários com usuário e senha a fazer a pesquisa mas sim os clientes finais.

## ✅ **DOs & DON'Ts** 🚫
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nessa SA vocês poderão fazer uso de inteligências artificiais generativas e templates da web. Kits de imagens e ícones também são aceitos. Pedir ajuda para os colegas de outras equipes também vale. Só não é aceito literalmente copiar o fonte de outras equipes ou utilizar Frameworks que “encurtem” o trabalho poupando-os de lidar com SQL (como Laravel). Também não é permitido usar outras linguagens de programação. A stack é **PHP, HTML, JS, CSS e MySQL**. Só faça em Python se você quiser zerar :}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O uso de localStorage será tolerado caso se faça extremamente necessário, mas nunca como substituto ao MySQL.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E o mais importante: não fique com dúvidas! Se tiver dúvida sobre qualquer um desses critérios, temas e funcionalidades, **pergunte!** Lembre-se: a SA aqui está simulando um trabalho profissional. Entregar algo diferente do que o cliente pediu simplesmente porque "ele não soube explicar o que queria" não muda o fato de que você dedicou horas pra fazer algo que ninguém pediu (e que é portanto inútil).

## 💅 **UI** 💅
- Não será exigido interface ~~nível Caio~~ super arrojada
- Será exigido
	- Alguma cor (pelo menos um pouco de estilo 🏳️‍🌈)
   	- Padronização (todas as telas devem parecer ser do mesmo sistema 🧩)
   	- Controle via JS de eventos no Front End

## 📑 **Sugestão de organização de atividades** 📑
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Comecem projetando o banco de dados. Pensem em quais telas o sistema terá. Pensem em como será cada tela (como serão os formulários? como serão os botões? Vai ter rodapé, topo, barra esquerda recolhível?). Em seguida, tente identificar que conhecimentos você deveria ter para conseguir fazer tudo isso e então peça pro professor focar as próximas aulas nesses temas.


## 🗓️ **Calendário Oficial** 🗓️
Consulte o [Calendário oficial](https://rodrigocane.github.io/) para se organizar. Mas atenção: esse calendário está sujeito a alterações sem aviso prévio conforme o engajamento da turma!
