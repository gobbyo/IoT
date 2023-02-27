# Tutorial: Send Hostname and IP address to the Cloud when Booting Up your Raspberry Pi

In this tutorial you'll create device code that sends a message to IoT Hub when booting up. Knowing your Raspberry Pi's hostname and IP address is helpful information needed to connect via ssh or from Visual Studio Code.

## Prerequisites

[Deploy and Configure StreamAnalytics](tutorial-deploystreamtostorage.md)

## Set up a Cron job to Send Device Information when your Raspberry Pi Boots Up

1. From your Windows Cloud Machine, open a console application and remote SSH into your Raspberry Pi from the command prompt as using {your account}@{hostname}, for example,

    ```azurecli
    c:\>ssh me@raspberrypi
    me@raspberrypi's password:
    Linux raspberrypi 5.15.76-v7+ #1597 SMP Fri Nov 4 12:13:17 GMT 2022 armv7l
    
    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.
    
    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Sun Jan  1 20:27:12 2023 from fe80::5a68:8a07:f908:168a%wlan0
    me@raspberrypi:~ $
    ```

1. Using your remote SSH session, open crontab in the GNU nano editor in your Raspberry Pi,

    ```azurecli
    $ crontab -e
    ```

    For example,

    ![lnk_crontab]

1. Copy and paste the following entry to crontab,

    ```azurecli
    @reboot python ~/repos/IoT/python/raspberrypi/d2cipandhostname.py
    ```

    *Note that you can use the sudo command in the previous step, but you'll need to reference the full path. For example,
    ```azurecli
    $ sudo crontab -e
    @reboot python /home/jbeman/repos/IoT/python/raspberrypi/d2cipandhostname.py
    ```

1. Type ctrl-o and hit the enter key, for example,

    ```azurecli
    $ ctrl-o
    $ File Name to Write: /tmp/crontab.4SQV5b/crontab
    ```

1. Type `ctrl-x` to exit `crontab`, then run the following command,

    ```azurecli
    sudo shutdown -r
    ```

1. Verify the message was sent to the cloud and saved in storage using Stream Analytics.

## Next Steps

Congratulations, you've successfully remotely coded a real device and connected it to Azure! You are ready to continue your journey and learn to wire IoT electronics to your Raspberry Pi and remotely controlling it.

[Tutorial: Light up an LED](tutorial-rasp-led.md)

<!--images-->

[lnk_crontab]: media/tutorial-rasp-d2cipandhostname/crontab.png