from google.cloud import bigquery

if __name__ == "__main__":

    client = bigquery.Client()

    schema = [
        bigquery.SchemaField(name = "dept_id",field_type ="INTEGER" ),
        bigquery.SchemaField(name = "dept_name", field_type = "STRING"),
        bigquery.SchemaField(name = "address",field_type = "RECORD",mode ="REPEATED" ,fields =[
            bigquery.SchemaField(name = "city",field_type = "string"),
            bigquery.SchemaField(name = "state",field_type ="string")
        ])
    ]

    table = bigquery.Table("augmented-city-351802.bwt_employee_dataset.employee_db",schema)

    table.clustering_fields=["dept_id"]
    table = client.create_table(table)
    print("Successfully created table: {}".format(table.table_id))

