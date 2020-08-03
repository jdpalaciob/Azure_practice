import logging
import tempfile
import cv2
import azure.functions as func
from azure.storage.blob import BlobServiceClient

def get_download_blob(connection_string, container, file_name, temp_path):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    file_read = f'Original/{file_name}'
    file_locate = f'{temp_path}/{file_name}'
    blob_client = blob_service_client.get_blob_client(container, file_read).download_blob()

    image_download = blob_client.readall()
    with open(file_locate, 'wb') as image:
        image.write(image_download)

def gray_conversion(file_name, temp_path):

    file_locate = f'{temp_path}/{file_name}'
    image = cv2.imread(file_locate, 0)

    file_destination = f'{temp_path}/gris_{file_name}'
    cv2.imwrite(file_destination, image)

def get_upload_blob(connection_string, container, file_name, temp_path):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    file_read = f'{temp_path}/gris_{file_name}'
    file_destination = f'Gris/gris_{file_name}'
    blob_client = blob_service_client.get_blob_client(container, file_destination)
    with open(file_read, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:

        CONNECT_STR = 'DefaultEndpointsProtocol=https;AccountName=josetextpythontry;AccountKey=dSZRzfx8eROjLaMsEonVPycb65FPyoJuiEgLIt2PdeTl1TcyY8LohJ8YC6Cvk65JYiYlUOkvP+y89Cd0CYVl9Q==;EndpointSuffix=core.windows.net'
        CONTAINER_NAME = 'image-trainning'
        FILE_NAME = name
        # Grises = tempfile.TemporaryDirectory()
        # Original = tempfile.TemporaryDirectory()
        temp_path = tempfile.gettempdir()

        get_download_blob(CONNECT_STR, CONTAINER_NAME, FILE_NAME, temp_path)
        gray_conversion(FILE_NAME, temp_path)
        get_upload_blob(CONNECT_STR, CONTAINER_NAME, FILE_NAME, temp_path)

        return func.HttpResponse(
             f"The image: {name}, has been sucesfully converted to gray!",
             status_code=200
        )
    else:
        return func.HttpResponse(
             "Please pass a name of the image you wish to convert",
             status_code=400
        )
