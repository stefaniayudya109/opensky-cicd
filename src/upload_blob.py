import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


def upload_file_to_blob(local_file_path: str, blob_name: str) -> str:
    account_name = (os.getenv("AZURE_STORAGE_ACCOUNT") or "openskycicd").strip()
    container_name = (os.getenv("AZURE_STORAGE_CONTAINER") or "opensky-data").strip()
    clean_blob_name = blob_name.lstrip("/")
    account_url = f"https://{account_name}.blob.core.windows.net"

    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
    container_client = blob_service_client.get_container_client(container_name)

    if not container_client.exists():
        container_client.create_container()

    blob_client = container_client.get_blob_client(clean_blob_name)

    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    return f"{account_url}/{container_name}/{clean_blob_name}"