---
title: Create a Simulated Device
description: Create a symmetric key device 
author: jbeman@hotmail.com
---

# Tutorial: Create a Simulated Device

In this tutorial, you learn how to:

- Create a simulated IoT device

Security is essential for any device on the public internet. When you create a device for Azure IoT, you MUST have a secure way to encrypt/decrypt the calls between the device and the cloud service. The simplest way to quickly create a device is with [symmetric key encryption](https://www.ibm.com/docs/en/ztpf/2020?topic=concepts-symmetric-cryptography). A symmetric key is a password that is stored in the device and in the cloud service. Managing devices with symmetric keys becomes increasingly difficult as you add more devices to your IoT Hub. Therefore, the preferred way to create a device for production is to use an asymmetric key, or x509 certificate, which we will cover in a later tutorial.

## Create a Device with a Symmetric Key

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