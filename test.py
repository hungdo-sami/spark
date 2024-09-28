import json
from pyspark.sql import SparkSession
from google.cloud import storage

# Dữ liệu cần ghi
data = {
    "name": "Hung Do",
    "age": 30,
    "city": "Hanoi"
}
json_data = json.dumps(data)

# Khởi tạo SparkSession với chế độ cluster
spark = SparkSession.builder \
    .appName("GCS JSON Writer") \
    .master("spark://34.64.144.247:7077") \
    .getOrCreate()

# Ghi dữ liệu vào GCS
bucket_name = 'hungdo_hust'
destination_blob_name = 'data-lakehouse/bronze/data.json'

# Tạo client
storage_client = storage.Client.from_service_account_json('key.json')

# Tạo bucket
bucket = storage_client.bucket(bucket_name)

# Tạo blob và ghi dữ liệu
blob = bucket.blob(destination_blob_name)
blob.upload_from_string(json_data, content_type='application/json')

print(f'JSON data đã được ghi vào gs://{bucket_name}/{destination_blob_name}')

# Dừng SparkSession
spark.stop()
