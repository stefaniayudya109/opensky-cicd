import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


def upload_file_to_blob(local_file_path: str, blob_name: str) -> str:
    account_name = os.environ["AZURE_STORAGE_ACCOUNT"]
    container_name = os.environ["AZURE_STORAGE_CONTAINER"]
    account_url = f"https://{account_name}.blob.core.windows.net"

    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    return f"{account_url}/{container_name}/{blob_name}"