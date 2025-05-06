# 🚀 **Situação de Aprendizagem - Desenvolvimento de Sistemas** 🚀

## 🧭 **Contexto** 🧭
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Na Situação de Aprendizagem deste semestre vocês desenvolverão um sistema de **CRM** (**C**ustomer **R**elationship **M**anagement) agnóstico, que pode ser usado pela sua mãe que vende Avon, pelo seu tio que vende marmita ou pelo barbeiro descolado da sua esquina. Esse sistema também poderia ser “acoplado” ao sistema do mercadinho do seu bairro ou talvez até ao próprio SENAI!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O sistema será de uso “interno” de um determinado empreendimento e/ou grupo econômico, podendo ser hospedado na nuvem ou em servidor local. Ou seja, não há uma preocupação quanto à usabilidade para usuários leigos, uma vez que espera-se que os usuários sejam treinados para utilizar o sistema.


## ⚙️ **Funcionalidades** ⚙️
- 🔑 Usuários
	- Login
	- Primeiro login ADM (troca de senha 🔑)
	- Convite de usuário (e-mail 📧)
	- Cadastro de usuário
	- Busca cep 📬
	- validação de e-mail 📧
	- Esqueci minha senha 🔑 (e-mail 📧 & token uso unico)
	- Gestão de usuários
	- Perfis: ADM (1 só), Supervisor e usuário
	- Logs do sistema (apenas para ADM e Supervisor)
- 👥 Clientes
	- Cadastro de cliente
	- Busca cep 📬
	- Validação de e-mail 📧
	- Listagem de clientes (filtros, paginação)
	- Alteração de cliente (usuário comum só pode alterar cliente que ele cadastrou)
	- Exclusão de Cliente usuário comum só pode excluir cliente que ele cadastrou)
	- Importar ↙️ (Rodada bônus 📈)
- 💌 Relacionamento
	- Listagem de clientes (filtros, paginação) [Sim é a mesma do 2b]
	- Exportar [precisa pelo menos uma] ↗️
	- Excel (Rodada bônus 📈)
	- JSON (Rodada bônus📈)
	- PDF
	- Histórico/Anotações/Comentários sobre Clientes
	- Pesquisa NPS (e-mail & token unico) (Rodada bônus 📈)
- 💻 API REST (Rodada bônus 📈)
	- GET
	- GET id
	- POST
	- PUT
	- DELETE


## 🤝 **Equipe** 🤝
- **Membros:** de um a quatro membros. Quanto mais membros, mais completo deverá ser o seu sistema.
- **Funcionalidades obrigatórias de acordo com a qtde de membros:**
  - (1) 👤: "Clientes"
  - (2) 👤👤: "Clientes" e "Login"
  - (3) 👤👤👤: "Login", "Clientes" e "Relacionamento"
  - (4) 👤👤👤👤: TUDO!!!

## 📦 **Entregáveis** 📦
1. Sistema funcional, commitado no GIT em repositório acessível pelo professor. Os commits devem ser feitos ao longo do semestre e por todos os integrantes da equipe. 🚀
2. Apresentação de até 15 minutos 🕒
3. ~~Documentação~~ não quero documentação "oficial" não. 📕

## ✅ **DOs & DON'Ts** 🚫
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nessa SA vocês poderão fazer uso de inteligências artificiais generativas e templates da web. Kits de imagens e ícones também são aceitos. Pedir ajuda para os colegas de outras equipes também vale. Só não é aceito literalmente copiar o fonte de outras equipes ou utilizar Frameworks que “encurtem” o trabalho poupando-os de lidar com SQL (como Laravel). Também não é permitido usar outras linguagens de programação. A stack é PHP, HTML, JS, CSS e MySQL. Só faça em Python se você quiser zerar :}

## 🗓️ **Sugestão de organização de atividades** 🗓️
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Comecem projetando o banco de dados. Pensem em quais telas o sistema terá. Pensem em como será cada tela (como serão os formulários? como serão os botões? Vai ter rodapé, topo, barra esquerda recolhível?). Em seguida, tente identificar que conhecimentos você deveria ter para conseguir fazer tudo isso e então peça pro professor focar as próximas aulas nesses temas.