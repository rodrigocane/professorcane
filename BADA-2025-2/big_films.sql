CREATE TABLE filme (
	id INT AUTO_INCREMENT PRIMARY KEY,
	titulo_original VARCHAR(150) NOT NULL,
	titulo_portugues VARCHAR(150) NULL,
	ano_lancamento INT NOT NULL,
	link VARCHAR(2048),
	opiniao ENUM(
		'Não posso opinar',
		'Não vi e não tenho interesse',
		'Não vi e tenho interesse em ver',
		'Vi e não gostei',
		'Vi e gostei'
	) NOT NULL DEFAULT 'Não posso opinar',
	UNIQUE KEY (titulo_original, ano_lancamento)
);

INSERT INTO filme (titulo_original, titulo_portugues, ano_lancamento) VALUES
('The Matrix', 'Matrix', 1999),
('Fight Club', 'Clube da Luta', 1999),
('Inception', 'A Origem', 2010),
('Memento', 'Amnésia', 2000),
('Predestination', 'O Predestinado', 2014), 
('The Shining', 'O Iluminado', 1980),
('Full Metal Jacket', 'Nascido para Matar', 1987),
('Se7en', 'Seven: Os Sete Crimes Capitais', 1995),
('Pulp Fiction', 'Pulp Fiction: Tempo de Violência', 1994), 
('Reservoir Dogs', 'Cães de Aluguel', 1992), 
('Once Upon a Time in Hollywood', 'Era uma vez em... Hollywood', 2019),
('Catch Me If You Can', 'Prenda-me Se For Capaz', 2002),
('Aliens', 'Aliens, O Resgate', 1986),
('Alien', 'Alien, O Oitavo Passageiro', 1979),
('Terminator 2: Judgment Day', 'O Exterminador do Futuro 2: O Julgamento Final', 1991),
('The Terminator', 'O Exterminador do Futuro', 1984);

INSERT INTO filme (titulo_original, titulo_portugues, ano_lancamento) VALUES
('Oppenheimer', 'Oppenheimer', 2023),
('Everything Everywhere All at Once', 'Tudo em Todo o Lugar ao Mesmo Tempo', 2022),
('CODA', 'No Ritmo do Coração', 2021),
('Nomadland', 'Nomadland', 2020),
('Parasite', 'Parasita', 2019),
('Green Book', 'Green Book: O Guia', 2018),
('The Shape of Water', 'A Forma da Água', 2017),
('Moonlight', 'Moonlight: Sob a Luz do Luar', 2016),
('Spotlight', 'Spotlight: Segredos Revelados', 2015),
('Birdman', 'Birdman ou (A Inesperada Virtude da Ignorância)', 2014),
('12 Years a Slave', '12 Anos de Escravidão', 2013),
('Argo', 'Argo', 2012),
('The Artist', 'O Artista', 2011),
('The King''s Speech', 'O Discurso do Rei', 2010),
('The Hurt Locker', 'Guerra ao Terror', 2009),
('Slumdog Millionaire', 'Quem Quer Ser um Milionário?', 2008),
('No Country for Old Men', 'Onde os Fracos Não Têm Vez', 2007),
('The Departed', 'Os Infiltrados', 2006),
('Crash', 'Crash: No Limite', 2005),
('Million Dollar Baby', 'Menina de Ouro', 2004),
('The Lord of the Rings: The Return of the King', 'O Senhor dos Anéis: O Retorno do Rei', 2003),
('Chicago', 'Chicago', 2002),
('A Beautiful Mind', 'Uma Mente Brilhante', 2001),
('Gladiator', 'Gladiador', 2000),
('American Beauty', 'Beleza Americana', 1999),
('Shakespeare in Love', 'Shakespeare Apaixonado', 1998),
('Titanic', 'Titanic', 1997),
('The English Patient', 'O Paciente Inglês', 1996),
('Braveheart', 'Coração Valente', 1995),
('Forrest Gump', 'Forrest Gump: O Contador de Histórias', 1994),
('Schindler''s List', 'A Lista de Schindler', 1993),
('Unforgiven', 'Os Imperdoáveis', 1992),
('The Silence of the Lambs', 'O Silêncio dos Inocentes', 1991),
('Dances with Wolves', 'Dança com Lobos', 1990);

