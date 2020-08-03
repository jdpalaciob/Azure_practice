""" Script for deleting a folder inside an Azure Storage.

This script contains the required python function for deleting a given
folder inside a Container present in an Azure Blob Storage service. The
Storage account and the Container must exist for propper operation and
the connection to the service must be stablished by connection string.

Requieres azure-storage-blob package to be installed alongside Python3.

Functions contained
    * blob_folder_eraser - delete a folder inside a container from Azure Blob Storage

Parameters:
----------
    CONNECT_STR: str
        Connection string of the Azure Storage account
    CONTAINER_NAME: str
        Name of the container where folder is located
    FOLDER_NAME: str
        Name of the folder to be deleted

See Also:
--------
BlobServiceClient: Class to interact with the Blob service
get_container_client: get a client to interact with a specific container
get_blob_client: get a client to interact with a sepecific blob
delete_blob: marks a sepecific blob for deletion
"""


from azure.storage.blob import BlobServiceClient#, ContainerClient, BlobClient

def blob_folder_eraser(connection_string, container, folder):
    """ Delete a folder inside a container from Azure Blob Storage.

    The function connects to the Blob Storage service via connection string.
    Select the container and delete everithing inside the given folder besides
    the folder itself. If the folder does not exist, no changes will occur.

    Parameters:
    ----------
    connection_string: str
        Connection string of the Azure Storage account
    container: str
        Name of the container where folder is located
    folder: str
        Name of the folder to be deleted

    See Also:
    BlobServiceClient: Class to interact with the Blob service
    get_container_client: get a client to interact with a specific container
    get_blob_client: get a client to interact with a sepecific blob
    delete_blob: marks a sepecific blob for deletion
    """

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container)

    blob_list = container_client.list_blobs()
    search_name = folder + '/'

    for blob in blob_list:
        if search_name in blob.name:
            blob_client = container_client.get_blob_client(blob)
            blob_client.delete_blob(delete_snapshots='include')


if __name__ == '__main__':

    CONNECT_STR = ''
    CONTAINER_NAME = ''
    FOLDER_NAME = ''

    blob_folder_eraser(CONNECT_STR, CONTAINER_NAME, FOLDER_NAME)
