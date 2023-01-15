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

## Set up speed test

1. run the following

```azurecli
sudo apt install apt-transport-https gnupg1 dirmngr lsb-release
```

2. run the following curl command.

```azurecli
curl -L https://packagecloud.io/ookla/speedtest-cli/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/speedtestcli-archive-keyring.gpg >/dev/null
```

1. run the following script

```azurecli
echo "deb [signed-by=/usr/share/keyrings/speedtestcli-archive-keyring.gpg] https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
```

1. Update

```azurecli
sudo apt update
```

1. Install speedtest

```azurecli
sudo apt install speedtest
```

1. run it.

```azurecli
sudo apt install speedtest
```

## Reference

- [Set up Remote Access on your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access)
- [Set up SSH on your Raspberry Pi](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)
- [Configure remote SSH in Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh)
- [Install VS Code python extension](https://code.visualstudio.com/docs/languages/python)

## Next Steps

[Tutorial: Deploy and Configure a Device Provisioning Service (DPS)](tutorial-deploydps.md)
