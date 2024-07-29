from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

def main():
    # Cria uma sessão Spark
    spark = SparkSession.builder \
        .appName("Streaming Ingestion") \
        .getOrCreate()

    # Lê dados de um diretório ou stream
    # Supondo que estamos lendo de um diretório que recebe dados em tempo real
    input_path = "/data/bronze/condominios/"
    df = spark.readStream \
        .format("csv") \
        .option("header", "true") \
        .schema("condominio_id INT, nome STRING") \
        .load(input_path)

    # Defina a saída dos resultados
    output_path = "/data/streaming_results"
    query = df.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .option("path", output_path) \
        .option("checkpointLocation", "/data/streaming_checkpoint") \
        .start()

    query.awaitTermination()

    # Finaliza a sessão Spark
    spark.stop()

if __name__ == "__main__":
    main()
