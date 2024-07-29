# Descrição do Projeto

Este projeto utiliza Docker para orquestrar um ambiente que inclui um banco de dados PostgreSQL, um serviço Python para ingestão de dados e um serviço PySpark para processamento de dados. Os dados são processados em camadas de Bronze e Silver, com arquivos CSV na camada Bronze e arquivos Parquet na camada Silver.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

- **data/**: Diretórios para armazenar arquivos de dados.
  - **bronze/**: Contém arquivos CSV com dados brutos.
  - **silver/**: Contém arquivos Parquet com dados processados.

- **raw_ingestion/**: Contém o serviço Python para ingestão de dados no banco de dados PostgreSQL.
  - **Dockerfile**: Define o ambiente para o serviço Python.
  - **ingestion_script.py**: Script Python para ler dados e salvar no banco de dados PostgreSQL.

- **silver_ingestion/**: Contém o serviço PySpark para processamento de dados.
  - **Dockerfile**: Define o ambiente para o serviço PySpark.
  - **silver_script.py**: Script PySpark para processar dados da camada Bronze e salvar resultados na camada Silver.

- **setup.sql**: Script SQL para criar tabelas e popular dados fictícios no banco de dados PostgreSQL.

- **docker-compose.yml**: Arquivo de configuração do Docker Compose para orquestrar todos os serviços.

## Serviços no Docker Compose

### 1. db

- **Imagem**: `postgres:latest`
- **Porta**: `5432`
- **Descrição**: Serviço de banco de dados PostgreSQL. Este serviço usa a imagem oficial do PostgreSQL e é configurado para criar e popular um banco de dados com tabelas e dados fictícios a partir do `setup.sql`.
- **Volumes**:
  - `db-data` para persistência dos dados do banco.
  - `./setup.sql` para inicialização do banco de dados.

### 2. python-script

- **Imagem**: Customizada a partir do diretório `raw_ingestion`
- **Descrição**: Serviço Python que lê dados dos arquivos CSV na camada Bronze e os salva no banco de dados PostgreSQL.
- **Volumes**:
  - `./data` mapeia o diretório local `data` para `/data` dentro do contêiner, permitindo acesso aos arquivos CSV e salvamento de dados processados.

### 3. pyspark-script

- **Imagem**: Customizada a partir do diretório `silver_ingestion`
- **Descrição**: Serviço PySpark que processa os dados da camada Bronze e gera dados transformados na camada Silver.
- **Volumes**:
  - `./data/bronze` mapeia o diretório local `data/bronze` para `/data/bronze` dentro do contêiner, permitindo a leitura dos arquivos CSV.
  - `./data/silver` mapeia o diretório local `data/silver` para `/data/silver` dentro do contêiner, permitindo a gravação dos arquivos Parquet.

## Comandos para Executar o Projeto

1. **Construir e iniciar os serviços**

   Execute o seguinte comando para construir as imagens Docker e iniciar os serviços definidos no `docker-compose.yml`:

   ```bash
   mkdir ./data/bronze/
   mkdir ./data/silver/
   docker-compose up --build
