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

## Verify your device enrollment

1. Open the [Azure portal](https://portal.azure.com)
1. Verify your device has enrolled by following the diagram below. 1️⃣ Open your your Device Provisioning Service, 2️⃣ from the left pane select **Settings > Manage enrollments**, from the right pane select **Individual Enrollments**, finally 4️⃣ verify your device registration ID is present.

    ![lnk_verifyenrollment]

## Add Variables to your Environment (`.env`) File

1. Open your `.env` file in the root of your github forked clone directory `various`.
1. Add the following entries to your `.env` file


    ```python
    DPS_HOST="{`service endpoint` from the overview page of your Device Provisioning Service}"
    DPS_REGISTRATIONID="{created in earlier in this tutorial}"
    DPS_SCOPEID="{`ID scope` from the overview page of your Device Provisioning Service}"
    X509_CERT_FILE="{full path to your `.pem` file}"
    X509_KEY_FILE="{full path to your `.key` file}"
    X509_PASS_PHRASE="{pass phrase created earlier in this tutorial}"
    ```

    For example,

    ```python
    DPS_HOST="dpsztputik7h47qi.azure-devices-provisioning.net"
    DPS_REGISTRATIONID="raspberrypi-b"
    DPS_SCOPEID="0ne008D45AC"
    X509_CERT_FILE="/home/me/certs/raspberrypi2.pem"
    X509_KEY_FILE="/home/me/certs/raspberrypi2.key"
    X509_PASS_PHRASE="1234"

1. Verify your environment file variables by opening a Visual Studio Code remote terminal session connected to your raspberry pi and run the following scripts.

    ```python
    python
    from decouple import config
    print(config('DPS_HOST'))
    ```

    For example,

    ```python
    me@raspberrypi:~/repos/various $ python
    >>> from decouple import config
    >>> print(config("DPS_HOST"))
    dpsztputik7h47qi.azure-devices-provisioning.net
    ```

1. Create a file called `provisiondevicex509.py` in the `python/raspberrypi/` directory of your git hub clone, for example `$ ~/repos/various/python/raspberrypi/provisiondevicex509.py`
1. Copy and paste the following code to your `provisiondevicex509.py` file.

    ```python
    provisioning_host = config("DPS_HOST")
    id_scope = config("DPS_SCOPEID")
    registration_id = config("DPS_REGISTRATIONID")
    ```

1. Copy and paste the following method to your `provisiondevicex509.py` file.

    ```python
    async def send_message(device_client):
        print("sending message. Code ID = f461ee5e-d7e4-4bea-8953-d0c7b113d522")
        hostname = socket.gethostname()
        ip_address = raspipaddress.get_ip_address()
        
        msg = Message('{{ "Hostname":"{0}", "IPAddress":"{1}" }}'.format(hostname, ip_address) )
        msg.message_id = uuid.uuid4()
        await device_client.send_message(msg)
        print("message sent: {0} ".format(msg))
    ```

1. Copy and past the main method to your `provisiondevicex509.py` file.

    ```python
    async def main():
        x509 = X509(
            cert_file=config("X509_CERT_FILE"),
            key_file=config("X509_KEY_FILE"),
            pass_phrase=config("X509_PASS_PHRASE"),
        )
    
        print("Creating provisioning client. Code Id = f1973054-24af-4a6b-9a79-409abcd7d27f")
        provisioning_device_client = ProvisioningDeviceClient.create_from_x509_certificate(
            provisioning_host=provisioning_host,
            registration_id=registration_id,
            id_scope=id_scope,
            x509=x509,
        )
    
        registration_result = await provisioning_device_client.register()
    
        if registration_result.status == "assigned":
            device_client = IoTHubDeviceClient.create_from_x509_certificate(
                x509=x509,
                hostname=registration_result.registration_state.assigned_hub,
                device_id=registration_result.registration_state.device_id,
            )
    
            await device_client.connect()
            await send_message(device_client)
            await device_client.disconnect()
        else:
            print("Error: Cannot send telemetry from the provisioned device. CodeID = f586eb27-5b36-46fa-ae25-5ffb3ad19efc")
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```

1. Run the code in your debugger using Visual Studio Code and verify you successfully sent a message as follows:

    ```azurecli
    Creating provisioning client. Code Id = f1973054-24af-4a6b-9a79-409abcd7d27f
    sending message. Code ID = f461ee5e-d7e4-4bea-8953-d0c7b113d522
    message sent: { "Hostname":"raspberrypi2", "IPAddress":"192.168.1.109" }
    ```

1. Verify your message is in IoT Hub following the diagram below. 1️⃣ Select your Stream Analytics Job from the [Azure Portal](https://portal.azure.com), 2️⃣ select **Settings > Query** in the left pane, and 3️⃣ select your IoT hub in the middle pane. 4️⃣ Select **() Raw** From the Input Preview (right pane), finally 5️⃣ verify your hostname and ipaddress.

    ![lnk_verifymessage]

## Next steps

[Tutorial: Send Hostname and IP address to the Cloud](tutorial-rasp-d2cipandhostname.md)

<!--images-->

[lnk_deviceenrollment]: media/tutorial-dpsx509deviceenrollment/downloadpemfile.png
[lnk_verifyenrollment]: media/tutorial-dpsx509deviceenrollment/verifyenrollment.png
[lnk_verifymessage]: media/tutorial-dpsx509deviceenrollment/verifymessage.png