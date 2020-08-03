import cv2
from azure.storage.blob import BlobServiceClient

def get_download_blob(connection_string, container, file_name):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    file_locate = f'Original/{file_name}'
    blob_client = blob_service_client.get_blob_client(container, file_locate).download_blob()

    image_download = blob_client.readall()
    with open(file_locate, 'wb') as image:
        image.write(image_download)

def gray_conversion(file_name):

    file_locate = f'Original/{file_name}'
    image = cv2.imread(file_locate, 0)

    file_destination = f'Grises/gris_{file_name}'
    cv2.imwrite(file_destination, image)

def get_upload_blob(connection_string, container, file_name):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    file_destination = f'Grises/gris_{file_name}'
    blob_client = blob_service_client.get_blob_client(container, file_destination)
    with open(file_destination, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)


if __name__ == '__main__':

    CONNECT_STR = 'DefaultEndpointsProtocol=https;AccountName=josetextpythontry;AccountKey=dSZRzfx8eROjLaMsEonVPycb65FPyoJuiEgLIt2PdeTl1TcyY8LohJ8YC6Cvk65JYiYlUOkvP+y89Cd0CYVl9Q==;EndpointSuffix=core.windows.net'
    CONTAINER_NAME = 'image-trainning'
    FILE_NAME = 'circulo.jpeg'

    get_download_blob(CONNECT_STR, CONTAINER_NAME, FILE_NAME)
    gray_conversion(FILE_NAME)
    get_upload_blob(CONNECT_STR, CONTAINER_NAME, FILE_NAME)
