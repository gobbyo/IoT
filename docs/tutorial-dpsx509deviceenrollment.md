---
title: Create a x509 Certificate and Enroll Your Device
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Create an x509 Certificate to Enroll Your Device

In this tutorial, you learn how to:

- Create an x509 Certificate
- Add environment variables to your Raspberry Pi for device enrollment

In the previous tutorials we used symmetric keys to manage our device. However, moving forward in our tutorials we'll use x509 certificates. An **x509 certificate** is a digital certificate that is used to authenticate the identity of a device or a user on a network. x509 certificates are based on the x509 standard, which is a widely used standard for public key infrastructure (PKI). There are several advantages to using X509 certificates for device security over symmetric keys:

- *Stronger security*. X509 certificates use public key infrastructure (PKI) for authentication, which provides stronger security than symmetric key authentication. In PKI, each device has a unique private key that is used to sign messages, and a corresponding public key that is used to verify the authenticity of the messages. This makes it more difficult for an attacker to impersonate a device or intercept communications.
- *Ease of use*. X509 certificates can be easily managed using standard tools and processes, such as certificate authorities (CAs) and certificate revocation lists (CRLs). This makes it easier to set up and maintain a secure device network.
- *Scalability*. X509 certificates can be used to securely authenticate a large number of devices, making them well-suited for use in large-scale deployments.
- *Interoperability*. X509 certificates are widely used and supported, which makes it easier to integrate devices from different vendors into a single system.

[todo] Diagram needed.

## Prerequisites

- Completed the [Tutorial: Deploy and Configure a Device Provisioning Service (DPS)](tutorial-deploydps.md)

## Create a Certificate
In this section you'll remotely connect to your Raspberry Pi to create a public and private key for your certificate. The private key remains on your device whereas you'll copy the public certificate for use by your IoT Hub.

1. [Remotely connect to your Raspberry Pi](tutorial-rasp-connect.md) from Visual Studio Code
1. Create a directory to hold your certs then change to the new directory.

    ```azurecli
    cd ~
    mkdir certs
    cd certs
    ```

1. Create a certificate using the following openssl script in a Visual Studio Code terminal session.  Enter `1234` for your PEM pass phrase.

    ```azurecli
    openssl req -outform PEM -x509 -sha256 -newkey rsa:4096 -keyout {yourDeviceName}.key -out {yourDeviceName}.pem -days {days until expired} -extensions usr_cert -addext extendedKeyUsage=clientAuth -subj "/CN={your device registration id, a-z,A-Z,- or _, only}"
    ```

    For example,

    ```azurecli
    $ openssl req -outform PEM -x509 -sha256 -newkey rsa:4096 -keyout raspberrypi2.key -out raspberrypi2.pem -days 365 -extensions usr_cert -addext extendedKeyUsage=clientAuth -subj "/CN=raspberrypi-b"
    Generating a RSA private key
    ............................................++++
    ................................................................................++++
    writing new private key to 'raspberrypi2.key'
    Enter PEM pass phrase:
    Verifying - Enter PEM pass phrase:
    -----
    ```

1. Copy the .pem file down to your local drive. Following the diagram below, 1️⃣ select the `File > Open Folder...` menu item, 2️⃣ right-click the `.pem` file you created to show the submenu, and 3️⃣ select the `Download...` menu item.

    ![lnk_deviceenrollment]

## Enroll Your Device

Device enrollment refers to the process of registering a device with DPS and assigning it to an Azure IoT hub. This process allows the device to securely connect to your IoT hub and start sending and receiving data.

Device enrollment in Azure DPS is typically used when you have a large number of devices that need to be registered with your IoT hub. With DPS, you can automate the enrollment process, eliminating the need for manual intervention and making it easier to set up and manage a fleet of devices.

To enroll a device in Azure DPS, you first need to create a device registration in the DPS portal. This will create a unique identity for the device, which can then be used to authenticate the device when it connects to your IoT hub. The device will also need to be provisioned with the necessary connectivity information, such as the IoT hub hostname and device-specific credentials.

Once the device is enrolled, it can start sending and receiving data to and from your IoT hub. You can use Azure IoT hub to set up device-to-cloud and cloud-to-device communication, as well as to monitor and manage your devices.

Before starting this section be sure to open Visual Studio (VS) Code, select the `Terminal > New Terminal...` menu and [Authenticate your Azure Subscription](howto-connecttoazure.md) using the PowerShell (PS) session.

1. Run the following PowerShell script

    ```powershell
    Add-AzIoTDeviceProvisioningServiceEnrollment `
    -ResourceGroupName "{your Device Provisioning Service resource group name}" `
    -DpsName "{name of your Device Provisioning Service}" `
    -RegistrationId "{the Common Name (CN) in the certificate you created}" `
    -AttestationType X509 `
    -PrimaryCertificate "{path to your .pem file}"
    ```

    For example,

    ```powershell
    PS C:\repos\IoT> Add-AzIoTDeviceProvisioningServiceEnrollment `
    >> -ResourceGroupName "myDpsRG" `
    >> -DpsName "dpsztputik7h47qi" `
    >> -RegistrationId "raspberrypi-b" `
    >> -AttestationType X509 `
    Created                      : 12/27/2022 15:12
    Last Updated                 : 12/27/2022 15:12
    ETag                         : IjE3MDFjNmVlLTAwMDAtMDMwMC0wMDAwLTYzYWI4MDZiMDAwMCI=
    Initial Twin State           : {
                                     "properties": {
                                       "desired": {}
                                     },
                                     "tags": {}
                                   }
    ```

## Verify your device enrollment

1. Open the [Azure portal](https://portal.azure.com)
1. Verify your device has enrolled by following the diagram below. 1️⃣ Open your your Device Provisioning Service, 2️⃣ from the left pane select **Settings > Manage enrollments**, from the right pane select **Individual Enrollments**, finally 4️⃣ verify your device registration ID is present.

    ![lnk_verifyenrollment]

## Next steps

[Tutorial: Send Hostname and IP address to the Cloud](tutorial-rasp-d2cipandhostname.md)

<!--images-->

[lnk_deviceenrollment]: media/tutorial-dpsx509deviceenrollment/downloadpemfile.png
[lnk_verifyenrollment]: media/tutorial-dpsx509deviceenrollment/verifyenrollment.png
[lnk_verifymessage]: media/tutorial-dpsx509deviceenrollment/verifymessage.png