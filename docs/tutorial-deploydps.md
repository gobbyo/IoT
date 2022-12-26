# Deploy and Configure a Device Provisioning Service (DPS)

## Prerequisites

- [Configure your Windows Machine](tutorial-configure.md)

## Deploy Device Provisioning Service

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

1. Deploy the Device Provisioning Service ARM template

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -location $location `
    -TemplateFile "C:\repos\various\arm\dps.json"
    ```

    For example,

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -location $location `
    -TemplateFile "C:\repos\various\arm\dps.json"
    ```

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
    PS C:\repos\various> $hubConnectionString = "HostName=HubMsgHubw2lu5yeop2qwy.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=92/Vxxxxxxxxxxxx7mW4="
    PS C:\repos\various> Add-AzIoTDeviceProvisioningServiceLinkedHub `
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

`openssl req -outform PEM -x509 -sha256 -newkey rsa:4096 -keyout device.key -out device.pem -days 30 -extensions usr_cert -addext extendedKeyUsage=clientAuth -subj "/CN={device registration id, a-z,A-Z,- or _, only}"`