INSERT INTO filme (titulo_original, titulo_portugues, ano_lancamento) VALUES
('Insomnia', 'Insônia', 2002),
('Batman Begins', 'Batman Begins', 2005),
('The Prestige', 'O Grande Truque', 2006),
('The Dark Knight', 'Batman: O Cavaleiro das Trevas', 2008),
('The Dark Knight Rises', 'Batman: O Cavaleiro das Trevas Ressurge', 2012),
('Interstellar', 'Interestelar', 2014),
('Dunkirk', 'Dunkirk', 2017),
('Tenet', 'Tenet', 2020),
('Jackie Brown', 'Jackie Brown', 1997),
('Kill Bill: Vol. 1', 'Kill Bill: Volume 1', 2003),
('Kill Bill: Vol. 2', 'Kill Bill: Volume 2', 2004),
('Death Proof', 'À Prova de Morte', 2007),
('Inglourious Basterds', 'Bastardos Inglórios', 2009),
('Django Unchained', 'Django Livre', 2012),
('The Hateful Eight', 'Os Oito Odiados', 2015),
('Taxi Driver', 'Taxi Driver - Motorista de Táxi', 1976),
('Raging Bull', 'Touro Indomável', 1980),
('The King of Comedy', 'O Rei da Comédia', 1982),
('After Hours', 'Depois de Horas', 1985),
('The Color of Money', 'A Cor do Dinheiro', 1986),
('The Last Temptation of Christ', 'A Última Tentação de Cristo', 1988),
('Goodfellas', 'Os Bons Companheiros', 1990),
('Cape Fear', 'Cabo do Medo', 1991),
('The Age of Innocence', 'A Época da Inocência', 1993),
('Casino', 'Cassino', 1995),
('Kundun', 'Kundun', 1997),
('Bringing Out the Dead', 'Vivendo no Limite', 1999),
('Gangs of New York', 'Gangues de Nova York', 2002),
('The Aviator', 'O Aviador', 2004),
('Shutter Island', 'Ilha do Medo', 2010),
('Hugo', 'A Invenção de Hugo Cabret', 2011),
('The Wolf of Wall Street', 'O Lobo de Wall Street', 2013),
('Silence', 'Silêncio', 2016),
('The Irishman', 'O Irlandês', 2019),
('Killers of the Flower Moon', 'Assassinos da Lua das Flores', 2023),
('Star Wars: Episode IV – A New Hope', 'Star Wars: Uma Nova Esperança', 1977),
('Star Wars: Episode V – The Empire Strikes Back', 'Star Wars: O Império Contra-Ataca', 1980),
('Star Wars: Episode VI – Return of the Jedi', 'Star Wars: O Retorno de Jedi', 1983),
('Star Wars: Episode I – The Phantom Menace', 'Star Wars: A Ameaça Fantasma', 1999),
('Star Wars: Episode II – Attack of the Clones', 'Star Wars: Ataque dos Clones', 2002),
('Star Wars: Episode III – Revenge of the Sith', 'Star Wars: A Vingança dos Sith', 2005),
('Star Wars: Episode VII – The Force Awakens', 'Star Wars: O Despertar da Força', 2015),
('Rogue One: A Star Wars Story', 'Rogue One: Uma História Star Wars', 2016),
('Star Wars: Episode VIII – The Last Jedi', 'Star Wars: Os Últimos Jedi', 2017),
('Solo: A Star Wars Story', 'Han Solo: Uma História Star Wars', 2018),
('Star Wars: Episode IX – The Rise of Skywalker', 'Star Wars: A Ascensão Skywalker', 2019),
('Ace Ventura: Pet Detective', 'Ace Ventura: Um Detetive Diferente', 1994),
('The Mask', 'O Máskara', 1994),
('Dumb and Dumber', 'Debi & Lóide: Dois Idiotas em Apuros', 1994),
('Batman Forever', 'Batman Eternamente', 1995),
('The Cable Guy', 'O Pentelho', 1996),
('Liar Liar', 'O Mentiroso', 1997),
('The Truman Show', 'O Show de Truman', 1998),
('Man on the Moon', 'O Mundo de Andy', 1999),
('How the Grinch Stole Christmas', 'O Grinch', 2000),
('Bruce Almighty', 'Todo Poderoso', 2003),
('Eternal Sunshine of the Spotless Mind', 'Brilho Eterno de uma Mente Sem Lembranças', 2004),
('A Series of Unfortunate Events', 'Desventuras em Série', 2004),
('Yes Man', 'Sim Senhor', 2008),
('When Harry Met Sally...', 'Harry e Sally - Feitos Um para o Outro', 1989),
('Pretty Woman', 'Uma Linda Mulher', 1990),
('Sleepless in Seattle', 'Sintonia de Amor', 1993),
('Notting Hill', 'Um Lugar Chamado Notting Hill', 1999),
('10 Things I Hate About You', '10 Coisas Que Eu Odeio em Você', 1999),
('Legally Blonde', 'Legalmente Loira', 2001),
('Sweet Home Alabama', 'Doce Lar', 2002),
('Love Actually', 'Simplesmente Amor', 2003),
('50 First Dates', 'Como Se Fosse A Primeira Vez', 2004),
('The Proposal', 'A Proposta', 2009),
('Crazy, Stupid, Love.', 'Amor a Toda Prova', 2011),
('La La Land', 'La La Land: Cantando Estações', 2016);

