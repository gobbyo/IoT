# Create A Virtual Machine

In this tutorial, you'll:

- Create a [Windows 10 Virtual Machine](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal)
- Install and use [Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) to connect to your VM

In this tutorial, you'll create a Windows virtual machine on the [Azure portal](http://portal.azure.com) to run and manage the cloud portion of the tutorials. You'll need to complete this tutorial if you do not have access to a Windows machine. If you're trying out these tutorials for the first time, then use a clean install of a virtual machine to avoid issues. Be aware there is cost involved in creating a Virtual Machine and using [Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview) to remotely access it. Otherwise, you can skip this tutorial and go directly to the [Tutorial: Configure your Windows Cloud Machine](tutorial-configure.md). Bastion is a remote access service in Azure that allows you to remotely connect to Windows virtual machines (VMs). There are several benefits to using Bastion to access your Windows VM over RDP:

- **Security**. Bastion is far more secure than using Remote Desktop or other mechanisms to remotely connect. Bastion uses Azure AD authentication and multi-factor authentication (MFA) to ensure that only authorized users can access the VM.
- **Convenience**. Bastion allows you to access your VM from any device with a modern web browser, without the need to install additional software or configure VPN connections.
- **Ease of use**. Bastion includes a user-friendly interface that makes it easy to connect to and manage your VMs.
- **Scalability**. Bastion can scale to support a large number of users and VMs, making it suitable for use in large organizations.
- **Integration with Azure**. Bastion is fully integrated with Azure, allowing you to manage your VMs and other resources from the same interface.

Overall, Bastion provides a secure and convenient way to remotely access Windows VMs over RDP, and can be especially useful for organizations looking to simplify their remote access infrastructure.

The following diagram provides you the context to create a Windows 10 cloud VM.
1. Create a Windows Cloud Virtual machine
1. Deploy Bastion and connect to your Windows Machine

![diagram of the VMs used for setting up the CVP environment]

## Prerequisites

- An Azure subscription, or use [free Azure subscription](https://azure.microsoft.com/en-us/free).
- Your account in your Azure Active Directory where your subscription resides, must have the *Application Developer Role*, for details see [steps for setting up your Azure Active Directory Role](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-users-assign-role-azure-portal?context=%2Fazure%2Factive-directory%2Froles%2Fcontext%2Fugr-context)

## Create a Windows 10 cloud VM

1. Open the [Azure portal](http://portal.azure.com) and select your subscription.
1. [Create a resource group](https://docs.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal#create-resource-groups) for your VM
1. From the [Azure portal](http://portal.azure.com), open your resource group and select the **Create** button.

1. Search for the **Microsoft Windows 10** image. Pick the first one that shows up in the list as the specific Windows 10 image to use will be detailed later in this tutorial.

    ![find resource in Azure portal]

1. Select Windows 10 Pro 1️⃣ then select the **Create** button 2️⃣.

    ![creating the Windows 10 resource in the Azure portal]

1. In the Create a virtual machine form as diagrammed below, fill in the form as suggested in each table: project details, instance details, administrator account, and inbound port rules. Once the form is complete, select the "Review + create" button.

    ![configuring a Windows 10 resource in the Azure portal]

    **Project details**

    |Form Item  |Action  |
    |---------|---------|
    |Subscription     | Select your subscription name from the dropdown        |
    |Resource group     | Select the resource group you created in the previous step.        |

    **Instance details**

    |Form Item  |Action  |
    |---------|---------|
    |Virtual Machine Name     | Name your VM, for example, myVM |
    |Region     | Select a region that supports the Standard D4s_v3 size, for example, West US 2 |
    |Availability Options     | No infrastructure redundancy required  |
    |Security Type     | Standard        |
    |Image     | Use the default image, for example, Windows 10 Pro, version xxxx|
    |Azure spot instance     | Select the box |
    |Size     |Standard D4s_v3  |

    **Administrator account**

    |Form Item  |Action  |
    |---------|---------|
    |Username     | Provide a user name |
    |Password     | A password between 12 and 123 characters        |
    |Confirm password     | Confirm your previous password |

    **Inbound port rules**

    |Form Item  |Action  |
    |---------|---------|
    |Public inbound ports     | Allows selected ports (default) |
    |Select inbound ports     | RDP (3389, default) |

    **Licensing**

    Select the box "I confirm ..."

1. Create the VM then select the **Go to resource** button when the deployment is complete.
1. Follow the instructions to [Deploy Bastion](https://docs.microsoft.com/en-us/azure/bastion/quickstart-host-portal) from your VM.
1. [Connect to your VM](https://docs.microsoft.com/en-us/azure/bastion/quickstart-host-portal#createvmset) using Bastion.
1. Once you've successfully connected to your VM using Bastion, be sure to [remove its public IP address](https://docs.microsoft.com/azure/bastion/quickstart-host-portal#remove). ⚠️ Missing this step will leave your VM open to security vulnerabilities.
1. Be sure to reset your password to avoid connectivity issues the next time you sign in. Select **Help->Reset password** found in the VM's left pane of the [Azure portal](http://portal.azure.com). ⚠️ Missing this step will prevent Bastion from connecting to your VM.

    ![password reset]

## Next Steps

[Tutorial: Configure your Windows Machine](tutorial-configure.md)

<!-- link -->

[lnk_ps_session]: https://docs.microsoft.com/visualstudio/ide/reference/command-prompt-powershell?view=vs-2022#developer-powershell
[lnk_vm_creation]: https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal
[lnk_azure_portal]: http://portal.azure.com
[lnk_git]: https://git-scm.com/download/win
[lnk_dotnet]: https://dotnet.microsoft.com/en-us/download/dotnet/sdk-for-vs-code?utm_source=vs-code&amp;utm_medium=referral&amp;utm_campaign=sdk-install
[lnk_visualstudio]: https://code.visualstudio.com/Download
[lnk_csharp_vscode]: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp
[lnk_ps_vscode]: https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell
[lnk_deploy_bastion]: https://docs.microsoft.com/en-us/azure/bastion/quickstart-host-portal
[lnk_connect_your_VM]: https://docs.microsoft.com/en-us/azure/bastion/quickstart-host-portal#createvmset
[lnk_remove_publicIP_address]: https://docs.microsoft.com/azure/bastion/quickstart-host-portal#remove


<!-- images -->

[diagram of the VMs used for setting up the CVP environment]: media/tutorial-prerequisites/installprereq.png
[configuring a resource group in the Azure portal]: media/tutorial-prerequisites/resourcegroupform.png
[adding a resource to a resource group in the Azure portal]: media/tutorial-prerequisites/addresource.png
[find resource in Azure portal]: media/tutorial-prerequisites/newwin10.png
[creating the Windows 10 resource in the Azure portal]: media/tutorial-prerequisites/createvm.png
[configuring a Windows 10 resource in the Azure portal]: media/tutorial-prerequisites/win10form_1.png
[deploying the Windows 10 VM in the Azure portal]: media/tutorial-prerequisites/win10deploymentcomplete.png
[deploy bastion]: media/tutorial-prerequisites/deploybastion.png
[bastion]: media/tutorial-prerequisites/bastion.png
[password reset]: media/tutorial-prerequisites/passwordreset.png
