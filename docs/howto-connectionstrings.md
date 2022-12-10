# How to Find and Set Your Connection Strings

## Set an Environment Variable with PowerShell

1. Open a [PowerShell session from Windows as an administrator](https://www.howtogeek.com/742916/how-to-open-windows-powershell-as-an-admin-in-windows-10/#:~:text=You%20can%20open%20Windows%20PowerShell%20with%20administrator%20privileges,and%20then%20type%20%E2%80%9Cpowershell%E2%80%9D%20in%20the%20text%20box.).
1. Run the following script by replacing `{Environment Variable Name}` with a name from the table below. Replace `{Value}` with the value found in [portal.azure.com](https://portal.azure.com/)

    ```powershell
    [System.Environment]::SetEnvironmentVariable("{Environment Variable Name}","{Value}","Machine")
    ```

    For example,

    ```powershell
    [System.Environment]::SetEnvironmentVariable("IOTHUB_CONNECTION_STRING","HostName=HubMxxxxxxxx2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/VxxxxxxxxmW4=")
    ```

1. Run the following script to verify the environment variable setting.

    ```powershell
    [System.Environment]::GetEnvironmentVariable("{Environment Variable Name}")
    ```

    For example,

    ```powershell
    [System.Environment]::GetEnvironmentVariable("IOTHUB_CONNECTION_STRING")
    HostName=HubMxxxxxxxx2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/VxxxxxxxxmW4=
    ```

## Set an Environment Variable with Python

1. Using a python shell session

    ```python
    import os
    os.environ['ENVIRONMENT_VARIABLE_NAME'] = 'ENVIRONMENT_VARIABLE_VALUE'
    ```

1. Run the following in a python shell session to verify

    ```python
    os.environ['ENVIRONMENT_VARIABLE_NAME']
    ```

Table of Environment Variables

| **Environment Variable Name**  | **Value Found in portal.azure.com**  | **Details about finding the value**  | **File Referencing Environment Variable** |
|:---------|:---------|:---------|:---------|
| `IOTHUB_CONNECTION_STRING`  | IoT Hub > Shared Access Policies > service (policy) > Primary Connection String |         | `c2dsendmsg.py` |
| `IOTHUB_DEVICE_CONNECTION_STRING` | IoT Hub > Devices > {your device} > Primary Connection String |         | `d2ceventhublistener.py, c2dlistener.py, d2csendmsg.py, c2dmaproutelistener` |
| `STORAGE_CONNECTION_STRING` | Storage Account > Access Keys > Connection String | [Manage storage account access keys](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/storage/common/storage-account-keys-manage.md#manage-storage-account-access-keys) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `STORAGE_CONTAINER_NAME` | Storage Account > Containers > Name | [Manage storage account access keys](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/storage/common/storage-account-keys-manage.md#manage-storage-account-access-keys) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `EVENTHUB_CONNECTION_STRING` | IoT Hub > Built-in endpoints > Event Hub-compatible endpoint | [Read from the built-in endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin#read-from-the-built-in-endpoint) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `EVENTHUB_NAME` | IoT Hub > Built-in endpoints > Event Hub-compatible name | [Read from the built-in endpoint](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin#read-from-the-built-in-endpoint) | `d2ceventhublistener.py, c2dmaproutelistener.py` |
| `MAP_KEY` | Azure Maps > Authentication > Primary Key | [Get the primary key for your account](https://learn.microsoft.com/en-us/azure/azure-maps/quick-demo-map-app#get-the-primary-key-for-your-account) | c2devent |

## Set all your environment variables with a single PowerShell file

You'll need to set all but the MAP_KEY environment variables in order to successfully use the tutorials. You'll get to setting the MAP_KEY later when you work on the Map Routing tutorials.

1. Open your GitHub cloned directory with the **File > Open Folder...** menu in Visual Studio Code.
1. Create a file named `environmentVariables.ps1`.
1. Copy and paste the following script into the file and replace the `{Value}`

    ```powershell
    [System.Environment]::SetEnvironmentVariable("IOTHUB_CONNECTION_STRING","{Value}","Machine")
    [System.Environment]::SetEnvironmentVariable("IOTHUB_DEVICE_CONNECTION_STRING","{Value}","Machine")
    [System.Environment]::SetEnvironmentVariable("STORAGE_CONNECTION_STRING","{Value}","Machine")
    [System.Environment]::SetEnvironmentVariable("STORAGE_CONTAINER_NAME","{Value}","Machine")
    [System.Environment]::SetEnvironmentVariable("EVENTHUB_CONNECTION_STRING","{Value}","Machine")
    [System.Environment]::SetEnvironmentVariable("EVENTHUB_NAME","{Value}","Machine")
    ```

1. Open a [PowerShell session from Windows as an administrator](https://www.howtogeek.com/742916/how-to-open-windows-powershell-as-an-admin-in-windows-10/#:~:text=You%20can%20open%20Windows%20PowerShell%20with%20administrator%20privileges,and%20then%20type%20%E2%80%9Cpowershell%E2%80%9D%20in%20the%20text%20box.).
1. Change the directory to your GitHub cloned directory, for example `PS > cd "C:\repos\various"`
1. Run the following script to set your environment variables.

    ```powershell
    .\environementVars.ps1
    ```

    For example,

    ```powershell
    PS C:\repos\various> .\environementVars.ps1
    ```

## Set all your environment variables with a python file

You'll need to set all but the MAP_KEY environment variables in order to successfully use the tutorials. You'll get to setting the MAP_KEY later when you work on the Map Routing tutorials.

1. Create a file named `environmentVariables.py`.
1. Copy and paste the following script into the file and replace the `VALUE` with the appropriate value found in the table above.

    ```python
    os.environ['IOTHUB_CONNECTION_STRING'] = 'VALUE'
    os.environ['IOTHUB_DEVICE_CONNECTION_STRING'] = 'VALUE'
    os.environ['STORAGE_CONNECTION_STRING'] = 'VALUE'
    os.environ['STORAGE_CONTAINER_NAME'] = 'VALUE'
    os.environ['EVENTHUB_CONNECTION_STRING'] = 'VALUE'
    os.environ['EVENTHUB_NAME'] = 'VALUE'
    ```

1. Change the directory to your GitHub cloned directory, for example `PS > cd "C:\repos\various"`
1. Run the file in a python shell environment: 

    ```powershell
    .\environementVars.ps1
    ```

    For example,

    ```powershell
    PS C:\repos\various> .\environementVars.ps1
    ```


## Clean up your Environment Variables

1. Open a [PowerShell session from Windows as an administrator](https://www.howtogeek.com/742916/how-to-open-windows-powershell-as-an-admin-in-windows-10/#:~:text=You%20can%20open%20Windows%20PowerShell%20with%20administrator%20privileges,and%20then%20type%20%E2%80%9Cpowershell%E2%80%9D%20in%20the%20text%20box.).
1. Run the following command by replacing `{Environment Variable Name}` with an environment variable from the table above.

    ```powershell
    [System.Environment]::SetEnvironmentVariable("{Environment Variable Name}",$null)
    ```

    For example,

    ```powershell
    [System.Environment]::SetEnvironmentVariable("IOTHUB_CONNECTION_STRING",$null)
    ```
