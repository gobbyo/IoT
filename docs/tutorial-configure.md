---
title: Configure your Windows Cloud Machine
description: Install Visual Studio Code, a few extensions, and Git for windows, Python, Azure Maps and Identity Python client libraries 
author: jbeman@hotmail.com
---

# Tutorial: Configure your Windows Cloud Machine

You'll need a cloud developer set up in order to deploy Azure services and remotely code your device. This tutorial must be completed before any other tutorials: you'll install Visual Studio Code, a few extensions, and Git for windows. Finally, you'll install Python, Azure Maps and Identity Python client libraries.

## Install Visual Studio Code and Extensions

1. Install [Visual Studio Code](https://code.visualstudio.com/Download) for Windows. Allow Visual Studio Code to launch.

1. From Visual Studio Code type **ctrl-shift-x** and install the following using the textbox to `Search Extensions in Marketplace`:

- `Remote Explorer`, published by Microsoft
- `Python`, published by Microsoft

1. Within Visual Studio Code, open a [PowerShell terminal session](https://learn.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell?view=vs-2022) in administrative mode and run the following commands:

    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
    
    Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy Unrestricted -Force
    ```

1. Run the following commands from your PowerShell terminal session:

    ```azurepowershell
    Install-Module Az.Accounts
    Install-Module Az.DeviceProvisioningServices
    ```

    For each module, reply **Y** or **A** when asked either question below:
    - `Do you want PowerShellGet to install and import the NuGet provider now?` Type **Y**.
    - `Are you sure you want to install the modules from the 'MSGallery'?` Type **A**.

## Install Git for Windows

1. Open a browser session in your Windows 10 machine and download the [git for windows](https://git-scm.com/download/win) installer.
1. Run the installer, accepting the default settings. When you arrive at the screen **Choosing the default editor used by Git**, choose **Use Visual Studio Code as Git's default editor** from the dropdown selection, then continue accepting the default settings until finished.
1. Close and open Visual Studio Code.
1. Open Visual Studio Code. Select `Terminal > New Terminal` from the menu.
1. Create a directory for cloned sample code and change to your new directory,

    ```powershell
    mkdir c:\repos
    cd c:\repos
    ```

    For example,

    ```powershell
    PS C:\> mkdir c:\repos
    PS C:\> cd c:\repos
    PS C:\repos>
    ```

1. [Fork the repo](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/#:~:text=How%20to%20Fork%20a%20Repo%20in%20GitHub%20Forking,forked%20repository%20gets%20created%20under%20your%20GitHub%20account.) from [https://github.com/gobbyo](https://github.com/gobbyo).
1. Run the following script from your terminal session in Visual Studio Code:

    ```powershell
    git clone https://github.com/{your-fork}/various.git
    ```

    For example,

    ```powershell
    PS > git clone https://github.com/{your-fork}/various.git
    Cloning into 'various'...
    remote: Enumerating objects: 250, done.
    remote: Counting objects: 100% (250/250), done.
    remote: Compressing objects: 100% (160/160), done.
    Receiving objects: 100% (250/250), 5.95 MiB | 20.18 MiB/s, done.
    Resolving deltas: 100% (105/105), done.13 (delta 72), pack-reused 0
    ```

1. Select `File > Open Folder...` from the menu in Visual Studio Code and select the cloned directory `various`.

## Install Python

1. From a browser open [install python](https://www.python.org/downloads/). Be sure to check the box `Use admin privileges when installing py.exe` and  `Add python.exe to PATH` at the start of the install, then select `Install Now`.  At the end of the install select the `Disable path length limit`, then select the `close` button.
1. From Visual Studio Code, select the `View > Command Pallette..` menu, type the following in the command pallette text box:

    |#  |Item  | Comment   |
    |:--------|:---------|:---------|
    |1     | `Python: Create Environment` | Creates a Python virtual environment  |
    |2     | `venv` to create a virtual environment | See [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html) |
    |3     |  Select the recommended Python interpreter | There may be multiple interpreters if you are installing on your own machine and have used Python in the past |

## Install Azure Client Libraries

1. From Visual Studio Code, select the `Terminal > New Terminal...` menu. In the powershell terminal session you should see the following,

    ```powershell
    Windows PowerShell
    Copyright (C) Microsoft Corporation. All rights reserved.
    
    Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows        
    
    PS C:\repos\various> & c:/repos/various/.venv/Scripts/Activate.ps1
    (.venv) PS C:\repos\various>
    ```

1. Install the [Azure IoT device client package](https://pypi.org/project/azure-iot-device/) by running the following python script in your terminal session:

    ```powershell
    pip install azure-iot-device
    ```

1. Install the [Azure Identity client library](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python) by running the following python script in your terminal session:

    ```python
    pip install azure-identity
    ```

1. Install the [Python Decouple](https://pypi.org/project/python-decouple/) by running the following python script in your terminal session:

    ```python
    pip install azure-maps-route
    ```

## Test Your Python Installation

1. From your Visual Studio Code terminal session, change the GitHub forked clone directory from `various` to `python` directory. Type `python` and hit the return key.

    ```powershell
    PS C:\repos\various> python
    ```

    For example,

    ```powershell
    PS C:\repos\various> cd python
    (.venv) PS C:\repos\various> python
    Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

1. Verify your python terminal session

    ```python
    print("Hello World!")
    ```

    For example,

    ```python
    >>> print("Hello World")
    >>> Hello World
    >>>
    ```

1. Type `exit()` to exit the python script environment. For example,

    ```python
    >>> exit()
    (.venv) PS C:\repos\various\python>
    ```

## Resources

Be sure to read more about the following code and concept references you used in this tutorial.

- [Set-ExecutionPolicy](https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.3)
- [Install-Module](https://learn.microsoft.com/powershell/module/powershellget/install-module?view=powershell-7.3)
- [Git Clone](https://github.com/git-guides/git-clone)
- [Download Visual Studio Code](https://code.visualstudio.com/Download)
- [Visual Studio Developer Command Prompt and Developer PowerShell](https://learn.microsoft.com/visualstudio/ide/reference/command-prompt-powershell?view=vs-2022)

## Next Steps

[Tutorial: Deploy an Azure IoT Hub](tutorial-deployiothub.md)