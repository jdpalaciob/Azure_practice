from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient

def get_upload_blob(connection_string, container, file_name):
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    blob_client = blob_service_client.get_blob_client(container, file_name)
    with open('./' + file_name, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)


if __name__ == '__main__':

    CONNECT_STR = 'DefaultEndpointsProtocol=https;AccountName=josetextpythontry;AccountKey=dSZRzfx8eROjLaMsEonVPycb65FPyoJuiEgLIt2PdeTl1TcyY8LohJ8YC6Cvk65JYiYlUOkvP+y89Cd0CYVl9Q==;EndpointSuffix=core.windows.net'
    CONTAINER_NAME = 'function-test'
    FILE_NAME = 'upload.txt'

    get_upload_blob(CONNECT_STR, CONTAINER_NAME, FILE_NAME)
