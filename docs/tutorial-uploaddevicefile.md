---
title: Upload a file to the Cloud from your Device
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Upload a file to the Cloud from your Device

In this tutorial, you'll learn how to:

- Create a new storage account and container
- Connect your storage account to your IoT Hub
- Create code to upload a file from your Device

There are several reasons why you might want to **upload files from an IoT device** to the cloud:

- *Data storage and backup*. The cloud provides a secure and scalable location to store data from your IoT devices. This can be useful for creating backups of your data in case something goes wrong with your device.
- *Data processing and analysis*. The cloud provides powerful resources for processing and analyzing data from your IoT devices. This can be useful for generating insights and making data-driven decisions.
- *Remote access*. By uploading data to the cloud, you can access it from anywhere with an internet connection. This can be useful for monitoring and controlling your IoT devices remotely.
- *Integration with other systems*. The cloud provides a way to integrate data from your IoT devices with other systems and applications. This can enable a wide range of possibilities, such as triggering automated responses based on data from your devices or integrating with other systems for analysis and decision making.

## Prerequisites

- [Tutorial: Send a Message from a Simulated Device To the Cloud](tutorial-devicetocloudmsg.md)
- The name of your IoT Hub's resource group

## Create a new storage account and container

In this section you'll create a storage container and account for the files you upload. **Azure Storage** is a service for storing and retrieving data in a variety of formats, including blobs (binary large objects), files, tables, and queues.

**A container in Azure Storage** is a logical grouping of blobs. Containers provide a way to organize your blobs and set permissions for them. You can think of a container as a folder in a file system.

Azure Storage containers are used for storing and managing large amounts of data in the cloud. They can be used for a variety of purposes, such as storing files for distributed access, storing data for backup and restore, storing data for analysis by an on-premises or Azure-hosted service, and storing data for archiving. You'll do the following actions in the diagram below to set up your upload storage:
1. Obtain the resource group name from your IoT Hub
1. Create a new storage account
1. Create a new storage container in your storage account
1. Configure IoT hub to use your storage account for file uploads

![lnk_installfileupload]

1. Open a PowerShell terminal session from VS Code in your Cloud Machine. Run the following script using your IoT Hub's resource group you created in the [Tutorial: Deploy an Azure IoT Hub](tutorial-deployiothub.md) to set the `$resourceGroupName` PowerShell variable.

    ```powershell
    $resourceGroupName = "{your IoT Hub resource group name}"
    ```

1. Set the $storename to a unique value. A simple way to generate a unique value is to run `new-guid` (like `ab54e2b1-efbc-440b-a8f3-402e15d843a4`) in your PowerShell console and append the last 12 numbers and characters to the word 'store', e.g. 'store402e15d843a4'.

    ```powershell
    $storename = "{your storage account name}"
    ```

    For example,
    ```powershell
    $storename = "store402e15d843a4"
    ```

1. Run the following script to create a new storage account,

    ```powershell
    New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -storeacctname  $storename -TemplateFile "{github root directory}\arm\store.json"
    ```

    For example,

    ```powershell
    New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -storeacctname  $storename -TemplateFile "c:\repos\IoT\arm\store.json"
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

1. Connect your storage account to your IoT Hub by following the instructions to [Configure IoT Hub file uploads](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-configure-file-upload)

## Create Code to Upload a file from your Device

In this section you'll create code to upload a file to blob storage from your simulated device. **Blob storage** in Azure is a cloud storage service that is optimized for storing large amounts of unstructured data, such as binary data, documents, media files, and backups. There are several reasons why you might want to use blob storage for IoT devices:

- *Scalability*. Blob storage is highly scalable, which means it can easily handle large amounts of data without requiring additional infrastructure. This makes it a good choice for storing data from IoT devices, which can generate large volumes of data.
- *Cost effectiveness*. Blob storage is relatively inexpensive compared to other storage options, which makes it a cost-effective choice for storing data from IoT devices.
- *Durability*. Blob storage is designed to be highly durable, with multiple copies of data stored in multiple locations. This makes it a good choice for storing data that needs to be preserved, such as data from IoT devices that is used for analysis or long-term storage.
- *Integration with other Azure services*. Blob storage can be easily integrated with other Azure services, such as Azure Stream Analytics and Azure Functions, which can be useful for processing and analyzing data from IoT devices.

1. From Visual Studio Code, create a new file called `devicefileupload.py`.
1. Copy and paste the following import statements into your `devicefileupload.py` file

    ```python
    import os
    import asyncio
    from azure.iot.device.aio import IoTHubDeviceClient
    from azure.storage.blob import BlobClient
    from azure.core.exceptions import ResourceExistsError
    ```

1. Create the storage blob upload function. [todo] describe the blob client call pattern.

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

1. Create the main function to provide the file to upload. [todo] describe the client call pattern.

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
    ```

1. Run the Visual Studio Code debugger

## Next Steps

[Deploy and Configure StreamAnalytics](tutorial-deploystreamtostorage.md)

<!--image-->

[lnk_installfileupload]: media/tutorial-uploaddevicefile/installuploadfilestorage.png
