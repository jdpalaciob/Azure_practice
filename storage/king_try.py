from azure.storage.blob import BlobServiceClient

try:
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=josetextpythontry;AccountKey=dSZRzfx8eROjLaMsEonVPycb65FPyoJuiEgLIt2PdeTl1TcyY8LohJ8YC6Cvk65JYiYlUOkvP+y89Cd0CYVl9Q==;EndpointSuffix=core.windows.net'

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    king_text_download = blob_service_client.get_blob_client('container-text-try', 'king.txt').download_blob()
    king_text = king_text_download.readall()
    print(king_text.decode('UTF-8'))

except Exception as ex:
    print('Exception:')
    print(ex)
    