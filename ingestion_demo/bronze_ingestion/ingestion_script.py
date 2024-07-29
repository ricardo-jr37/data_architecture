import psycopg2
import pandas as pd
import awswrangler as wr

# Configurações do PostgreSQL
db_config = {
    'dbname': 'condominios_db',
    'user': 'user',
    'password': 'password',
    'host': 'db',
    'port': '5432'
}

# Configurações do S3
s3_config = {
    'bucket_name': 'YOUR_BUCKET_NAME',
    'aws_access_key_id': 'YOUR_ACCESS_KEY_ID',
    'aws_secret_access_key': 'YOUR_SECRET_ACCESS_KEY',
    'region_name': 'YOUR_REGION'
}

def fetch_data(table):
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(**db_config)
    query = f"SELECT * FROM {table};"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def upload_to_s3(
        df,
        table
    ):
    s3_target_path = f"s3://{s3_config['bucket_name']}/raw/{table}/"
    print(s3_target_path)
    """
    wr.s3.to_parquet(
        df            = df,
        path          = s3_target_path,
    )
    """

def upload_local(
    df,
    table
):
    print(df)   
    df.to_csv(f'./data/bronze/{table}.csv', index=False)

def ingestion_data(table):
    df = fetch_data(table)
    print(df)
    return df

if __name__ == "__main__":
    tables = ['condominios', 'imoveis', 'moradores', 'transacoes']
    for table in tables:
        print(f'Load table: {table}')
        df_raw = ingestion_data(table)
        upload_local(df_raw, table)
        #print("Upload to s3")
        #upload_to_s3(df_raw, table)
