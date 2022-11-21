# Create Sample Data

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
    $projectName = "{new maps project name}"
    $rg = ($projectName + "RG")
    ```

    For example,

    ```powershell
    PS > $projectName = "Map"
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

    ResourceGroupName : MapRG
    Location          : centralus
    ProvisioningState : Succeeded
    Tags              : 
    ResourceId        : /subscriptions/d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda/resourceGroups/MessagingRG
    
    ```

1. Run the following script to set the path to the ARM template `ARMtemplate.json`

    ```powershell
    $templateFile = "{path to Map ARMtemplate.json}"
    ```

    For example,

    ```powershell
    PS > $templateFile = "C:\\repos\\various\\scripts\\ARMtemplate.json"
    ```