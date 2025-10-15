CREATE TABLE conta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL,
    digito CHAR(1) NOT NULL,
    titular VARCHAR(250) NOT NULL,
    saldo_atual DECIMAL(10,2) NOT NULL DEFAULT 0,
    UNIQUE KEY (numero, digito)
);

CREATE TABLE operacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME NOT NULL DEFAULT NOW(),
    id_conta_origem INT NOT NULL,
    id_conta_destino INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    CHECK (id_conta_origem <> id_conta_destino),
    CHECK (valor > 0),
    FOREIGN KEY (id_conta_origem) REFERENCES conta(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_conta_destino) REFERENCES conta(id)  ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO conta (numero, digito, titular, saldo_atual) VALUES 
(17, 1,'Alan Capone', 10000.0), (61, 6,'Stanley Lieber', 1000.0), (169, 9,'Kevin Spacey', 1.0),
(99, 9,'Zed Zidane', 600000.0), (1, 1,'Martin Luther', 1.0), (88, 0,'Luciano A. Van', 88888.0);