-- #################################################
-- 1. DDL: RECRIAÇÃO E CRIAÇÃO DAS TABELAS
-- #################################################

-- A - Criação da tabela Diretor (1:N)
CREATE TABLE diretor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    UNIQUE KEY (nome)
);

-- B - Criação da tabela Ator (N:N)
CREATE TABLE ator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    UNIQUE KEY (nome)
);

-- C - Criação da tabela Genero (N:N)
CREATE TABLE genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    UNIQUE KEY (nome)
);

-- D - Adiciona a chave estrangeira do Diretor na tabela Filme (1:N)
ALTER TABLE filme
ADD COLUMN id_diretor INT NULL,
ADD FOREIGN KEY (id_diretor) REFERENCES diretor(id) ON DELETE SET NULL;

-- E - Tabela Associativa para Elenco (N:N entre Filme e Ator)
CREATE TABLE elenco (
    id_filme INT NOT NULL,
    id_ator INT NOT NULL,
    principal TINYINT(1) NOT NULL DEFAULT 0 COMMENT '1=Principal, 0=Coadjuvante',
    PRIMARY KEY (id_filme, id_ator),
    FOREIGN KEY (id_filme) REFERENCES filme(id) ON DELETE CASCADE,
    FOREIGN KEY (id_ator) REFERENCES ator(id) ON DELETE CASCADE
);

-- F - Tabela Associativa para Gênero do Filme (N:N entre Filme e Genero)
CREATE TABLE filme_genero (
    id_filme INT NOT NULL,
    id_genero INT NOT NULL,
    PRIMARY KEY (id_filme, id_genero),
    FOREIGN KEY (id_filme) REFERENCES filme(id) ON DELETE CASCADE,
    FOREIGN KEY (id_genero) REFERENCES genero(id) ON DELETE CASCADE
);


-- #################################################
-- 2. DML: INSERÇÃO DE DADOS
-- #################################################

