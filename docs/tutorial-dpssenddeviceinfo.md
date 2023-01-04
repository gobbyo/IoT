---
title: Send Device Information to the Cloud with DPS
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

# Tutorial: Send Device Information to the Cloud with DPS

In this tutorial, you learn how to:

- Add environment variables to your Raspberry Pi
- Send Device Information to the Cloud when Booting Up your Raspberry Pi

[todo] Diagram needed.

## Prerequisites

- Completed the...

## Add Variables to your Environment (.env) File

1. Open your `.env` file in the root of your github forked clone directory `IoT`.
1. Add the following entries to your `.env` file

    ```python
    DPS_HOST="{`service endpoint` from the overview page of your Device Provisioning Service}"
    DPS_REGISTRATIONID="{created in earlier in this tutorial}"
    DPS_SCOPEID="{`ID scope` from the overview page of your Device Provisioning Service}"
    X509_CERT_FILE="{full path to your device `.pem` file}"
    X509_KEY_FILE="{full path to your device `.key` file}"
    X509_PASS_PHRASE="{pass phrase created in the previous tutorial}"
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
    me@raspberrypi:~/repos/IoT $ python
    >>> from decouple import config
    >>> print(config("DPS_HOST"))
    dpsztputik7h47qi.azure-devices-provisioning.net
    ```

## Send Device Information to the Cloud when Booting Up your Raspberry Pi

1. Create a file called `provisiondevicex509.py` in the `python/raspberrypi/` directory of your git hub clone, for example `$ ~/repos/IoT/python/raspberrypi/provisiondevicex509.py`
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