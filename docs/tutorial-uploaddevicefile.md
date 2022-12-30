---
title: Upload a file to the Cloud from your Device
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Upload a file to the Cloud from your Device

In this tutorial you'll...

[todo] image needed

## Prerequisites

[todo]

## Create a new storage account and container

1. Use the resource group for your IoT Hub

    ```powershell
    $resourceGroupName = "{your IoT Hub resource group name"
    ```

1. Set the storage account name after creating it

    ```powershell
    $storename = "{your storage account name}"
    ```

1. Create a new storage account

    ```powershell
    New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -storeacctname  $storename -TemplateFile "store.json"
    ```

1. Find the storage account key and create a new "mydevicefiles" container

    ```powershell
    Connect-AzAccount -SubscriptionId "{your subscription id}"
    
    $ctx = New-AzStorageContext -StorageAccountName $storename -StorageAccountKey "{primary storage key}"
    New-AzStorageContainer -Name "{your file container name}" -Context $ctx
    ```

    For example,

    ```powershell
    Connect-AzAccount -SubscriptionId "3286xxxx-xxxx-xxxx-xxxx-xxxxxxxx46e1"
    
    $ctx = New-AzStorageContext -StorageAccountName $storename -StorageAccountKey "qlwjxxxxxxxxxxxxqwjr"
    New-AzStorageContainer -Name "mydevicefiles" -Context $ctx
    ```

## Connect your storage account to your IoT Hub

See [Configure IoT Hub file uploads](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-configure-file-upload)

## Create Code to Upload a file from your Device

1. From Visual Studio Code, create a new file called `devicefileupload.py`.
1. Copy and paste the following import statements into your `devicefileupload.py` file

    ```python
    import os
    import asyncio
    from azure.iot.device.aio import IoTHubDeviceClient
    from azure.storage.blob import BlobClient
    from azure.core.exceptions import ResourceExistsError
    ```

1. Create the storage blob upload function

    ```python
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
    ```

1. Create the main function to provide the file to upload.

    ```python
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
    
        # Using the Storage Blob V12 API, perform the blob upload.
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
    ```

1. Run the Visual Studio Code debugger and [todo: complete this section]

## Next Steps

[Deploy and Configure StreamAnalytics](tutorial-deploystreamtostorage.md)