-- 2.1 INSERÇÃO DE DIRETORES
INSERT INTO diretor (nome) VALUES
('Lana Wachowski'), ('Lilly Wachowski'),
('David Fincher'),
('Christopher Nolan'),
('Michael Spierig'), ('Peter Spierig'),
('Stanley Kubrick'),
('Quentin Tarantino'),
('Steven Spielberg'),
('James Cameron'),
('Ridley Scott'),
('Siân Heder'),
('Chloé Zhao'),
('Bong Joon-ho'),
('Peter Farrelly'),
('Guillermo del Toro'),
('Barry Jenkins'),
('Tom McCarthy'),
('Alejandro G. Iñárritu'),
('Steve McQueen'),
('Ben Affleck'),
('Michel Hazanavicius'),
('Tom Hooper'),
('Kathryn Bigelow'),
('Danny Boyle'),
('Joel Coen'), ('Ethan Coen'),
('Martin Scorsese'),
('Paul Haggis'),
('Clint Eastwood'),
('Peter Jackson'),
('Rob Marshall'),
('Ron Howard'),
('Sam Mendes'),
('John Madden'),
('Anthony Minghella'),
('Mel Gibson'),
('Robert Zemeckis'),
('Jonathan Demme'),
('Kevin Costner'),
('George Lucas'),
('JJ Abrams'),
('Gareth Edwards'),
('Rian Johnson'),
('Jim Abrahams'),
('Chuck Russell'),
('Joel Schumacher'),
('Ben Stiller'),
('Tom Shadyac'),
('Peter Weir'),
('Milos Forman'),
('Michel Gondry'),
('Brad Silberling'),
('Peyton Reed'),
('Rob Reiner'),
('Garry Marshall'),
('Nora Ephron'),
('Roger Michell'),
('Gil Junger'),
('Robert Luketic'),
('Andy Tennant'),
('Richard Curtis'),
('Peter Segal'),
('Anne Fletcher'),
('Glenn Ficarra'), ('John Requa'),
('Damien Chazelle'),
('Daniel Kwan'), ('Daniel Scheinert');


