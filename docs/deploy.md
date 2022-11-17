# Deploy a Messaging Hub

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
    $rg = "{new resource group name}"
    ```

    For example,

    ```powershell
    PS > $rg = "myMessagingRG"
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
    ResourceId        : /subscriptions/d330e131-4ea5-49ab-aa0e-238d8ad1abda/resourceGroups/myMessagingRG
    
    ```

1. Run the following script to set the path to the ARM template `hubstorageARM.json`

    ```powershell
    $templateFile = "{path to hubstorageARM.json}"
    ```

    For example,

    ```powershell
    PS > $templateFile = "C:\\repos\\various\\data\\hubstorageARM.json"
    ```

1. Deploy the ARM template

    ```powershell
    New-AzResourceGroupDeployment `
        -ResourceGroupName $rg `
        -TemplateFile $templateFile `
        -Location $location
    ```

    For example,

    ```powershell
    PS > New-AzResourceGroupDeployment `
        -ResourceGroupName $rg `
        -TemplateFile $templateFile `
        -Location $location

    TemplateLink            : 
    Parameters              : 
                              Name             Type                       Value
                              ===============  =========================  ==========
                              projectName      String                     "myMessaging"
                              location         String                     "Central US"                          skuName          String                     "S1"
                              skuUnits         Int                        1
                              d2cPartitions    Int                        4
    
    Outputs                 : 
    DeploymentDebugLogLevel :
    ```
