---
title: Deploy and Configure StreamAnalytics
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Deploy and Configure StreamAnalytics

In this tutorial you'll...

- Create a new resource group
- Deploy a Stream Analytics Service into your new resource group
- Create a query to move messages to storage

**Azure Stream Analytics** is a fully managed service provided by Microsoft that enables users to analyze and process high volumes of streaming data in real-time. It can be used to build solutions that analyze data streams from devices, sensors, social media, applications, websites, and more. Some benefits of using Azure Stream Analytics include:

- *Real-time processing*. Stream Analytics enables users to analyze and process data as it is generated, in real-time. This allows organizations to react to events and make decisions quickly.
- *Scalability*. Stream Analytics is designed to handle high volumes of data with low latency. It can scale up or down as needed to meet the demands of the workload.
- *Integration with other Azure services*. Stream Analytics integrates with other Azure services such as Azure Functions, Azure Machine Learning, and Azure Storage, which allows users to build more sophisticated and powerful solutions.
- *Ease of use*. Stream Analytics has a simple, intuitive query language that enables users to analyze and process data streams without the need for complex programming. It also has a visual interface that allows users to build and monitor stream analytics jobs without writing code.
- *Cost-effective*. Stream Analytics is a fully managed service that charges users based on the number of events processed and the duration of the job. This means users only pay for what they use and can scale up or down as needed to meet the demands of their workload.

The following the diagram below details what you'll do in this tutorial:

1. Deploy a new resource group to contain your Stream Analytics Jobs
1. Deploy the Stream Analytics service into your new resource group
1. Send a message using the simulated device you created in the [Tutorial: Send a Message from a Simulated Device To the Cloud](tutorial-devicetocloudmsg.md)
1. Configure the input of your stream analytics job to and see the preview of your message
1. Configure the output of your stream anayltics job and start the job to send your message to storage.

![lnk_processedmessage]

## Prerequisites

Completed the [Tutorial: Send a Message from a Simulated Device To the Cloud](tutorial-devicetocloudmsg.md)

## Deploy

In this section you'll create a resource group and deploy a stream analytics service into it.

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
    PS > $templateFile = "C:\repos\IoT\arm\stream.json"
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

## Queue a Message



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

## Verify

In this section you'll use the building blocks from the previous tutorials to send a message from a simulated device to IoT Hub, view the contents of the incoming message in your Stream Analytics query, then run a Stream Analytics job to save the messages to storage.

## Next Steps

Congratulations, you've completed the basics of IoT Cloud development and have a solid understanding of Azure! You are ready for the next section on setting up your Raspberry Pi with an easy way to remotely code it.

[Tutorial: Connect and configure your Raspberry Pi with Visual Studio Code](tutorial-rasp-connect.md)

<!--images-->
[lnk_processedmessage]: media\tutorial-deploystreamtostorage\processedmessage.png