---
title: Deploy an Azure IoT Hub
description: Deploy an Azure IoT Hub using an ARM template 
author: jbeman@hotmail.com
---

# Tutorial: Deploy an Azure IoT Hub

In this tutorial, you learn how to:

- Deploy an Azure Resource Group using PowerShell
- Deploy an Azure IoT Hub using an ARM template
- Deploy an Azure Storage Account using an ARM template

In this tutorial you'll create an IoT Hub and an associated storage account using an [Azure Resource Manager (ARM) template](https://learn.microsoft.com/azure/azure-resource-manager/templates/overview). Following the diagram below using the machine you configured in the previous tutorial:

1. Create an Azure Resource Group for your IoT Hub
1. Deploy IoT Hub and a Storage Account

![lnk_deployiothub]

All tutorials involving deploying or creating an Azure service focus on using an ARM (Azure Resource Manager) template rather than the [Azure portal user interface](https://portal.azure.com). An ARM template is a JSON file that defines the infrastructure and configuration for an Azure solution. There are several benefits to using an ARM template to deploy services:

- **Reusability**. ARM templates can be used to deploy resources consistently and repeatably, which can be especially useful when deploying the same resources to multiple environments (e.g., development, staging, production).
- **Version control**. ARM templates can be stored in a version control system, such as Git, which allows you to track changes to the infrastructure over time and roll back to previous versions if needed.
- **Collaboration**. ARM templates can be shared and collaborated on by multiple team members, which can be useful when working on complex projects with multiple dependencies.
- **Automation**. ARM templates can be used to automate the deployment of resources, which can save time and reduce the risk of errors.
- **Consistency**. ARM templates can help ensure that resources are deployed consistently across environments, which can be especially important for maintaining compliance with corporate standards or regulatory requirements.

No need to avoid using the [Azure portal user interfaces](https://portal.azure.com) entirely as it is a great way to visualize any Azure service and all its settings.

## Prerequisites

- Completed the [Tutorial: Configure your Windows Cloud Machine](tutorial-configure.md)

## Create an Azure Resource Group for your IoT Hub

In this section you'll create a resource group for your IoT Hub and Storage Account. A resource group is a logical container in Azure that holds related resources for an Azure solution. There are several benefits to creating a resource group for your Azure services:

- **Organization**. Resource groups can help you organize your Azure resources in a logical and meaningful way, which can make it easier to manage and understand your Azure infrastructure.
- **Cost management**. Resource groups can be used to manage costs associated with your Azure resources. For example, you can use a resource group to monitor and track the costs of your resources, and apply tags to your resources to help you better understand how your costs are being incurred.
- **Resource management**. Resource groups provide a convenient way to manage the lifecycle of your Azure resources. For example, you can use a resource group to deploy, update, and delete resources as a group, rather than managing them individually.
- **Access control**. Resource groups can be used to control access to your Azure resources. For example, you can use resource policies or role-based access control to grant or restrict access to specific resource groups or resources within them.

Before starting this section be sure to open Visual Studio (VS) Code, select the `Terminal > New Terminal...` menu and [Authenticate your Azure Subscription](howto-connecttoazure.md) using the PowerShell (PS) session.

1. From your VS code PS terminal session, run the following script to set a new resource group name to the `$rg` powershell variable. Replace `{new resource group name}` with the new name of your resource group.

    ```powershell
    $projectName = "{new hub project name}"
    $rg = ($projectName + "RG")
    ```

    For example,

    ```powershell
    PS > $projectName = "HubMsg"
    PS > $rg = ($projectName + "RG")
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

    ResourceGroupName : myMessagingRG
    Location          : centralus
    ProvisioningState : Succeeded
    Tags              : 
    ResourceId        : /subscriptions/d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda/resourceGroups/myMessagingRG
    
    ```

## Deploy IoT Hub and a Storage Account

In this section you'll deploy an Azure IoT Hub and a Storage Account. Azure IoT Hub is a cloud-based service that enables secure and reliable communication between IoT devices and the cloud. It provides a range of features that make it well-suited for use in IoT applications, including:

- **Device management**. IoT Hub enables you to manage and monitor your IoT devices, including provisioning, updating, and de-provisioning devices.
- **Secure communication**. IoT Hub provides secure communication between devices and the cloud using industry-standard protocols, such as MQTT and HTTPS.
- **Scalability**. IoT Hub is designed to handle large volumes of device data and traffic, making it suitable for use in large-scale IoT deployments.
- **Integration with Azure services**. IoT Hub can be easily integrated with other Azure services, such as Azure Stream Analytics, Azure Functions, and Azure Machine Learning, which can be useful for building more complex IoT solutions.
- **Customizable routing**. IoT Hub allows you to configure custom routes to send device data to different endpoints, such as storage or event hubs.

Before starting, verify your PowerShell variables are set in your PS session:
- `$rg`
- `$projectName`
- `$location`

For example,

```powershell
PS> $location
Central US
```

1. Run the following script to set the path to the ARM template `hub.json`

    ```powershell
    $templateFile = "{path to hub.json}"
    ```

    For example,

    ```powershell
    PS > $templateFile = "C:\\repos\\various\\arm\\hub.json"
    ```

1. Deploy the hub ARM template

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile $templateFile `
    -projectName $projectName `
    -location $location
    ```

    For example,

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile $templateFile `
    -projectName $projectName `
    -location $location
    ```

1. Check the status of your deployment by opening the [Azure Portal](https://portal.azure.com) and following the diagram below. 1️⃣ Open the resource group you created earlier in this tutorial. 2️⃣ Select **Settings > Deployments** in the left pane, then 3️⃣ select your hyperlinked deployment name.

    ![lnk_checkdeployment]

## Resources

Be sure to read more about the following code and concept references you used in this tutorial.

- [New-AzResourceGroup](https://learn.microsoft.com/powershell/module/az.resources/new-azresourcegroup?view=azps-9.2.0)
- [New-AzResourceGroupDeployment](https://learn.microsoft.com/powershell/module/az.resources/new-azresourcegroupdeployment?view=azps-9.2.0)
- [Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits)
- [Azure Resource Manager vs. classic deployment: Understand deployment models and the state of your resources](https://learn.microsoft.com/azure/azure-resource-manager/management/deployment-models)
- Manage Azure Resource Groups:
    - [Using the Azure Portal](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
    - [Using PowerShell](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-powershell)

## Explore More

You can optionally explore and learn more about deploying Azure services by doing the following:

1. Modify the ARM template to deploy IoT Hub
1. Create your own ARM template

## Next Steps

[Tutorial: Create a Simulated Device](tutorial-symmetrickeydevice.md)

<!-- images -->
[lnk_deployiothub]: media/tutorial-deployiothub/deployiothub.png
[lnk_checkdeployment]: media/tutorial-deployiothub/checkdeployment.png