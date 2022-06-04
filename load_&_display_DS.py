import os
import re
from google.cloud import bigquery

client = bigquery.Client()

dataset_id  = "{}.empl".format(client.project)

dataset = bigquery.Dataset(dataset_id)

dataset.location = 'asia-east1'


dataset = client.create_dataset(dataset,timeout=30)

print("created dataset {}.{}".format(client.project,dataset.dataset_id))