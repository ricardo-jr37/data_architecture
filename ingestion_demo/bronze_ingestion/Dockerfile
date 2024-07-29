# Use a imagem oficial do Python
FROM python:3.9-slim

# Instale as dependências necessárias
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script Python para dentro do contêiner
COPY ingestion_script.py /bronze_ingestion/ingestion_script.py

# Defina o comando padrão
CMD ["python", "/bronze_ingestion/ingestion_script.py"]