from google.cloud import bigquery

if __name__ == "__main__":

    client = bigquery.Client()

    schema = [
        bigquery.SchemaField(name = "stud_id",field_type ="INTEGER" ),
        bigquery.SchemaField(name = "stud_name", field_type = "STRING"),
        bigquery.SchemaField(name = "stud_gender", field_type = "STRING"),
        bigquery.SchemaField(name = "stud_admn_date", field_type = "DATE")
    ]

    table = bigquery.Table("augmented-city-351802.bwt_student_dataset.student_db",schema)
    table.time_partitioning = bigquery.TimePartitioning(

        field = "stud_admn_date"
    )

    table = client.create_table(table)
    print("Successfully created table: {}".format(table.table_id))

