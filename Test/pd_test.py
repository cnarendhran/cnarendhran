from google.cloud import storage,bigquery as BQ
# Explicitly use service account credentials by specifying the private key
# file.
client = BQ.Client.from_service_account_json(r"D:\Programing\BigQuery SA KeyFile\Pavarotti-28ade0fd2dd3.json")

# client = BQ.Client()
dataset_id = 'analytics_166860306'
# table_id = 'my_table'

dataset_ref = client.dataset(dataset_id)
tables = list(client.list_tables(dataset_ref)) 
print(tables)

# table_ref = dataset_ref.table(table_id)
# table = client.get_table(table_ref)  # API Request

# View table properties
# print(table.schema)
# print(table.description)
# print(table.num_rows)


