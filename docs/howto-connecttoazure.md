# How to Use Your Azure Subscription

You'll need to authenticate your subscription to use any service in Azure. This guide provides you the basics and simplest way to authenticate to your subscription.

An **Azure tenant** represents a single organization. It is a dedicated instance of Azure Active Directory (Azure AD) that an organization receives and owns when it signs up for a Microsoft cloud service such as Azure. An Azure tenant is associated with a subscription, which represents a billing relationship between the tenant and Microsoft.

An **Azure subscription** is a logical container used to track the resources that an organization consumes. Subscriptions are associated with an Azure tenant and are used to manage access to Azure resources, enforce quotas and limits, and manage billing.

Each Azure tenant has at least one subscription, and an organization can have multiple subscriptions associated with a single tenant. Subscriptions can be used to isolate resources for different purposes, such as production and development, or to allocate resources to different departments within an organization.

In summary, an Azure tenant represents an organization and is associated with a subscription, which represents a billing relationship with Microsoft and is used to manage access to Azure resources.

When you create a free subscription, a default active directory tenant is automatically created for your account. If you have already been working with multiple subcriptions through school or work organization, then you'll need to log into the right tenant to find your subscription.

## Find and Authenticate Your Subscription

1. Find your tenant and subscription. Read the guide on how to [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/azure/azure-portal/get-subscription-tenant-id). The easiest way to find out which tenant you are using is to run the following PowerShell script on the machine you configured from the tutorial [Configure your Windows Machine](tutorial-configure.md):

    ```powershell
    Get-AzContext | format-list
    ```

    For example,

    ```powershell
    PS C:\repos\various> Get-AzContext | format-list
    
    Name               : Visual Studio Enterprise Subscription (3286xxxx-xxxx-xxxx-xxxx-xxxx72d746e1) - 
                         37f7xxxx-xxxx-xxxx-xxxx-xxxx46a89ca5 - <alias>@mail.com
    Account            : <alias>@mail.com
    Environment        : AzureCloud
    Subscription       : 3286xxxx-xxxx-xxxx-xxxx-xxxx72d746e1
    Tenant             : 37f7xxxx-xxxx-xxxx-xxxx-xxxx46a89ca5
    TokenCache         : 
    VersionProfile     : 
    ExtendedProperties : {}
    ```

2. Run the following script to authenticate your Azure subscription. Replace `{your subscription ID}` with the identifier to your Azure subscription.

    ```powershell
    Connect-AzAccount -SubscriptionId "{your subscription ID}"
    ```

    For example,

    ```powershell
    PS > Connect-AzAccount -SubscriptionId "d330xxxx-xxxx-xxxx-xxxx-xxxxxxxxabda"
    ```

## References

- [Get-AzContext](https://learn.microsoft.com/powershell/module/az.accounts/get-azcontext?view=azps-9.2.0)
- [Set-AzContext](https://learn.microsoft.com/powershell/module/az.accounts/set-azcontext?view=azps-9.2.0)
- [Connect-AzAccount](https://learn.microsoft.com/powershell/module/az.accounts/connect-azaccount?view=azps-9.2.0)
- [Manage Azure portal settings and preferences](https://learn.microsoft.com/azure/azure-portal/set-preferences)
- [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/azure/azure-portal/get-subscription-tenant-id)
- [Configure your Windows Machine](tutorial-configure.md)