from google.cloud import bigquery

cli = bigquery.Client()

table_id = "procrastinated-city-46778.bwt_employee_dataset.department"



job_config = bigquery.LoadJobConfig(autodetect=True)

uri = "gs://buk_zero/departments.csv"

ct = cli.load_table_from_uri(uri,table_id,job_config=job_config)

ct.result()

destination_table = cli.get_table(table_id)
print("loaded {} rows".format(destination_table.num_rows))
