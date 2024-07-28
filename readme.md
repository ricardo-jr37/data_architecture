# Arquitetura de Dados - Visão Geral

Este documento descreve a arquitetura de dados utilizada para coletar, processar, armazenar e analisar dados de diversas fontes. A plataforma foi projetada para gerar insights valiosos e auxiliar na tomada de decisões.

![arquitetura](./img/architecture.png)

## Componentes Principais

### Fontes de Dados (Data Sources)
As fontes de dados representam a origem dos dados que serão coletados e processados na plataforma. Nesta arquitetura, as fontes de dados incluem:

- **SQL Server**: Banco de dados relacional da Microsoft, utilizado para armazenar dados estruturados.
- **PostgreSQL**: Banco de dados relacional open-source, conhecido por sua robustez e suporte a diversos tipos de dados.
- **Oracle**: Banco de dados relacional utilizado para aplicações empresariais de grande escala.
- **APIs**: Interfaces de programação de aplicações que permitem a integração e troca de dados entre diferentes sistemas.
- **Outras fontes**: Incluem arquivos de texto, planilhas, e outras bases de dados que podem ser integradas à plataforma.

### Zona de Ingestão (Ingestion Zone)
A zona de ingestão é responsável pela coleta inicial dos dados das fontes e pelo seu encaminhamento para o processamento. As tecnologias utilizadas incluem:

- **Airbyte**: Ferramenta de integração de dados que facilita a movimentação dos dados entre diferentes fontes e destinos.
- **Kafka**: Plataforma de streaming distribuída que permite a publicação e a subscrição de fluxos de dados em tempo real.
- **Python**: Linguagem de programação usada para escrever scripts de ingestão e transformação de dados.

### Data Stack (Pilha de Dados)
O Data Stack é a camada responsável pelo processamento, armazenamento e refinamento dos dados. Ele é dividido em várias subcamadas:

- **Camadas de Dados (Bronze, Silver, Gold)**:
  - **Bronze Layer**: Armazena dados brutos, conforme coletados das fontes.
  - **Silver Layer**: Contém dados limpos e transformados.
  - **Gold Layer**: Dados altamente refinados, prontos para análise e consumo.

- **Data Process**: 
  - **Spark**: Ferramenta de processamento de dados que realiza transformações complexas, como agregação, junção e análise em janelas de tempo.

- **Governance Zone**:
  - **OpenMetadata**: Plataforma de metadados que facilita a gestão e a governança dos dados, promovendo a colaboração, a descoberta de dados e a conformidade.

- **Orchestration**:
  - **Apache Airflow**: Plataforma de orquestração de workflows que gerencia tarefas de ETL (extração, transformação e carregamento) e outros processos de dados.
  - **Kubernetes**: Sistema de orquestração de contêineres que automatiza a implantação, o dimensionamento e a gestão de aplicações em contêineres.

### Self-Service Analytics (Amazon Athena)
O **Amazon Athena** é um serviço de análise interativa que permite consultar dados diretamente no Amazon S3 usando SQL. Ele facilita a realização de análises de dados de forma rápida e eficiente, sem a necessidade de configurar ou gerenciar infraestrutura complexa. Suas principais características incluem:

- **Consultas SQL**: Permite aos usuários executar consultas SQL diretamente em dados armazenados no Amazon S3, facilitando o acesso e a análise de dados.
- **Self-Service**: Capacita analistas de negócios, cientistas de dados e outros usuários a realizar análises de dados sem a necessidade de suporte contínuo da equipe de TI.
- **Escalabilidade**: Athena escala automaticamente para executar consultas de qualquer tamanho e complexidade, garantindo desempenho e eficiência.
- **Custo-Efetividade**: Os usuários pagam apenas pelas consultas executadas e pela quantidade de dados processados, tornando-o uma solução econômica para análise de dados.
- **Integração com outras ferramentas**: Pode ser facilmente integrado com ferramentas de visualização de dados como o Power BI para criar dashboards e relatórios interativos.

### Data Visualization
Esta camada fornece acesso e visualizações dos dados para os usuários finais:

- **Power BI**: Ferramenta de visualização de dados que permite criar dashboards e relatórios interativos.

### Data Users
Usuários finais que utilizam os dados para gerar insights e tomar decisões:

- **Analistas de negócios**: Utilizam os dados para análise e geração de relatórios.
- **Cientistas de dados**: Realizam análises avançadas e modelagem preditiva.
- **Tomadores de decisão**: Usam insights derivados dos dados para orientar decisões estratégicas.

### Infrastructure Stack (Pilha de Infraestrutura)
Gerencia a infraestrutura necessária para suportar toda a plataforma de dados:

- **Argo**: Ferramenta de fluxo de trabalho que gerencia a automação e a execução de pipelines de dados.
- **Terraform**: Ferramenta de infraestrutura como código que permite a definição e o provisionamento de infraestrutura.
- **GitHub**: Plataforma de controle de versão e colaboração de código.
- **Docker Registry**: Armazena e distribui imagens de contêiner Docker.

### Observability Stack
A camada de observabilidade fornece monitoramento e análise do desempenho da plataforma:

- **Monitoring**:
  - **Grafana**: Plataforma de observabilidade que fornece dashboards e gráficos interativos.
  - **Prometheus**: Sistema de monitoramento e alerta que coleta e armazena métricas.
   - **OpenTelemetry**: Ferramenta que fornece rastreamento e monitoramento de desempenho, permitindo a coleta de dados sobre a latência e a performance das aplicações.

- **Alertas e Mensagens**:
  - **Telegram, Slack, Gmail**: Canais de comunicação para notificação de eventos críticos e alertas.