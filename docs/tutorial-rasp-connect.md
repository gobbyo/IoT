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

## Set Up Remote SSH with Visual Studio Code

1. Follow the instructions to set up [Remote Access](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access) and [SSH](https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server)

1. Follow the instructions to set up a [remote session in Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh).

## Add the GitHub Repository

1. From your terminal session in Visual Studio Code, change to the home directory and create a "repos" directory as follows,

    ```azurecli
    cd ~
    mkdir repos
    ```

1. Change to the repos directory and clone your github fork, `git clone https://github.com/{your-fork}/various.git`

    ```azurecli
    cd repos
    git clone https://github.com/{your-fork}/various.git
    ```

## Reference

- IoT Hub message [system and user-defined properties](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-construct#system-properties-of-d2c-iot-hub-messages)

## Next Steps

[Tutorial: Deploy and Configure a Device Provisioning Service (DPS)](tutorial-deploydps.md)
