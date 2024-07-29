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

### 4. spark-streaming

- **Objetivo**: Este serviço é responsável por processar dados em tempo real usando o Spark Structured Streaming. Ele lê dados de entrada da camada bronze, processa esses dados e grava os resultados em formatos otimizados na camada de dados de streaming e resultados.

- **Construção**:
  - **Contexto**: A partir do Dockerfile localizado no diretório `./streaming_ingestion`. Este Dockerfile define o ambiente necessário para executar scripts Spark Streaming.
  - **Dependências**: Depende do serviço `bronze-ingestion`, o qual deve estar em execução para fornecer os dados necessários.

- **Variáveis de Ambiente**:
  - `AWS_ACCESS_KEY_ID`: Identificador da chave de acesso AWS (se necessário).
  - `AWS_SECRET_ACCESS_KEY`: Chave secreta da AWS (se necessário).
  - `AWS_REGION`: Região da AWS onde os serviços são executados (se necessário).

- **Volumes**:
  - `./data/streaming`: Diretório onde os dados de entrada são armazenados.
  - `./data/streaming_results`: Diretório onde os resultados processados são armazenados.
  - `./data/streaming_checkpoint`: Diretório para checkpoints do Spark Streaming, garantindo que o estado da aplicação seja salvo periodicamente para permitir a recuperação em caso de falhas.
  - `./data/bronze`: Diretório contendo dados da camada bronze que serão processados pelo Spark Streaming.
  - `./data/silver`: Diretório para armazenar dados processados na camada silver (se necessário).

- **Redes**: Conectado à rede `dbnet`, permitindo a comunicação com outros serviços, como `bronze-ingestion`, e possibilitando o acesso aos dados e a integração com outros serviços.

- **Comando de Execução**:
  - O serviço executa um script Python (`streaming_script.py`) localizado no diretório `./streaming_ingestion`. Este script configura e inicia uma aplicação Spark Structured Streaming, processando os dados em tempo real e salvando os resultados conforme necessário.

- **Observações**:
  - O serviço está configurado para processar dados de streaming a partir de arquivos CSV na camada bronze e gravar os resultados em formato otimizado, como Parquet, na camada de dados de streaming e resultados.
  - Certifique-se de que o diretório `./data/streaming` contenha os dados apropriados para que o serviço funcione corretamente.
  - O serviço utiliza checkpoints para garantir a tolerância a falhas. O diretório `./data/streaming_checkpoint` deve ser persistente e disponível.

Este serviço faz parte de uma pipeline de processamento de dados em tempo real e é crucial para a análise e transformação contínua dos dados conforme eles são gerados.


## Comandos para Executar o Projeto

1. **Construir e iniciar os serviços**

   Execute o seguinte comando para construir as imagens Docker e iniciar os serviços definidos no `docker-compose.yml`:

   ```bash
   docker-compose up --build