-- 2.2 ASSOCIAÇÃO DIRETORES (UPDATE NA TABELA FILME)
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Lana Wachowski') WHERE titulo_original = 'The Matrix';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'David Fincher') WHERE titulo_original IN ('Fight Club', 'Se7en');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Christopher Nolan') WHERE titulo_original IN (
    'Inception', 'Memento', 'The Prestige', 'Batman Begins', 'The Dark Knight', 'The Dark Knight Rises',
    'Interstellar', 'Dunkirk', 'Tenet', 'Insomnia', 'Oppenheimer'
);
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Michael Spierig') WHERE titulo_original = 'Predestination';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Stanley Kubrick') WHERE titulo_original IN ('The Shining', 'Full Metal Jacket');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Quentin Tarantino') WHERE titulo_original IN (
    'Pulp Fiction', 'Reservoir Dogs', 'Once Upon a Time in Hollywood', 'Jackie Brown', 'Kill Bill: Vol. 1',
    'Kill Bill: Vol. 2', 'Death Proof', 'Inglourious Basterds', 'Django Unchained', 'The Hateful Eight'
);
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Steven Spielberg') WHERE titulo_original IN ('Catch Me If You Can', 'Schindler\'s List');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'James Cameron') WHERE titulo_original IN ('Aliens', 'Terminator 2: Judgment Day', 'Titanic');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Ridley Scott') WHERE titulo_original IN ('Alien', 'Gladiator');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Daniel Kwan') WHERE titulo_original = 'Everything Everywhere All at Once';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Siân Heder') WHERE titulo_original = 'CODA';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Chloé Zhao') WHERE titulo_original = 'Nomadland';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Bong Joon-ho') WHERE titulo_original = 'Parasite';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peter Farrelly') WHERE titulo_original = 'Green Book';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Guillermo del Toro') WHERE titulo_original = 'The Shape of Water';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Barry Jenkins') WHERE titulo_original = 'Moonlight';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Tom McCarthy') WHERE titulo_original = 'Spotlight';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Alejandro G. Iñárritu') WHERE titulo_original = 'Birdman';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Steve McQueen') WHERE titulo_original = '12 Years a Slave';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Ben Affleck') WHERE titulo_original = 'Argo';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Michel Hazanavicius') WHERE titulo_original = 'The Artist';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Tom Hooper') WHERE titulo_original = 'The King\'s Speech';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Kathryn Bigelow') WHERE titulo_original = 'The Hurt Locker';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Danny Boyle') WHERE titulo_original = 'Slumdog Millionaire';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Joel Coen') WHERE titulo_original = 'No Country for Old Men';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Martin Scorsese') WHERE titulo_original IN (
    'The Departed', 'Taxi Driver', 'Raging Bull', 'The King of Comedy', 'After Hours', 'The Color of Money',
    'The Last Temptation of Christ', 'Goodfellas', 'Cape Fear', 'The Age of Innocence', 'Casino', 'Kundun',
    'Bringing Out the Dead', 'Gangs of New York', 'The Aviator', 'Shutter Island', 'Hugo', 'The Wolf of Wall Street',
    'Silence', 'The Irishman', 'Killers of the Flower Moon'
);
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Paul Haggis') WHERE titulo_original = 'Crash';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Clint Eastwood') WHERE titulo_original IN ('Million Dollar Baby', 'Unforgiven');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peter Jackson') WHERE titulo_original = 'The Lord of the Rings: The Return of the King';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Rob Marshall') WHERE titulo_original = 'Chicago';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Ron Howard') WHERE titulo_original IN ('A Beautiful Mind', 'How the Grinch Stole Christmas');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Sam Mendes') WHERE titulo_original = 'American Beauty';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'John Madden') WHERE titulo_original = 'Shakespeare in Love';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Anthony Minghella') WHERE titulo_original = 'The English Patient';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Mel Gibson') WHERE titulo_original = 'Braveheart';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Robert Zemeckis') WHERE titulo_original = 'Forrest Gump';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Jonathan Demme') WHERE titulo_original = 'The Silence of the Lambs';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Kevin Costner') WHERE titulo_original = 'Dances with Wolves';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'George Lucas') WHERE titulo_original LIKE 'Star Wars: Episode %';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'JJ Abrams') WHERE titulo_original IN ('Star Wars: Episode VII – The Force Awakens', 'Star Wars: Episode IX – The Rise of Skywalker');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Gareth Edwards') WHERE titulo_original = 'Rogue One: A Star Wars Story';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Rian Johnson') WHERE titulo_original = 'Star Wars: Episode VIII – The Last Jedi';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Ron Howard') WHERE titulo_original = 'Solo: A Star Wars Story';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Jim Abrahams') WHERE titulo_original = 'Ace Ventura: Pet Detective';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Chuck Russell') WHERE titulo_original = 'The Mask';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peter Farrelly') WHERE titulo_original = 'Dumb and Dumber';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Joel Schumacher') WHERE titulo_original = 'Batman Forever';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Ben Stiller') WHERE titulo_original = 'The Cable Guy';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Tom Shadyac') WHERE titulo_original IN ('Liar Liar', 'Bruce Almighty');
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peter Weir') WHERE titulo_original = 'The Truman Show';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Milos Forman') WHERE titulo_original = 'Man on the Moon';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Michel Gondry') WHERE titulo_original = 'Eternal Sunshine of the Spotless Mind';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Brad Silberling') WHERE titulo_original = 'A Series of Unfortunate Events';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peyton Reed') WHERE titulo_original = 'Yes Man';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Rob Reiner') WHERE titulo_original = 'When Harry Met Sally...';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Garry Marshall') WHERE titulo_original = 'Pretty Woman';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Nora Ephron') WHERE titulo_original = 'Sleepless in Seattle';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Roger Michell') WHERE titulo_original = 'Notting Hill';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Gil Junger') WHERE titulo_original = '10 Things I Hate About You';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Robert Luketic') WHERE titulo_original = 'Legally Blonde';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Andy Tennant') WHERE titulo_original = 'Sweet Home Alabama';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Richard Curtis') WHERE titulo_original = 'Love Actually';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Peter Segal') WHERE titulo_original = '50 First Dates';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Anne Fletcher') WHERE titulo_original = 'The Proposal';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Glenn Ficarra') WHERE titulo_original = 'Crazy, Stupid, Love.';
UPDATE filme SET id_diretor = (SELECT id FROM diretor WHERE nome = 'Damien Chazelle') WHERE titulo_original = 'La La Land';


-- 2.3 INSERÇÃO DE GÊNEROS
INSERT INTO genero (nome) VALUES
('Ficção Científica'),
('Ação'),
('Drama'),
('Suspense'),
('Terror'),
('Comédia'),
('Romance'),
('Guerra'),
('Crime'),
('Faroeste'),
('Biografia'),
('Fantasia'),
('Musical'),
('Mistério');


