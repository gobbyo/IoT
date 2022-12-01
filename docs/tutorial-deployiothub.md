# Deploy an Azure IoT Hub

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
