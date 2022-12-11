## Configure your Windows Machine

This tutorial must be completed before any other tutorials: you'll install Visual Studio Code, a few extensions, and Git for windows. Finally, you'll install Python, Azure Maps and Identity Python client libraries.

### Install Visual Studio Code and Extensions

1. Install [Visual Studio Code](https://code.visualstudio.com/Download) for Windows. Allow Visual Studio Code to launch.
1. Within Visual Studio Code, open a [PowerShell terminal session][lnk_ps_session] in administrative mode and run the following commands:

    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
    
    Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy Unrestricted -Force
    ```

1. Run the following commands from your PowerShell terminal session:

    ```azurepowershell
    Install-Module Az.Accounts
    ```

    For each module, reply **Y** or **A** when asked either question below:
    - `Do you want PowerShellGet to install and import the NuGet provider now?` Type **Y**.
    - `Are you sure you want to install the modules from the 'MSGallery'?` Type **A**.

### Install Git for Windows

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

1. Run the following script from your terminal session in Visual Studio Code:

    ```powershell
    git clone https://github.com/gobbyo/various.git
    ```

    for example,

    ```powershell
    PS C:\repos> git clone https://github.com/gobbyo/various.git
    Cloning into 'various'...
    remote: Enumerating objects: 250, done.
    remote: Counting objects: 100% (250/250), done.
    remote: Compressing objects: 100% (160/160), done.
    Receiving objects: 100% (250/250), 5.95 MiB | 20.18 MiB/s, done.
    Resolving deltas: 100% (105/105), done.13 (delta 72), pack-reused 0
    ```

1. Select `File > Open Folder...` from the menu in Visual Studio Code and select the cloned directory `various`.

### Install Python

1. From a browser open [install python](https://www.python.org/downloads/). Be sure to check the box `Use admin privileges when installing py.exe` and  `Add python.exe to PATH` at the start of the install, then select `Install Now`.  At the end of the install select the `Disable path length limit`, then select the `close` button.
1. Install the Visual Studio Code [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. From Visual Studio Code, select the `View > Command Pallette..` menu, type the following in the command pallette text box:

    |#  |Item  | Comment   |
    |:--------|:---------|:---------|
    |1     | `Python: Create Environment` | Creates a Python virtual environment  |
    |2     | `Venv` to create a virtual environment | See [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html) |
    |3     |  Select the recommended Python interpreter | There may be multiple interpreters if you are installing on your own machine and have used Python in the past |

### Install Azure Client Libraries

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

1. Install the [Azure IoT device client package](https://pypi.org/project/azure-iot-device/) by running the following python script in your terminal session:

    ```powershell
    pip install python-decouple
    ```

### Test Your Python Installation

1. From your Visual Studio Code terminal session, change the GitHub cloned directory from `various` to `python` directory. Type `python` and hit the return key.

    ```powershell
    PS C:\repos\various> cd python
    PS C:\repos\various\python> python
    ```

    For example,

    ```powershell
    PS C:\repos\various> cd python
    (.venv) PS C:\repos\various\python> python
    Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

1. The following python scripts, run the `createRouteList` in the `maproute` module, and hit the enter key.

    ```python
    from maproute import createRouteList
    listOfLatLon=[]
    listOfLatLon.append('48.5015559212639, -122.6753872337671')
    listOfLatLon.append('48.42566904524409, -122.60848502024562')
    createRouteList(listOfLatLon)
    ```

    For example,

    ```python
    >>> from maproute import createRouteList
    >>> listOfLatLon=[]
    >>> listOfLatLon.append('48.5015559212639, -122.6753872337671')
    >>> listOfLatLon.append('48.42566904524409, -122.60848502024562')       
    >>> createRouteList(listOfLatLon)
    [LatLon(lat='48.5015559212639', lon='-122.6753872337671'), LatLon(lat='48.42566904524409', lon='-122.60848502024562')]
    >>>
    ```

1. Type `exit()` to exit the python script environment. For example,

    ```python
    >>> exit()
    (.venv) PS C:\repos\various\python>
    ```


## Next Steps

[todo]
