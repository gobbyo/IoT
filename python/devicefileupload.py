import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.storage.blob import BlobClient
from azure.core.exceptions import ResourceExistsError

async def upload_via_storage_blob(blob_info, filepath):
    sas_url = "https://{}/{}/{}{}".format(
        blob_info["hostName"],
        blob_info["containerName"],
        blob_info["blobName"],
        blob_info["sasToken"],
    )
    
    blob_client = BlobClient.from_blob_url(sas_url)

    # Perform the actual upload for the data.
    print("\nUploading to Azure Storage as blob:\n\t" + blob_info["blobName"])
    # # Upload the created file
    with open(filepath, "rb") as data:
        result = blob_client.upload_blob(data)

    return result

async def main():
    filepath = input("Full path to file: ").replace('"','')
    if not os.path.exists(filepath):
        exit(print('File "{0}" does not exist.'), filepath)

    result = {"status_code": -1, "status_description: ": "unknown error"}
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    await device_client.connect()

    # get the Storage SAS information from IoT Hub.
    storage_info = await device_client.get_storage_info_for_blob(os.path.basename(filepath))

    # perform the blob upload.
    try:
        upload_result = await upload_via_storage_blob(storage_info, filepath)
        if hasattr(upload_result, "error_code"):
            result = {
                "status_code": upload_result.error_code,
                "status_description": "Storage Blob Upload Error",
            }
        else:
            result = {"status_code": 200, "status_description": ""}
    except ResourceExistsError as ex:
        if ex.status_code:
            result = {"status_code": ex.status_code, "status_description": ex.reason}
        else:
            print("Failed with Exception: {}", ex)
            result = {"status_code": 400, "status_description": ex.message}

    if result["status_code"] == 200:
        await device_client.notify_blob_upload_status(
            storage_info["correlationId"], True, result["status_code"], result["status_description"]
        )
    else:
        await device_client.notify_blob_upload_status(
            storage_info["correlationId"],
            False,
            result["status_code"],
            result["status_description"],
        )

    print(result)

    # Finally, shut down the client
    await device_client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())