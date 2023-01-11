---
title: Connect and configure your Raspberry Pi with Visual Studio Code
description: [todo] 
author: jbeman@hotmail.com
---

# Tutorial: Connect and configure your Raspberry Pi with Visual Studio Code

In this tutorial you'll connect to your Raspberry pi with Visual Studio Code and write some python code.

## Prerequisites

- [Completed an install of an OS onto your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [Enabled SSH on your Raspberry PI](https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh)

## Set Up Remote SSH and Python Extension with Visual Studio Code

1. Follow the instructions to set up [Remote Access](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access) and [SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)

1. Follow the instructions to set up a [remote session in Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh).
1. Add the [VS Code python extension](https://code.visualstudio.com/docs/languages/python) while remotely connected to your Raspberry pi in VS Code. This extension allows you to debug your Python code while remotely connected in VS code.

## Add the GitHub Repository

1. [Install GitHub](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) from your VS Code SSH session.
1. Change to your home directory and create a "repos" directory as follows,

    ```azurecli
    cd ~
    mkdir repos
    ```

1. Change to the repos directory and clone your GitHub fork, `git clone https://github.com/{your-fork}/IoT.git`

    ```azurecli
    cd repos
    git clone https://github.com/{your-fork}/IoT.git
    ```

## Reference

- [Set up Remote Access on your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access)
- [Set up SSH on your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)
- [Configure remote SSH in Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh)
- [Install VS Code python extension](https://code.visualstudio.com/docs/languages/python)

## Next Steps

[Tutorial: Deploy and Configure a Device Provisioning Service (DPS)](tutorial-deploydps.md)
