# Create a Device

1. Create a device.

    ```powershell
    Add-AzIotHubDevice `
    -ResourceGroupName $rg `
    -IotHubName "{name of your IoTHub}" `
    -DeviceId "{new device name}" `
    -AuthMethod "shared_private_key"
    ```

    For example,

    ```powershell
    Add-AzIotHubDevice `
    -ResourceGroupName $rg `
    -IotHubName "myMessagingHubd3fqt3vtn3zbm" `
    -DeviceId "myDevice1" `
    -AuthMethod "shared_private_key"
    ```
