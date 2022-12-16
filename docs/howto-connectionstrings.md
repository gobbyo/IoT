# How to Find and Set Your Connection Strings

1. Install decouple, see https://pypi.org/project/python-decouple/ for details.

    ```python
    pip install python-decouple
    ```

1. Create an '.env' file and save it to the various/python directory from your GitHub clone.

    ```python
    IOTHUB_CONNECTION_STRING="{IoT hub Primary Connection String}"
    IOTHUB_DEVICE_CONNECTION_STRING="{Your Device Connection String}"
    STORAGE_CONNECTION_STRING="{Storage Connection String}"
    STORAGE_CONTAINER_NAME="{Name of Your Storage Container}"
    EVENTHUB_CONNECTION_STRING="{Built-in Endpoint Event Hub Connection String}"
    EVENTHUB_NAME="{Built-in Endpoint Event Hub Name}"
    ```

Table of Connection Variables

| **Connection Variable Name**  | **Value Found in portal.azure.com**  | **Details about finding the value**  | **File Referencing Environment Variable** |
|:---------|:---------|:---------|:---------|
| `IOTHUB_CONNECTION_STRING`  | IoT Hub > Shared Access Policies > service (policy) > Primary Connection String |         | `c2dsendmsg.py` |
| `IOTHUB_DEVICE_CONNECTION_STRING` | IoT Hub > Devices > {your device} > Primary Connection String |         | `d2ceventhublistener.py, c2dlistener.py, d2csendmsg.py, c2dmaproutelistener` |
| `STORAGE_CONNECTION_STRING` | Storage Account > Access Keys > Connection String | [Manage storage account access keys](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/storage/common/storage-account-keys-manage.md#manage-storage-account-access-keys) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `STORAGE_CONTAINER_NAME` | Storage Account > Containers > Name | [Manage storage account access keys](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/storage/common/storage-account-keys-manage.md#manage-storage-account-access-keys) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `EVENTHUB_CONNECTION_STRING` | IoT Hub > Built-in endpoints > Event Hub-compatible endpoint | [Read from the built-in endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin#read-from-the-built-in-endpoint) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `EVENTHUB_NAME` | IoT Hub > Built-in endpoints > Event Hub-compatible name | [Read from the built-in endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin#read-from-the-built-in-endpoint) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `MAP_KEY` | Azure Maps > Authentication > Primary Key | [Get the primary key for your account](https://learn.microsoft.com/en-us/azure/azure-maps/quick-demo-map-app#get-the-primary-key-for-your-account) | c2devent |

1. Obtain the secret by opening a python session in the same directory as the '.env' file where you'll run your scripts.

    ```python
    cd {github clone root}/python python
    from decouple import config
    config('IOTHUB_DEVICE_CONNECTION_STRING')
    ```

    for example,

    ```python
    cd c:/repos/various/python python
    >>> from decouple import config
    >>> config('IOTHUB_DEVICE_CONNECTION_STRING')
    >>> 'HostName=HubMsg********p2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8IrO********ZUkg='
    ```
