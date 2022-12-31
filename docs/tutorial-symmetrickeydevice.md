---
title: Create a Simulated Device
description: Create a symmetric key device 
author: jbeman@hotmail.com
---

# Tutorial: Create a Simulated Device

In this tutorial, you learn how to:

- Create a simulated IoT device

Security is important for IoT devices for a number of reasons:

- **Confidentiality**. IoT devices often collect and transmit sensitive data, such as personal information, financial data, or proprietary business information. Ensuring the security of this data is important to protect the confidentiality of the individuals or organizations involved.
- **Integrity**. Ensuring the integrity of data transmitted by IoT devices is important to ensure that the data has not been tampered with or altered in any way.
- **Availability**. Ensuring the availability of IoT devices is important to ensure that they can perform their intended functions and provide the expected level of service.
- **Safety**. In some cases, IoT devices are used in safety-critical applications, such as in healthcare or transportation. Ensuring the security of these devices is important to prevent accidents or other adverse outcomes.

Overall, security is an important consideration for IoT devices, as it helps protect the confidentiality, integrity, availability, and safety of the data and systems involved. As you progress through these tutorials you'll use the best practices to securely code your IoT device.

## Prerequisites

- Completed the [Tutorial: Deploy an Azure IoT Hub](tutorial-deployiothub.md)

## Create a Device with a Symmetric Key

In this section you'll create a device in IoT Hub that uses a symmetric key. The simplest way to quickly create a device is with [symmetric key encryption](https://www.ibm.com/docs/en/ztpf/2020?topic=concepts-symmetric-cryptography).

When your device communicates to the cloud, the transmission needs to be encrypted in a secure way. A symmetric key is typically a password is used for both encryption and decryption of data. Symmetric keys are typically shorter and easier to generate and manage than the keys used in asymmetric (or public-key) cryptography. This makes them well-suited for use in applications where performance is a key concern.

However, symmetric-key cryptography has a number of limitations, including the need to securely share the key between the sender and receiver of the data, and the inability to authenticate the sender of the data. Managing devices with symmetric keys becomes increasingly difficult as you add more devices to your IoT Hub. Therefore, the preferred way to create a device for production is to use an asymmetric key, or x509 certificate, which we will cover in a later tutorial.

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