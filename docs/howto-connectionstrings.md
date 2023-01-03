# How to Find and Set Your Connection Strings

## On your Raspberry Pi

1. Install decouple, see https://pypi.org/project/python-decouple/ for details.

    ```python
    pip install python-decouple
    ```

1. Create an '.env' file and save it to GitHub root (e.g. `c:/repos/IoT`) directory from your GitHub forked clone, then add your entries as follows:

    ```python
    IOTHUB_CONNECTION_STRING="{IoT hub Primary Connection String}"
    IOTHUB_DEVICE_CONNECTION_STRING="{Your Device Connection String}"
    ```

1. Obtain the environment variable by opening a python session and run the following script

    ```python
    cd {github forked clone root}
    python
    from decouple import config
    config('IOTHUB_DEVICE_CONNECTION_STRING')
    ```

    for example,

    ```python
    cd c:/repos/IoT 
    c:/repos/IoT> python
    >>> from decouple import config
    >>> config('IOTHUB_DEVICE_CONNECTION_STRING')
    >>> 'HostName=HubMsg********p2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8IrO********ZUkg='
    ```

## On your Windows Cloud Machine

1. Add system environment variables by opening a PowerShell command prompt in [Administrative mode](https://learn.microsoft.com/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.3#how-do-i-launch-powershell) and run the following script.

    ```powershell
    [Environment]::SetEnvironmentVariable('IOTHUB_CONNECTION_STRING','{connection string from previous step}','Machine')
    ```

1. Obtain the environment variable by opening a python session in the same directory as the '.env' file where you'll run your scripts.

    ```python
    import os
    os.getenv('IOTHUB_DEVICE_CONNECTION_STRING')
    ```

    for example,

    ```python
    c:/repos/IoT python
    >>> import os
    >>> os.getenv('IOTHUB_DEVICE_CONNECTION_STRING')
    >>> 'HostName=HubMsg********p2qwy.azure-devices.net;DeviceId=myDevice;SharedAccessKey=8IrO********ZUkg='
    ```

1. Delete your system variable from a PowerShell command prompt in Administrative mode by changing the `{your environment variable}` name and running following script:

    ```powershell
    [Environment]::SetEnvironmentVariable('{your environment variable}',$Null,'Machine')
    ```

    For example

    ```powershell
    [Environment]::SetEnvironmentVariable('IOTHUB_CONNECTION_STRING',$Null,'Machine')
    ```    

## Resources

- [Python Decouple](https://pypi.org/project/python-decouple/)
- [PowerShell Administrative mode](https://learn.microsoft.com/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.3#how-do-i-launch-powershell)