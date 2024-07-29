-- Criação das tabelas
CREATE TABLE condominios (
    condominio_id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco TEXT NOT NULL
);

CREATE TABLE moradores (
    morador_id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    condominio_id INT NOT NULL,
    data_registro DATE NOT NULL,
    FOREIGN KEY (condominio_id) REFERENCES condominios(condominio_id)
);

CREATE TABLE imoveis (
    imovel_id SERIAL PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    condominio_id INT NOT NULL,
    valor NUMERIC(15, 2) NOT NULL,
    FOREIGN KEY (condominio_id) REFERENCES condominios(condominio_id)
);

CREATE TABLE transacoes (
    transacao_id SERIAL PRIMARY KEY,
    imovel_id INT NOT NULL,
    morador_id INT NOT NULL,
    data_transacao DATE NOT NULL,
    valor_transacao NUMERIC(15, 2) NOT NULL,
    FOREIGN KEY (imovel_id) REFERENCES imoveis(imovel_id),
    FOREIGN KEY (morador_id) REFERENCES moradores(morador_id)
);

-- Inserção de dados fictícios
INSERT INTO condominios (nome, endereco) VALUES 
('Condomínio A', 'Rua A, 123'),
('Condomínio B', 'Rua B, 456');

INSERT INTO moradores (nome, condominio_id, data_registro) VALUES 
('Morador 1', 1, '2024-01-01'),
('Morador 2', 2, '2024-02-01');

INSERT INTO imoveis (tipo, condominio_id, valor) VALUES 
('Apartamento', 1, 300000.00),
('Casa', 2, 500000.00);

INSERT INTO transacoes (imovel_id, morador_id, data_transacao, valor_transacao) VALUES 
(1, 1, '2024-03-01', 320000.00),
(2, 2, '2024-04-01', 520000.00);
