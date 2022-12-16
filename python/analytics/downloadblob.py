from azure.storage.blob import BlobServiceClient
import pandas as pd
import time
from decouple import config
from azure.identity import DefaultAzureCredential

try:
    account_url = "https://deviceessagetore213h4ms.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    container_client = blob_service_client.get_container_client(config('STORAGE_CONTAINER_NAME'))

finally:
    print("finished!")

print("\nListing blobs...")

# List the blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)

print("Complete")