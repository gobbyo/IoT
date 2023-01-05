---
title: Deploy and Configure a Device Provisioning Service (DPS)
description: This tutorial has you deploy a Device Provisioning Service and add IoT Hub to the Device Provisioning Service
author: jbeman@hotmail.com
---

# Tutorial: Deploy and Configure a Device Provisioning Service

In this tutorial you'll...

- Deploy a Device Provisioning Service
- Add IoT Hub to the Device Provisioning Service

**Azure Device Provisioning Service (DPS)** is a cloud service that enables you to automatically register and provision devices to your Azure IoT hub. It simplifies the process of setting up and managing a fleet of devices by allowing you to provision devices to your IoT hub automatically and securely, without manual intervention. There are several benefits to using Azure DPS:

- *Ease of use*. With DPS, you can provision thousands of devices with just a few clicks, saving time and effort.
- *Secure registration*. DPS uses a secure, decentralized registration process to ensure that only authorized devices can connect to your IoT hub.
- *Scalability*. DPS can handle a large number of devices and can scale up or down as needed.
- *Flexibility*. DPS supports multiple device types and can be used with a variety of communication protocols, including HTTP, MQTT, and AMQP.
- *Cost effectiveness*. DPS can help you save money by eliminating the need for manual provisioning processes and reducing the risk of errors that can lead to lost or damaged devices.

Overall, Azure DPS is a useful tool for anyone looking to set up and manage a fleet of devices connected to Azure IoT hub. It simplifies the process and helps ensure that your devices are securely and efficiently registered and provisioned. As a best practice, we'll use DPS to manage our Raspberry Pi device throughout future tutorials.

## Prerequisites

- Completed the [Tutorial: Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)

## Deploy a Device Provisioning Service

In this section you'll use PowerShell to create a new resource group, then you'll deploy DPS using an ARM template. Following the diagram below,

1. Create a new resource group for DPS
1. Deploy DPS using an ARM template

![lnk_installdps]

Before starting this section be sure to open Visual Studio (VS) Code, select the `Terminal > New Terminal...` menu and [Authenticate your Azure Subscription](howto-connecttoazure.md) using the PowerShell (PS) session.

1. Run the following script to set a new resource group name to the `$rg` powershell variable. Replace `{new resource group name}` with the new name of your resource group.

    ```powershell
    $rg = "{resource group name}"
    ```

    For example,

    ```powershell
    PS > $rg = "myDpsRG"
    ```

1. Run the following script to set the PowerShell variable to a region location for your resource group.  Replace `{region location}` with the location of your resource group.

    ```powershell
    $location = "{region location}"
    ```

    For example,

    ```powershell
    $location = "Central US"
    ```

1. Run the following script to create a new resource group

    ```powershell
    New-AzResourceGroup -Name $rg -Location $location
    ```

    For example,

    ```powershell
    PS > New-AzResourceGroup -Name $rg -Location $location

    ResourceGroupName : myDpsRG
    Location          : centralus
    ProvisioningState : Succeeded
    Tags              : 
    ResourceId        : /subscriptions/d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda/resourceGroups/MessagingRG
    
    ```

1. Deploy the Device Provisioning Service ARM template. Be sure to replace the `{path to your Device Provisioning Service ARM template}` in the script sample,

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -location $location `
    -TemplateFile "{path to your Device Provisioning Service ARM template}"
    ```

    For example,

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -location $location `
    -TemplateFile "C:\repos\IoT\arm\dps.json"
    ```

1. Verify your DPS has successfully deployed.

## Add IoT Hub to DPS

In this section you'll use PowerShell to add your IoT hub to DPS per the diagram:

1. From [Azure IoT Hub portal](https://portal.azure.com) copy the `Security Settings > Shared access policies > iothubowner > Primary connection string`
1. Run a PowerShell script `Add-AzIoTDeviceProvisioningServiceLinkedHub` using the Primary connection string you copied in the previous step
1. DPS connects to your IoT Hub and retains it in its list of IoT Hubs.

![lnk_addhubtodps]

1. Set the variable `$hubConnectionString` by replacing the `{your iothubowner primary connection string}` with your iot hub owner primary connection string.

    ```powershell
    $hubConnectionString = "{your iothubowner primary connection string}"
    ```

    For example,

    ```powershell
    $hubConnectionString = "HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/Vxxxxxxxxxxxx7mW4="
    ```

1. Run the following powershell script to add a link to your IoT Hub. Replace the `{device provisioning service name}` with the name of your newly deployed device provisioning service. Replace the `{iot hub region}` with your IoT Hub regional location, e.g. "Central US"

    ```powershell
    Add-AzIoTDeviceProvisioningServiceLinkedHub `
        -ResourceGroupName $rg `
        -Name "{device provisioning service name}" `
        -IotHubConnectionString $hubConnectionString `
        -IotHubLocation "{iot hub region}"
    ```

    For example,

    ```powershell
    PS C:\repos\IoT> $hubConnectionString = "HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/Vxxxxxxxxxxxx7mW4="
    PS C:\repos\IoT> Add-AzIoTDeviceProvisioningServiceLinkedHub `
    >> -ResourceGroupName $rg `
    >> -Name "dpsztputik7h47qi" `
    >> -IotHubConnectionString $hubConnectionString `
    >> -IotHubLocation "centralus"
    
    ResourceGroupName     : myDpsRG
    Name                  : dpsztputik7h47qi
    LinkedHubName         : HubMsgHubw2lu5yeop2qwy.azure-devices.net
    ConnectionString      : HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;SharedAccessKeyName=iothubowner;Shared                         AccessKey=****
    AllocationWeight      : ApplyAllocationPolicy : False
    Location              : centralus
    ```

1. Verify you have successfully deployed a new resource group and DPS by opening the [Azure Portal](https://portal.azure.com). Following the diagram below: 1️⃣ Open the DPS resource group you created earlier in this tutorial. 2️⃣ Verify the deployment succeeded, if not, then click on the `Deployments` hyperlink to troubleshoot the issue. 3️⃣ Verify the presence of your new DPS.

![lnk_verifydps]

## Next Steps

[Tutorial: Create a x509 Certificate and Enroll Your Device](tutorial-dpsx509deviceenrollment.md)

<!-- images -->

[lnk_installdps]: media/tutorial-deploydps/installdps.png
[lnk_addhubtodps]: media/tutorial-deploydps/addhubtodps.png
[lnk_verifydps]: media/tutorial-deploydps/verifydpsdeployment.png
