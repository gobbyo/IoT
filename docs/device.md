# Create a Device

1. Create a device.

    ```powershell
    Add-AzIotHubDevice `
    -ResourceGroupName "{name of your IoTHub's resource group}" `
    -IotHubName "{name of your IoTHub}" `
    -DeviceId "{new device name}" `
    -AuthMethod "shared_private_key"
    ```

    For example,

    ```powershell
    Add-AzIotHubDevice `
    -ResourceGroupName "HubMsgRG" `
    -IotHubName "HubMsgHubw2lu5yeop2qwy" `
    -DeviceId "myMapRoutingDevice" `
    -AuthMethod "shared_private_key"
    ```

2. Remove your IoT Hub device

    ```powershell
    Remove-AzIotHubDevice `
    -ResourceGroupName "{name of your IoTHub's resource group}" `
    -IotHubName "{name of your IoTHub}" `
    -DeviceId "{device name}"
    ```

    For example,

    ```powershell
    Remove-AzIotHubDevice `
    -ResourceGroupName "HubMsgFreeRG" `
    -IotHubName "HubMsgFreeHubcv5xo2lejevg6" `
    -DeviceId "myMapRoutingDevice"
    ```
