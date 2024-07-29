# Use a imagem oficial do Spark da Bitnami, que inclui Spark e Java
FROM bitnami/spark:latest

# Instale Python e outras dependências do sistema
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Instale as dependências do Python
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copie o script PySpark para dentro do contêiner
COPY streaming_script.py /streaming_script/script.py

# Defina o comando padrão
CMD ["python", "/streaming_script/script.py"]
