CREATE DATABASE `balanco`;

USE `balanco`;

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ean VARCHAR(13) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE balanco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE balanco_produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    balanco_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade_aferida INT NOT NULL,
    FOREIGN KEY (balanco_id) REFERENCES balanco(id) ON DELETE CASCADE,
    FOREIGN KEY (produto_id) REFERENCES produto(id) ON DELETE CASCADE,
    UNIQUE (balanco_id, produto_id) /* Garante que um mesmo produto só tenha um registro por balanço*/
);

INSERT INTO produto (ean, nome) VALUES
('7891000100100', 'Refrigerante de Cola 350ml'),
('7894900010014', 'Arroz Tipo 1 5kg'),
('7891000240102', 'Sabonete 90g'),
('7891991010103', 'Leite Integral 1L'),
('7892840800108', 'Papel Higiênico 12 rolos'),
('7891000050015', 'Café Tradicional 500g'),
('7891000100109', 'Achocolatado em Pó 400g'),
('7894900010015', 'Óleo de Soja 900ml'),
('7891000100109', 'Achocolatado em Pó 400g'),
('6925281986160', 'Fone de Ouvido Bluetooth'),
('0190286592990', 'Mochila Old School II');

INSERT INTO balanco (data_registro) VALUES (NOW());

INSERT INTO balanco_produto (balanco_id, produto_id, quantidade_aferida) VALUES
(1, 1, 11),
(1, 2, 22),
(1, 3, 33),
(1, 4, 44),
(1, 5, 55);