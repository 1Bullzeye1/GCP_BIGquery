from google.cloud import bigquery

client = bigquery.Client()


dataset = client.dataset(dataset_id = "bwt_employee_dataset",project = "augmented-city-351802")

print(dataset)

dataset.location = "US"

out = client.create_dataset(dataset = dataset)
print("successfully created {} in {}".format(dataset.dataset_id,client.project))

