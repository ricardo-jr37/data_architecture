from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, to_date

def main():
    # Cria uma sessão Spark
    spark = SparkSession.builder \
        .appName("Silver Ingestion") \
        .getOrCreate()

    # Caminhos para os arquivos CSV na camada Bronze
    bronze_path = "/data/bronze"
    
    # Leitura dos dados da camada Bronze
    transacoes_df = spark.read.csv(f"{bronze_path}/transacoes.csv", header=True, inferSchema=True)
    imoveis_df = spark.read.csv(f"{bronze_path}/imoveis.csv", header=True, inferSchema=True)
    condominios_df = spark.read.csv(f"{bronze_path}/condominios.csv", header=True, inferSchema=True)
    moradores_df = spark.read.csv(f"{bronze_path}/moradores.csv", header=True, inferSchema=True)

    # Calcular o total de transações por condomínio
    transacoes_por_condominio_df = transacoes_df.join(
        imoveis_df, transacoes_df.imovel_id == imoveis_df.imovel_id
    ).join(
        condominios_df, imoveis_df.condominio_id == condominios_df.condominio_id
    ).groupBy(
        "nome"
    ).agg(
        count("transacao_id").alias("total_transacoes")
    )
    
    # Calcular o valor total das transações por morador
    valor_transacoes_por_morador_df = transacoes_df.join(
        moradores_df, transacoes_df.morador_id == moradores_df.morador_id
    ).groupBy(
        "nome"
    ).agg(
        sum("valor_transacao").alias("valor_total_transacoes")
    )

    # Agregar as transações diárias por tipo de imóvel
    transacoes_diarias_por_tipo_df = transacoes_df.join(
        imoveis_df, transacoes_df.imovel_id == imoveis_df.imovel_id
    ).groupBy(
        to_date(col("data_transacao")).alias("data"),
        col("tipo")
    ).agg(
        sum("valor_transacao").alias("valor_total")
    )

    # Caminhos para os arquivos Parquet na camada Silver
    silver_path = "/data/silver"
    
    # Salvar os resultados em formato Parquet
    transacoes_por_condominio_df.write.parquet(f"{silver_path}/transacoes_por_condominio.parquet", mode="overwrite")
    valor_transacoes_por_morador_df.write.parquet(f"{silver_path}/valor_transacoes_por_morador.parquet", mode="overwrite")
    transacoes_diarias_por_tipo_df.write.parquet(f"{silver_path}/transacoes_diarias_por_tipo.parquet", mode="overwrite")

    # Finaliza a sessão Spark
    spark.stop()

if __name__ == "__main__":
    main()
