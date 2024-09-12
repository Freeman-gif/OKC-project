from datetime import date, timedelta
import os
import request

from google.cloud import storage

def 


def create_dir(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)
    
    
    
def write_json_to_gcs(bucket_name, blob_name, service_account_key_file, file):
    storage_client = storage.Client.from_service_account_json(service_account_key_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)