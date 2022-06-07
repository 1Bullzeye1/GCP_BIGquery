from google.cloud import bigquery

#create table

bq = bigquery.Client()

# table_id = "procrastinated-city-46778.bwt_student_dataset.student_db"
#
# schema = [
#     bigquery.SchemaField("id","integer",mode="required"),
#     bigquery.SchemaField("name","string",mode="required"),
#     bigquery.SchemaField("email","string",mode="required"),
#     bigquery.SchemaField("department","string",mode="required")
# ]
#
#
# table1 = bigquery.Table(table_id,schema=schema)
# table = bq.create_table(table1)
# print(
#     "Created table {}.{}.{}".format(table1.project, table1.dataset_id, table1.table_id)
# )


#delete table


# table_id = "procrastinated-city-46778.bwt_employee_dataset.survey_db"
#
# bq.delete_table(table_id,not_found_ok=True)
# print("Deleted Table '{}' ".format(table_id))


#copy table

# dest_table_id = "procrastinated-city-46778.bwt_employee_dataset.student_db"
#
# source_table_id = "augmented-city-351802.bwt_student_dataset.student_db"
#
# job_cp = bq.copy_table(source_table_id,dest_table_id)
#
# job_cp.result()
#
# dest_tb = bq.get_table(dest_table_id)
# if dest_tb:
#     print("copy of table created")
# else:
#     print("error while creating copy..!")