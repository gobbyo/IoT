---
title: Deploy and Configure StreamAnalytics
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Deploy and Configure StreamAnalytics

In this tutorial you'll...

[todo] image needed

## Prerequisites

[todo]

## Deploy

1. Run the following script to connect to your Azure subscription. Replace `{your subscription ID}` with the identifier to your Azure subscription.

    ```powershell
    Connect-AzAccount -SubscriptionId "{your subscription ID}"
    ```

    For example,

    ```powershell
    PS > Connect-AzAccount -SubscriptionId "d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda"
    ```

1. Run the following script to set a new resource group name to the `$rg` powershell variable. Replace `{new resource group name}` with the new name of your resource group.

    ```powershell
    $streamJobName = "{new stream to storage project name}"
    $rg = ($projectName + "RG")
    ```

    For example,

    ```powershell
    PS > $streamJobName = "StreamToStorage"
    PS > $rg = ($streamJobName + "RG")
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

    ResourceGroupName : StreamToStorageRG
    Location          : centralus
    ProvisioningState : Succeeded
    Tags              : 
    ResourceId        : /subscriptions/d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda/resourceGroups/myMessagingRG
    
    ```

1. Run the following script to set the path to the ARM template `stream.json`

    ```powershell
    $templateFile = "{path to stream.json}"
    ```

    For example,

    ```powershell
    PS > $templateFile = "C:\\repos\\various\\arm\\stream.json"
    ```

1. Deploy the stream analytics ARM template

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile $templateFile `
    -location $location `
    -streamJobName $streamJobName `
    -numberOfStreamingUnits 1
    ```

    For example,

    ```powershell
    PS> New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile $templateFile `
    -location $location `
    -streamJobName $streamJobName `
    -numberOfStreamingUnits 1
    ```

## Configure

1. Open your StreamAnalytics service, named `$streamJobName`, in portal.azure.com
1. In the left pane under `Job topology`, select `Inputs`
1. Select `+ Add Stream Input > IoT Hub`, and fill in the form as follows,
    |Item  |Action  |Description  |
    |:---------|:---------|:---------|
    |Input Alias Text Box|myIoTHub|The name of your IoT Hub, for example, "HubMsgHubw2lu5yeop2qwy"|
    |Subscription Dropdown|{your subscription}|Select the name of your subscription|
    |IoT Hub Text Box|Select your IoT Hub|For example, "HubMsgHubw2lu5yeop2qwy"|
    |Consumer Group Text Box|Select `$Default`|The readers with access to IoT Hub|
    |Shared Access Policy Name Text Box|`iotHubOwner`|The access policy created with IoT Hub|
    |Shared Access Policy Key Secrets Text Box|Provided by default|         |
    |Endpoint Dropdown|Select `Messaging`| For devices that message to the cloud |
    |Encoding Dropdown|Select `UTF-8`| Message encoding |
    |Event Compression Type Dropdown|Select `None`| No message compression |

1. Select the "Save" button. This action enables the stream analytics service to pull messages from IoT Hub.
1. In the left pane under `Job topology`, select `Outputs`
1. Select `Add > Blob Storage/ADLS Gen2` and fill in the form as follows,
    |Item  |Action  |Description  |
    |:---------|:---------|:---------|
    |Input Alias Text Box|myDeviceStorage|The name of your IoT Hub, for example, "HubMsgHubw2lu5yeop2qwy"|
    |Radio Button|Select Blob storage/ADLS Gen2 from your subscriptions|    |
    |Subscription Dropdown|{your subscription}|Select the name of your subscription in the dropdown|
    |Storage Account Dropdown|Select the storage account that begins with `stor`|For example, "storl1234fkjhgkg12gh"|
    |Container Radio Button and Dropdown|Select `Use Existing` radio button|Select the container name in the dropdown|
    |Authentication Mode Dropdown |Select `Connection String`|        |
    |Storage account key Secrets Text Box |Filled in by default|  |
    |Path Pattern Text Box| type in `messages` | This is the root folder in the hierarchy |
    |Date Format Text Box | Set to `YYYY/MM/DD` | |
    |Time Format Text Box | Set to `HH` | |
    |Minimum rows Text Box| Leave empty| |
    |Minimum Time| Leave empty| Hours, Minutes, Seconds|
1. Select the "Save" button. This action enables the stream analytics service to save messages to Blob storage.

## Next Steps

Congratulations, you've completed the basics of IoT Cloud development and have a solid understanding of Azure! You are ready for the next section on setting up your Raspberry Pi with an easy way to remotely code it.

[Tutorial: Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)
