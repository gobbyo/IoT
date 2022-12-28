---
title: Create a x509 Certificate and Enroll Your Device
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Create a x509 Certificate and Enroll Your Device

<!-- 2. Introductory paragraph 
Required. Lead with a light intro that describes, in customer-friendly language, 
what the customer will learn, or do, or accomplish. Answer the fundamental “why 
would I want to do this?” question. Keep it short.
-->

[Add your introductory paragraph]

<!-- 3. Tutorial outline 
Required. Use the format provided in the list below.
-->

In this tutorial, you learn how to:

> [!div class="checklist"]
> * All tutorials include a list summarizing the steps to completion
> * Each of these bullet points align to a key H2
> * Use these green checkboxes in a tutorial

<!-- 4. Prerequisites 
Required. First prerequisite is a link to a free trial account if one exists. If there 
are no prerequisites, state that no prerequisites are needed for this tutorial.
-->

## Prerequisites

- <!-- An Azure account with an active subscription. [Create an account for free]
  (https://azure.microsoft.com/free/?WT.mc_id=A261C142F). -->
- <!-- prerequisite 2 -->
- <!-- prerequisite n -->

<!-- 5. H2s
Required. Give each H2 a heading that sets expectations for the content that follows. 
Follow the H2 headings with a sentence about how the section contributes to the whole.
-->

## Create a Certificate
<!-- Introduction paragraph -->

1. Remotely connect to your device from Visual Studio Code
1. Create a directory to hold your certs then change to the new directory.

    ```azurecli
    cd ~
    mkdir certs
    cd certs
    ```

1. Create a certificate using the following openssl script in a Visual Studio Code terminal session.

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
<!-- Introduction paragraph -->
1. Open a terminal session from Visual Studio Code on your Windows machine.

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
    PS C:\repos\various> Add-AzIoTDeviceProvisioningServiceEnrollment `
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

<!-- 6. Clean up resources
Required. If resources were created during the tutorial. If no resources were created, 
state that there are no resources to clean up in this section.
-->
## Enroll your device

1. Create a file named [todo].
1. Add the following import statements to your 

import asyncio
import socket
import uuid
from decouple import config
from azure.iot.device import Message,X509
from azure.iot.device.aio import ProvisioningDeviceClient, IoTHubDeviceClient
import modules.raspipaddress as raspipaddress

## Clean up resources

If you're not going to continue to use this application, delete
<resources> with the following steps:

1. From the left-hand menu...
1. ...click Delete, type...and then click Delete

<!-- 7. Next steps
Required: A single link in the blue box format. Point to the next logical tutorial 
in a series, or, if there are no other tutorials, to some other cool thing the 
customer can do. 
-->

## Next steps

Advance to the next article to learn how to create...
> [!div class="nextstepaction"]
> [Next steps button](contribute-how-to-mvc-tutorial.md)

<!--images-->

[lnk_deviceenrollment]: media/tutorial-dpsx509deviceenrollment/downloadpemfile.png
[lnk_verifyenrollment]: media/tutorial-dpsx509deviceenrollment/verifyenrollment.png