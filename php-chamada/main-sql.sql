CREATE DATABASE IF NOT EXISTS chamada;
USE chamada;

-- Tabela de Alunos
CREATE TABLE Aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    dataNascimento DATE NOT NULL
);

-- Tabela de Dias Letivos
CREATE TABLE DiaLetivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL UNIQUE
);

-- Tabela associativa Presença (ligação entre Aluno e DiaLetivo)
CREATE TABLE Presenca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    dia_letivo_id INT NOT NULL,
    aula ENUM('1', '2', '3', '4') NOT NULL,
    presente BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (aluno_id) REFERENCES Aluno(id) ON DELETE CASCADE,
    FOREIGN KEY (dia_letivo_id) REFERENCES DiaLetivo(id) ON DELETE CASCADE,
    UNIQUE (aluno_id, dia_letivo_id, aula) -- Evita duplicação da mesma aula
);

--Carga Inicial
SET @dataInicio = CURDATE(); -- Data de hoje
SET @dataFim = '2025-07-02'; -- Data final

-- Criando tabela temporária para armazenar os dias letivos
CREATE TEMPORARY TABLE TempDiasLetivos (data DATE);

-- Loop para gerar todas as terças, quartas e sextas úteis
WHILE @dataInicio <= @dataFim DO
    -- Se for terça (2), quarta (3) ou sexta (5) e não for sábado (6) ou domingo (7)
    IF WEEKDAY(@dataInicio) IN (1,2,4) THEN
        INSERT INTO TempDiasLetivos (data) VALUES (@dataInicio);
    END IF;
    -- Avança para o próximo dia
    SET @dataInicio = DATE_ADD(@dataInicio, INTERVAL 1 DAY);
END WHILE;

-- Inserindo os dias úteis na tabela DiaLetivo
INSERT INTO DiaLetivo (data)
SELECT data FROM TempDiasLetivos;

-- Limpando a tabela temporária
DROP TEMPORARY TABLE TempDiasLetivos;

INSERT INTO Aluno (nome, dataNascimento) VALUES
('Ana Andrade', '2009-01-15'),  -- 16 anos
('Bruno Biz de Barros', '2008-02-22'),  -- 17 anos
('Carla Cardoso', '2007-03-10'),  -- 18 anos
('Daniel Dantas', '2006-04-05'),  -- 19 anos
('Eduardo Esteves', '2005-05-18'),  -- 20 anos
('Fernando Fernandes', '2004-06-30'),  -- 21 anos
('Gabriel Giovanella', '2003-07-12'),  -- 22 anos
('Heloísa Hess', '2002-08-25'),  -- 23 anos
('Igor Igarashi', '2001-09-14'),  -- 24 anos
('Jordana Jordão', '2000-10-08'),  -- 25 anos
('Kleber Kalil', '1999-11-19'),  -- 26 anos
('Lana Lang', '1998-12-03'),  -- 27 anos
('Mariana Matos', '1997-01-29'),  -- 28 anos
('Natália Nogueira', '1996-02-17'),  -- 29 anos
('Otávio Oliveira', '1995-03-21'),  -- 30 anos
('Patrícia Poeta', '2009-04-09'),  -- 16 anos
('Quênia Queiroz', '2008-05-27'),  -- 17 anos
('Rodrigo Rodrigues', '2007-06-15'),  -- 18 anos
('Sabrina Sato', '2006-07-23'),  -- 19 anos
('Tiago Tavares', '2005-08-30'),  -- 20 anos
('Ursula Uchôa', '2004-09-11'),  -- 21 anos
('Vinícius Vasconcelos', '2003-10-04'),  -- 22 anos
('Wesley Werlich', '2002-11-16'),  -- 23 anos
('Xênia Xavier', '2001-12-28'),  -- 24 anos
('Yago Yamada', '2000-01-06'),  -- 25 anos
('Zilda Zambrano', '1999-02-14');  -- 26 anos