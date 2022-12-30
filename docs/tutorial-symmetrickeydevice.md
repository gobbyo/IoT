# Tutorial: Create a Simulated Device

Creating an IoT device with a symmetric key is the easiest way to create a device.  This is best only for testing and proof of concept. The preferred way to create a device for production is with an x509 certificate which we will cover in a later tutorial.

1. Create a device in the [Azure Portal for IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal#register-a-new-device-in-the-iot-hub).  Note this tutorial shows you where to obtain the device connection string.
1. Create a device using PowerShell.

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
    -DeviceId "myDevice" `
    -AuthMethod "shared_private_key"
    ```

1. Remove your device using PowerShell

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
    -DeviceId "myDevice"
    ```

## Next Steps

[Tutorial: Send a Message from the Cloud to a Simulated Device](tutorial-cloudtodevicemsg.md)