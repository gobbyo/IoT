## Configure your Windows Machine

In this section you'll install Visual Studio Code, a few extensions, and Git for windows. Finally, you'll install Python, Azure Maps and Identity Python client libraries. Upon completion, you'll need to reboot your machine before starting the next tutorial.

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
1. Open Visual Studio Code. Select `Terminal > New Terminal` from the menu.
1. Create a directory for cloned sample code and change to your new directory,

    ```powershell
    mkdir repos
    cd repos
    ```

    For example,

    ```powershell
    PS C:\> mkdir repos
    PS C:\> cd repos
    PS C:\repos>
    ```

1. Run the following script from your terminal session in Visual Studio Code:

    ```powershell
    git clone https://github.com/gobbyo/various.git
    ```

    for example,

    ```powershell
    PS C:\repos> git clone https://github.com/gobbyo/various.git
    ```

1. Select `File > Open Folder...` from the menu in Visual Studio Code and select the cloned directory `various`.

### Install Python

1. From a browser open [install python](https://code.visualstudio.com/docs/languages/python#_install-python-and-the-python-extension). Follow the Visual Studio Code tutorial to [install python](https://code.visualstudio.com/docs/languages/python#_install-python-and-the-python-extension). Be sure to check the box `Add python.exe to PATH` at the start of the install.  At the end of the install be sure to select the `disable the maximum allowable path length`. Stop at the section [Run Python Code](https://code.visualstudio.com/docs/languages/python#_run-python-code) until you have finished the next two steps to install the Azure client libraries.
1. [Install the Visual Studio Code python extension](https://code.visualstudio.com/docs/languages/python#_install-python-and-the-python-extension)
1. Install the [Azure Maps Route Package client library](https://learn.microsoft.com/en-us/python/api/overview/azure/maps-route-readme?view=azure-python-preview)

    ```python
    pip install azure-maps-route
    ```

1. Install the [Azure Identity client library](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python). For example,

    ```python
    pip install azure-identity
    ```

1. Close Visual Studio Code.

### Test Your Python Installation

1. Open a command prompt, change the directory to the GitHub `various` repo, type `code .`, then hit the enter key. Note the `code .` command automatically starts Visual Studio Code and prepares the Python interpreter, see selecting the [Python Interpreter](https://code.visualstudio.com/docs/languages/python#_run-python-code).

    ```azurecli
    C:\repos>cd various
    C:\repos\various>code .
    ```

    Example command window,

    ```azurecli
    C:\repos>cd various
    C:\repos\various>code .
    ```

    Example terminal session in Visual Studio Code,

    ```python
    PS C:\repos\various> & c:/repos/various/.venv/Scripts/Activate.ps1
    (.venv) PS C:\repos\various> cd python
    (.venv) PS C:\repos\various\python>
    ```

1. From the `\various\python` directory, type `python` and hit the return key.

    ```powershell
    (.venv) PS C:\repos\various\python> python
    ```

    For example,

    ```python
    (.venv) PS C:\repos\various\python> python
    Python 3.xx.xx (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32       
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

1. The following python scripts, run the `createRouteList` in the `maproute` module.

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

1. Restart your machine

## Next Steps

[todo]
