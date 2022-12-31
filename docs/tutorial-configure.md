---
title: Configure your Windows Cloud Machine
description: Install Visual Studio Code, a few extensions, and Git for windows, Python, Azure Maps and Identity Python client libraries 
author: jbeman@hotmail.com
---

# Tutorial: Configure your Windows Cloud Machine

In this tutorial, you'll do the following:

- Install Visual Studio Code and Extensions
- Install Git for Windows
- Install Python
- Install Azure Client Libraries

You'll need a Raspberry Pi and Cloud developer set up in order to easily deploy Azure services and remotely code your device. This tutorial must be completed before any other tutorials.

## Prerequisites

- Your own Windows machine or having completed the tutorial to [Configure your Windows Machine](tutorial-configure.md)

## Install Visual Studio Code and Extensions

In this section you'll install Visual Studio (VS) Code and a few extensions. There are several benefits to using VS Code for developing applications for the Raspberry Pi and your Cloud applications:

- **Remote development**. VS Code includes support for remote development, which allows you to develop applications on your local machine while remotely connected to your Raspberry Pi. This can be especially useful if you don't have access to a Raspberry Pi all the time, as you can still develop and test your applications remotely.
- **Debugging**. VS Code includes a powerful debugger that allows you to set breakpoints, step through code, and inspect variables. This can be especially useful when developing applications for Raspberry Pi, as it can help you identify and fix issues more quickly.
- **IntelliSense**. VS Code includes a feature called IntelliSense, which provides intelligent code completion and snippets. This can help speed up the development process by providing suggestions for code completion as you type.
- **Extensibility**. VS Code is highly extensible, with a wide range of extensions available that can add additional functionality to the editor. You'll be adding several extensions to your VS Code environment. Extensions are useful when developing applications because they are tailored for the platform.
- **Code formatting**. VS Code includes support for code formatting, which can help you keep your code organized and easy to read. This can be especially useful when working on large projects or when collaborating with other developers.

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

In this section you'll [install GitHub](https://git-scm.com/download/win) and [fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo), https://github.com/gobbyo, for your tutorial projects. Forking code refers to the process of creating a copy of an existing codebase and making changes to it. There are several benefits to forking code:

- **Customization**. By forking code, you can customize the sample code. For example, in several tutorials there are "Explore More" sections where you explore making changes to add new features or modify the existing features.
- **Collaboration**. Code works differently across operating systems like Windows and your Raspberry Pi. Forking code facilitates collaborating between your Cloud Machine and your Raspberry Pi while working on the same project. For example, while on the Raspberry Pi, you might fork a project and make changes to the message listener on your device, while on your Windows Cloud machines you'll make changes to the way the message is being sent. The changes can then be merged back into the main codebase.
- **Experimentation**. Forking code allows you to experiment with different approaches or solutions to a problem, without affecting the main codebase. This can be especially useful for testing new ideas.
- **Community involvement**. By forking code, you can contribute to this open-source project and become more involved in the community. For example, you can submit a pull request to have your changes merged into the main codebase should you find an error in the code or documentation.
- **Learning**. Forking code can be a great way for you to learn about IoT and approaches to solving problems. By working on a codebase and making changes, you can gain valuable experience and improve your skills.

1. Open a browser session in your Windows machine and download the [git for windows](https://git-scm.com/download/win) installer.
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

1. [Fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) from [https://github.com/gobbyo](https://github.com/gobbyo).
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

In this section you'll install Python into your Windows Cloud Machine. You'll use your Windows Cloud Machine to develop and code applications for your Raspberry Pi. There are several benefits to using Python to code for the Raspberry Pi:

- **Ease of use**. Python is known for being easy to read and write, which can make it an ideal choice for beginners or for projects where simplicity is a priority.
- **Wide range of libraries**. Python has a large and active community, which has developed a wide range of libraries for various purposes. These libraries can be easily imported and used in Python programs, which can save time and effort when developing applications for the Raspberry Pi.
- **Extensive documentation**. Python has extensive documentation, including tutorials and examples, which can be helpful for learning the language and for developing applications for the Raspberry Pi.
- **Compatibility with Raspberry Pi hardware**. Python is well-suited for interacting with the hardware on the Raspberry Pi, including the GPIO pins and sensors. There are also a number of libraries available that make it easy to control the hardware on the Raspberry Pi using Python.
- **Community support**. There is a large and active community of Python developers, which can be a useful resource for getting help or finding solutions to problems when developing applications for the Raspberry Pi.

1. From a browser open [install python](https://www.python.org/downloads/). Be sure to check the box `Use admin privileges when installing py.exe` and  `Add python.exe to PATH` at the start of the install, then select `Install Now`.  At the end of the install select the `Disable path length limit`, then select the `close` button.
1. From Visual Studio Code, select the `View > Command Pallette..` menu, type the following in the command pallette text box:

    |#  |Item  | Comment   |
    |:--------|:---------|:---------|
    |1     | `Python: Create Environment` | Creates a Python virtual environment  |
    |2     | `venv` to create a virtual environment | See [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html) |
    |3     |  Select the recommended Python interpreter | There may be multiple interpreters if you are installing on your own machine and have used Python in the past |

## Install Azure Client Libraries

In this section you'll install the Azure Client Libraries. Azure client libraries are needed to create IoT applications because they provide a set of APIs (Application Programming Interfaces) that allow you to interact with the Azure IoT services. These libraries make it easy to integrate Azure IoT functionality into an application, such as sending data to the cloud, receiving commands from the cloud, and authenticating devices. Some of the benefits of using Azure client libraries to create IoT applications include:

- **Simplicity**. Azure client libraries provide a simple and easy-to-use interface for interacting with Azure IoT services, which can save time and effort when developing IoT applications.
- **Consistency**. Azure client libraries are designed to be consistent across different platforms and languages, which can make it easier to develop IoT applications that run on multiple platforms or that use different programming languages.
- **Reliability**. Azure client libraries are regularly updated and tested, which can help ensure that they are reliable and robust when used in IoT applications.
- **Security**. Azure client libraries include support for secure communication between devices and the cloud, which is important for ensuring the security of IoT applications.

Overall, Azure client libraries are an essential tool for developers who want to create IoT applications using Azure IoT services, as they provide a convenient and reliable way to interact with these services and take advantage of their capabilities.

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
- [Visual Studio Developer Command Prompt and Developer PowerShell](https://learn.microsoft.com/visualstudio/ide/reference/command-prompt-powershell?view=vs-2022)

## Next Steps

[Tutorial: Deploy an Azure IoT Hub](tutorial-deployiothub.md)