-- 2.4 INSERÇÃO DE ATORES/ATRIZES
INSERT INTO ator (nome) VALUES
('Keanu Reeves'),
('Laurence Fishburne'),
('Edward Norton'),
('Brad Pitt'),
('Leonardo DiCaprio'),
('Guy Pearce'),
('Ethan Hawke'),
('Jack Nicholson'),
('Matthew Modine'),
('Morgan Freeman'),
('Samuel L. Jackson'),
('John Travolta'),
('Tim Roth'),
('Bruce Willis'),
('Tom Hanks'),
('Arnold Schwarzenegger'),
('Sigourney Weaver'),
('Cillian Murphy'),
('Robert Downey Jr.'),
('Michelle Yeoh'),
('Jamie Lee Curtis'),
('Emilia Jones'),
('Frances McDormand'),
('Song Kang-ho'),
('Viggo Mortensen'),
('Mahershala Ali'),
('Sally Hawkins'),
('Emma Stone'),
('Michael Keaton'),
('Chiwetel Ejiofor'),
('Ben Affleck'),
('Jean Dujardin'),
('Colin Firth'),
('Jeremy Renner'),
('Dev Patel'),
('Javier Bardem'),
('Matt Damon'),
('Don Cheadle'),
('Clint Eastwood'),
('Elijah Wood'),
('Renée Zellweger'),
('Russell Crowe'),
('Kevin Spacey'),
('Joseph Fiennes'),
('Ralph Fiennes'),
('Mel Gibson'),
('Anthony Hopkins'),
('Jodie Foster'),
('Jim Carrey'),
('Jeff Daniels'),
('Cameron Diaz'),
('Uma Thurman'),
('Jamie Foxx'),
('Harrison Ford'),
('Mark Hamill'),
('Carrie Fisher'),
('Billy Dee Williams'),
('Daisy Ridley'),
('Adam Driver'),
('Felicity Jones'),
('Alden Ehrenreich'),
('Donald Glover'),
('Ryan Gosling'),
('Steve Carell'),
('Sandra Bullock'),
('Ryan Reynolds'),
('Kate Winslet'),
('Meg Ryan'),
('Billy Crystal'),
('Julia Roberts'),
('Hugh Grant'),
('Heath Ledger'),
('Reese Witherspoon'),
('Adam Sandler'),
('Drew Barrymore');


-- 2.5 INSERÇÃO NA TABELA ASSOCIATIVA filme_genero
INSERT INTO filme_genero (id_filme, id_genero)
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Matrix' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Matrix' AND g.nome = 'Ação' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Fight Club' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Fight Club' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Inception' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Inception' AND g.nome = 'Ação' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Memento' AND g.nome = 'Mistério' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Memento' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Predestination' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Predestination' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Shining' AND g.nome = 'Terror' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Shining' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Full Metal Jacket' AND g.nome = 'Guerra' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Full Metal Jacket' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Se7en' AND g.nome = 'Crime' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Se7en' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Pulp Fiction' AND g.nome = 'Crime' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Pulp Fiction' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Catch Me If You Can' AND g.nome = 'Biografia' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Catch Me If You Can' AND g.nome = 'Crime' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Aliens' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Aliens' AND g.nome = 'Ação' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Oppenheimer' AND g.nome = 'Biografia' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Oppenheimer' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Everything Everywhere All at Once' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Everything Everywhere All at Once' AND g.nome = 'Ação' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Everything Everywhere All at Once' AND g.nome = 'Comédia' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Silence of the Lambs' AND g.nome = 'Suspense' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Silence of the Lambs' AND g.nome = 'Crime' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Forrest Gump' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Titanic' AND g.nome = 'Romance' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Titanic' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Departed' AND g.nome = 'Crime' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Departed' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Truman Show' AND g.nome = 'Comédia' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'The Truman Show' AND g.nome = 'Drama' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Eternal Sunshine of the Spotless Mind' AND g.nome = 'Romance' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'Eternal Sunshine of the Spotless Mind' AND g.nome = 'Ficção Científica' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'La La Land' AND g.nome = 'Musical' UNION ALL
SELECT f.id, g.id FROM filme f, genero g WHERE f.titulo_original = 'La La Land' AND g.nome = 'Romance';


