# Deploy an Azure IoT Hub

IoT Hub is the simplest an most efficient way for devices to send and receive messages from the cloud. In this tutorial you'll create an IoT Hub and an associated storage account using an [Azure Resource Manager (ARM) template](https://learn.microsoft.com/azure/azure-resource-manager/templates/overview). Following the diagram below using the machine you configured in the previous tutorial:

1. Create an Azure Resource Group for your IoT Hub
1. Deploy IoT Hub and a Storage Account

![deploy_iothub]
*Figure of the main steps in this tutorial*

Using an ARM template rather than the [Azure portal user interface](https://portal.azure.com) has several benefits:

- **Consistency when creating or recreating your service setup** and all the configuration settings involved. There are dozens of service configuration settings, capturing your service settings in an ARM template avoids any unintended consequences that can occur by missing or mis-typing the wrong setting.
- **Saves time in having to go through all the user interface forms**. There are a lot of ways to get distracted from your original goal by having to learn about service settings that you may never need to understand nor use. Having a pre-configured ARM template avoids being overwhelmed with all the possibilities.
- **Automate the creation of your service setup**. You may in the future have a need to automate the deployment and setup of your services in Azure. ARM templates are designed to support the automated deployment of Azure services. Throughout our tutorials we use PowerShell on our own machine with ARM templates to deploy Azure services. That way you can easily transfer your scripts and setup code to any machine or environment.

No need to avoid using the [Azure portal user interfaces](https://portal.azure.com) entirely as it is a great way to visualize any Azure service and all its settings.

## Prerequisites

- [Configure your Windows Machine](tutorial-configure.md)

## Create an Azure Resource Group for your IoT Hub

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

Before starting this section, make sure your PowerShell variables are set in your PS session:
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

## Resources

Be sure to read more about the following code and concept references you used in this tutorial.

- [New-AzResourceGroup](https://learn.microsoft.com/powershell/module/az.resources/new-azresourcegroup?view=azps-9.2.0)
- [New-AzResourceGroupDeployment](https://learn.microsoft.com/powershell/module/az.resources/new-azresourcegroupdeployment?view=azps-9.2.0)
- [Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits)
- [Azure Resource Manager vs. classic deployment: Understand deployment models and the state of your resources](https://learn.microsoft.com/azure/azure-resource-manager/management/deployment-models)
- Manage Azure Resource Groups:
    - [Using the Azure Portal](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
    - [Using PowerShell](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-powershell)

## Explore more

You can optionally explore and learn more about deploying Azure services by doing the following:

1. Modify the ARM template to deploy IoT Hub
1. Create your own ARM template

## Next Steps

[Create a device for your IoT Hub](docs/tutorial-symmetrickeydevice.md)

<!-- images -->

[deploy_iothub]: media/tutorial-deployiothub/deployiothub.png