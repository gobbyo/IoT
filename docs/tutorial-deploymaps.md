# Deploy a Maps Service

Before starting this section be sure to open Visual Studio (VS) Code, select the `Terminal > New Terminal...` menu and [Authenticate your Azure Subscription](howto-connecttoazure.md) using the PowerShell (PS) session.

1. Run the following script to set a new resource group name to the `$rg` powershell variable. Replace `{new resource group name}` with the new name of your resource group.

    ```powershell
    $rg = "{resource group name}"
    ```

    For example,

    ```powershell
    PS > $rg = "myMapRG"
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

    ResourceGroupName : myMapRG
    Location          : centralus
    ProvisioningState : Succeeded
    Tags              : 
    ResourceId        : /subscriptions/d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda/resourceGroups/MessagingRG
    
    ```

1. Deploy the Map ARM template

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile "C:\repos\IoT\arm\map.json"
    ```

    For example,

    ```powershell
    New-AzResourceGroupDeployment `
    -ResourceGroupName $rg `
    -TemplateFile $templateFile

    DeploymentName          : mapARMtemplate
    ResourceGroupName       : myMapRG
    ProvisioningState       : Succeeded
    Timestamp               : 11/21/2022 7:39:29 PM
    Mode                    : Incremental
    TemplateLink            : 
    Parameters              : 
                              Name             Type                       Value
                              ===============  =========================  ==========
                              accountName      String                     "xxxxxxxxxx"
                              pricingTier      String                     "S0"
                              kind             String                     "Gen1"
    
    Outputs                 : 
    DeploymentDebugLogLevel : 
    ```