-- 2.6 INSERÇÃO NA TABELA ASSOCIATIVA elenco (N:N com 'principal')
INSERT INTO elenco (id_filme, id_ator, principal)
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Matrix' AND a.nome = 'Keanu Reeves' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Matrix' AND a.nome = 'Laurence Fishburne' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Fight Club' AND a.nome = 'Edward Norton' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Fight Club' AND a.nome = 'Brad Pitt' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Inception' AND a.nome = 'Leonardo DiCaprio' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Pulp Fiction' AND a.nome = 'John Travolta' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Pulp Fiction' AND a.nome = 'Uma Thurman' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Pulp Fiction' AND a.nome = 'Samuel L. Jackson' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Se7en' AND a.nome = 'Brad Pitt' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Se7en' AND a.nome = 'Morgan Freeman' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Se7en' AND a.nome = 'Kevin Spacey' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Titanic' AND a.nome = 'Leonardo DiCaprio' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Titanic' AND a.nome = 'Kate Winslet' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'La La Land' AND a.nome = 'Ryan Gosling' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'La La Land' AND a.nome = 'Emma Stone' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Oppenheimer' AND a.nome = 'Cillian Murphy' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Oppenheimer' AND a.nome = 'Robert Downey Jr.' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Everything Everywhere All at Once' AND a.nome = 'Michelle Yeoh' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Everything Everywhere All at Once' AND a.nome = 'Jamie Lee Curtis' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Truman Show' AND a.nome = 'Jim Carrey' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Eternal Sunshine of the Spotless Mind' AND a.nome = 'Jim Carrey' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Eternal Sunshine of the Spotless Mind' AND a.nome = 'Kate Winslet' UNION ALL

SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = '50 First Dates' AND a.nome = 'Adam Sandler' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = '50 First Dates' AND a.nome = 'Drew Barrymore';

-- #################################################
-- 1. DML: INSERÇÃO DE NOVOS ATORES (COMPLEMENTO)
-- #################################################

-- Inserção de atores que não estavam na lista inicial
INSERT INTO ator (nome) VALUES
('Shelley Duvall'),
('Harvey Keitel'),
('Margot Robbie'),
('Robert De Niro'),
('Kurt Russell'),
('Christoph Waltz'),
('Liam Neeson'),
('Mark Ruffalo'),
('Lupita Nyong\'o'),
('Josh Brolin'),
('Hilary Swank'),
('Gwyneth Paltrow'),
('Val Kilmer'),
('Jennifer Aniston'),
('Zooey Deschanel'),
('Alan Rickman'),
('Richard Gere')
ON DUPLICATE KEY UPDATE nome=nome; -- Garante que atores já inseridos (como Robert De Niro) não causem erro.


-- #################################################
-- 2. DML: INSERÇÃO NA TABELA ASSOCIATIVA elenco (COMPLEMENTO)
-- #################################################

-- Garante que todos os filmes listados agora tenham pelo menos um ator/atriz principal (principal=1)
INSERT INTO elenco (id_filme, id_ator, principal)
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Memento' AND a.nome = 'Guy Pearce' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Predestination' AND a.nome = 'Ethan Hawke' UNION ALL

-- The Shining
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Shining' AND a.nome = 'Jack Nicholson' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Shining' AND a.nome = 'Shelley Duvall' UNION ALL

-- Full Metal Jacket
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Full Metal Jacket' AND a.nome = 'Matthew Modine' UNION ALL

-- Reservoir Dogs
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Reservoir Dogs' AND a.nome = 'Tim Roth' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Reservoir Dogs' AND a.nome = 'Harvey Keitel' UNION ALL

-- Once Upon a Time in Hollywood
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Once Upon a Time in Hollywood' AND a.nome = 'Leonardo DiCaprio' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Once Upon a Time in Hollywood' AND a.nome = 'Margot Robbie' UNION ALL

-- Jackie Brown
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Jackie Brown' AND a.nome = 'Samuel L. Jackson' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Jackie Brown' AND a.nome = 'Robert De Niro' UNION ALL

-- Kill Bill Vol 1 e 2
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Kill Bill: Vol. 1' AND a.nome = 'Uma Thurman' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Kill Bill: Vol. 2' AND a.nome = 'Uma Thurman' UNION ALL

