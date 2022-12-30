# Internet of Things

These tutorials were compiled as a way to understand Azure and how to use the Internet of Things (IoT) cloud services. When you complete these tutorials you will be able to build your own remotely controlled devices and solutions as presented in Azure's reference architectures.

You don't need to know much about Azure and only be familiar with the basics of coding to successfully get through this program. These tutorials focus on minimizing the cost of using Azure. You'll use PowerShell for cloud service management and Python for device coding on a Raspberry Pi.

## Tutorials

These tutorials are intended to be completed in the order they are listed. The table below details the supplies you'll need for a successful journey.

| Ingredient  | Description  |
|---------|---------|
| An Azure Subscription | There are a few avenues to choose from: a one-time [free Azure subscription](https://azure.microsoft.com/en-us/free) with $200 USD 30-day starter or a student subscription with a 12 month $100 Azure credit limit. You'll need to opt in for pay-as-you go once the free offers expire. The $100 credit won't be enough should you need to create a cloud virtual machine, see the prerequisite tutorial to [Create A Virtual Machine](docs/tutorial-prerequisites.md). The other option is to purchase a [Visual Studio Professional subscription](https://www.microsoft.com/en-us/d/visual-studio-professional-subscription/dg7gmgf0dst3?activetab=pivot:overviewtab) or higher, which provides you with an Azure monthly limit of around $150 USD. |
| A Raspberry Pi | A model 3 was used to create these tutorials, however you'll only need a basic model. Note these tutorials do not make use of any desktop features. Your best bet is to purchase one directly from the https://www.raspberrypi.com/ website |
| [A Starter Kit](https://www.amazon.com/starter-kit-raspberry-pi/s?k=starter+kit+raspberry+pi) for your Raspberry Pi | There is a wide variety to choose from but you'll only need the most basic starter kit. A good starter kit will have a plethora of electronics (sensors, LEDs, motors, buzzers, transistors, resistors), with accompanying tutorials explaining the concepts of each electronic part, the schematic for connecting the part to your Raspberry Pi, and provides reference material such as specifications to each electronic part. |
| A micro-SD card of 16 MB or higher and a micro-SD to USB-C adapter | Note that some starter kits come with these items. |

### IoT Fundamentals with a Simulated Device

This section of tutorials starts you on the basics of IoT cloud development. With the exception on the first tutorial to [Create a Cloud Virtual Machine](docs/tutorial-prerequisites.md), the remaining tutorials focus on setting up and using IoT Cloud services. No need for a Raspberry Pi in this section of tutorials because you'll simulate the device with code. Once you've completed this section you'll have a solid understanding of the Azure Cloud.

1. [Create a Cloud Virtual Machine](docs/tutorial-prerequisites.md)
1. [Configure your Cloud Machine](docs/tutorial-configure.md)
1. [Create an IoT Hub and Storage Account](docs/tutorial-deployiothub.md)
1. [Create a Simulated Device](docs/tutorial-symmetrickeydevice.md)
1. [Send a Message from the Cloud to a Simulated Device](docs/tutorial-cloudtodevicemsg.md)
1. [Send a Message from a Simulated Device to the Cloud](docs/tutorial-devicetocloudmsg.md)
1. [Upload a file to the Cloud from your Device](docs/tutorial-uploaddevicefile.md)
1. [Create a Stream Analytics Job](docs/tutorial-deploystreamtostorage.md)

### Raspberry Pi and Cloud Starter

This section of tutorials covers setting up your Raspberry Pi with an easy way to remotely code on it. Upon completion, and whenever your Raspberry Pi boots up, your device will send essential information to the cloud services you set up in the previous section. Once you've completed this section you'll have a solid understanding of how to scale and securely use IoT device on the public internet.

1. [Set up your Raspberry Pi and Remotely Connect Visual Studio Code](docs/tutorial-rasp-connect.md)
1. [Create a Device Provisioning Service](docs/tutorial-deploydps.md)
1. [Provision and Test a Device using an x509 Certificate](docs/tutorial-dpsx509deviceenrollment.md)
1. [Send Hostname, IP Address, and Device Information to the Cloud](docs/tutorial-rasp-d2cipandhostname.md)

### Raspberry Pi and Cloud IoT Building Blocks

This section of tutorials are sequentially paired where the first tutorial focuses on wiring a sensor or device (LED, Sensor, Motor, Buzzer, or Display) to your Raspberry Pi followed by the next tutorial showing you how to remotely control the device. For example, the first tutorial [Light Emitting Diode (LEDs)](docs/tutorial-rasp-led.md) has you connect an LED to your Raspberry Pi and write code to switch on or off your LED. The subsequent tutorial, [Remotely Control an LED](docs/tutorial-rasp-remoteled.md), has you code your Raspberry Pi to receive Cloud messages to remotely switch on or off the LED. Once you've completed this section you'll have the essential building blocks to build a variety of projects and enough coding experience to remotely control and manage them.

1. [Light Emitting Diode (LEDs)](docs/tutorial-rasp-led.md)
1. [Remotely Control an LED](docs/tutorial-rasp-remoteled.md)
1. Light Emitting Display Bar Graph
1. Remotely Control a Light Emitting Display Bar Graph
1. Passive Buzzer
1. Remotely Control a Passive Buzzer with Morse Code
1. Seven Segment Digit Display
1. Remotely Control a Seven Segment Digit Display
1. Liquid Crystal Display
1. Remotely Control a Liquid Crystal Display
1. Ultrasonic Distance Sensor
1. Send Ultrasonic Distance Sensor Data to the Cloud
1. Temperature and Humidity Sensor
1. Send Temperature and Humidity Sensor Data to the Cloud
1. Photoresistor
1. Send Light Measurements to the Cloud
1. DC Motor
1. Remotely Control a DC Motor
1. Step Motor
1. Remotely Control a Step Motor
1. Sensor Hat
1. [Remotely Control a Sensor Hat](docs/tutorial-rasp-d2csensorhat.md)
1. Camera
1. Remotely Control a Camera

## Additional IoT Services

1. [Deploy Map Routing](docs/tutorial-deploymaps.md)
1. [Create a Turn-by-turn Route Simulated Device](docs/tutorial-maproutelistener.md)
1. [Send a Route of Coordinates](docs/tutorial-maproutecommand.md)
1. Create a Digital Twins Service
1. Configure your Digital Twins Service

## How to guides

1. [How to Use Your Azure Subscription](docs/howto-connecttoazure.md)
1. [How to Find and Set Your Connection Strings](docs/howto-connectionstrings.md)