-- Inglourious Basterds
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Inglourious Basterds' AND a.nome = 'Christoph Waltz' UNION ALL

-- Django Unchained
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Django Unchained' AND a.nome = 'Jamie Foxx' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Django Unchained' AND a.nome = 'Christoph Waltz' UNION ALL

-- The Hateful Eight
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Hateful Eight' AND a.nome = 'Kurt Russell' UNION ALL

-- Schindler's List
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Schindler\'s List' AND a.nome = 'Liam Neeson' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Schindler\'s List' AND a.nome = 'Ralph Fiennes' UNION ALL

-- Terminator 2: Judgment Day
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Terminator 2: Judgment Day' AND a.nome = 'Arnold Schwarzenegger' UNION ALL

-- Alien
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Alien' AND a.nome = 'Sigourney Weaver' UNION ALL

-- Gladiator
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Gladiator' AND a.nome = 'Russell Crowe' UNION ALL

-- Vencedores do Oscar Recente
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'CODA' AND a.nome = 'Emilia Jones' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Nomadland' AND a.nome = 'Frances McDormand' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Parasite' AND a.nome = 'Song Kang-ho' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Shape of Water' AND a.nome = 'Sally Hawkins' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Moonlight' AND a.nome = 'Mahershala Ali' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Spotlight' AND a.nome = 'Mark Ruffalo' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = '12 Years a Slave' AND a.nome = 'Chiwetel Ejiofor' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Artist' AND a.nome = 'Jean Dujardin' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The King\'s Speech' AND a.nome = 'Colin Firth' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Hurt Locker' AND a.nome = 'Jeremy Renner' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Slumdog Millionaire' AND a.nome = 'Dev Patel' UNION ALL

-- Filmes de Scorsese/Nolan/Coen
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'No Country for Old Men' AND a.nome = 'Josh Brolin' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Departed' AND a.nome = 'Matt Damon' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Taxi Driver' AND a.nome = 'Robert De Niro' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Raging Bull' AND a.nome = 'Robert De Niro' UNION ALL

-- Filmes Vencedores do Oscar
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Million Dollar Baby' AND a.nome = 'Hilary Swank' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Unforgiven' AND a.nome = 'Clint Eastwood' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The Lord of the Rings: The Return of the King' AND a.nome = 'Elijah Wood' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Chicago' AND a.nome = 'Renée Zellweger' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'A Beautiful Mind' AND a.nome = 'Russell Crowe' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'American Beauty' AND a.nome = 'Kevin Spacey' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Shakespeare in Love' AND a.nome = 'Gwyneth Paltrow' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'The English Patient' AND a.nome = 'Ralph Fiennes' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Braveheart' AND a.nome = 'Mel Gibson' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Dances with Wolves' AND a.nome = 'Kevin Costner' UNION ALL

-- Star Wars
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Star Wars: Episode IV – A New Hope' AND a.nome = 'Mark Hamill' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Star Wars: Episode VII – The Force Awakens' AND a.nome = 'Daisy Ridley' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Rogue One: A Star Wars Story' AND a.nome = 'Felicity Jones' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Solo: A Star Wars Story' AND a.nome = 'Alden Ehrenreich' UNION ALL

-- Comédias
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Batman Forever' AND a.nome = 'Val Kilmer' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Bruce Almighty' AND a.nome = 'Jennifer Aniston' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Yes Man' AND a.nome = 'Zooey Deschanel' UNION ALL

-- Romances/Comédias Românticas
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Pretty Woman' AND a.nome = 'Richard Gere' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Sleepless in Seattle' AND a.nome = 'Tom Hanks' UNION ALL
SELECT f.id, a.id, 1 FROM filme f, ator a WHERE f.titulo_original = 'Sleepless in Seattle' AND a.nome = 'Meg Ryan' UNION ALL
SELECT f.id, a.id, 0 FROM filme f, ator a WHERE f.titulo_original = 'Love Actually' AND a.nome = 'Alan Rickman'
ON DUPLICATE KEY UPDATE principal=VALUES(principal);
