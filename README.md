# Internet of Things

These tutorials were compiled as a way to understand Azure and how to use the Internet of Things (IoT) cloud services. When you complete these tutorials you will be able to build your own remotely controlled devices and solutions. Coding devices to use the IoT can provide a number of benefits, including:

- **Improved efficiency**. By using IoT devices, businesses and individuals can automate tasks and processes, which can lead to increased efficiency and productivity. For example, a company might use IoT sensors to monitor the temperature and humidity in a warehouse, and use this data to optimize the climate control system.
- **Enhanced security**. IoT devices can be used to monitor and secure physical assets and infrastructure. For example, a smart security system might use IoT sensors to detect unusual activity and send alerts to the owner or security personnel.
- **Increased connectivity**. IoT devices can be used to connect people, devices, and systems in ways that were previously not possible. For example, a smart home might use IoT devices to control the lighting, heating, and appliances, allowing the homeowner to control these systems remotely.
- **Improved decision-making**. IoT devices can generate large amounts of data, which can be used to inform decision-making and improve business operations. For example, a retailer might use IoT sensors to track customer foot traffic and use this data to optimize store layouts and product placements.
- **Enhanced customer experience**. IoT devices can be used to improve the customer experience in a variety of ways. For example, a hotel might use IoT devices to allow guests to control the temperature and lighting in their rooms, or a retailer might use IoT devices to personalize the shopping experience for individual customers.

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

This section of tutorials starts you on the basics of IoT cloud development. With the exception on the first tutorial to [Create a Cloud Virtual Machine](docs/tutorial-prerequisites.md), the remaining tutorials focus on setting up and using IoT Cloud services and using a simulated device to interact with them. No need for a Raspberry Pi in this section. There are several reasons you'll start with a simulated IoT device rather than a real one:

- **Cost**. Simulated IoT devices are typically less expensive than real ones, which can make them a more affordable option for learning and experimentation.
- **Convenience**. Simulated IoT devices can be more convenient to use than real ones, as they do not require physical setup or maintenance. This can be especially useful if you do not have access to a real IoT device or if you are learning remotely.
- **Safety**. Simulated IoT devices can be safer to use than real ones, as they do not involve any physical components or connections. This can be especially important if you are working with potentially hazardous devices or if you are learning to code with a limited understanding of the underlying hardware.
- **Reproducibility**. Simulated IoT devices can be easier to reproduce and share than real ones, which can be useful for collaborative learning or for sharing code examples.

However, it is also important to note that learning to code with a real IoT device can provide a more realistic and hands-on experience, which is covered in the tutorials that follow this section. Once you've completed this section you'll have a solid understanding of how IoT devices interact with the Cloud.

1. [Create a Cloud Virtual Machine](docs/tutorial-prerequisites.md)
1. [Configure your Cloud Machine](docs/tutorial-configure.md)
1. [Create an IoT Hub and Storage Account](docs/tutorial-deployiothub.md)
1. [Create a Simulated Device](docs/tutorial-symmetrickeydevice.md)
1. [Send a Message from the Cloud to a Simulated Device](docs/tutorial-cloudtodevicemsg.md)
1. [Send a Message from a Simulated Device to the Cloud](docs/tutorial-devicetocloudmsg.md)
1. [Upload a file to the Cloud from your Device](docs/tutorial-uploaddevicefile.md)
1. [Create a Stream Analytics Job](docs/tutorial-deploystreamtostorage.md)

### Raspberry Pi and Cloud Starter

This section of tutorials covers setting up your Raspberry Pi with an easy way to remotely code it. Once you've completed this section you'll have a solid understanding of how to scale and securely use IoT devices on the public internet.

1. [Set up your Raspberry Pi and Remotely Connect Visual Studio Code](docs/tutorial-rasp-connect.md)
1. [Create a Device Provisioning Service](docs/tutorial-deploydps.md)
1. [Create an x509 Certificate to Enroll Your Device](docs/tutorial-dpsx509deviceenrollment.md)
1. [Send Device Information to the Cloud with DPS](docs/tutorial-dpssenddeviceinfo.md)

### Raspberry Pi and Cloud IoT Building Blocks

This section of tutorials you'll dive into the the Raspberry Pi GPIO enabled sensors and peripherals and its communication with Cloud services. Note the tutorials are sequentially paired where the first tutorial focuses on wiring an electronic component (LED, Sensor, Motor, Buzzer, or Display) to your Raspberry Pi followed by the next tutorial showing you how to remotely control the component. For example, the first tutorial [Light Emitting Diode (LEDs)](docs/tutorial-rasp-led.md) has you connect an LED to your Raspberry Pi and write code to switch on or off your LED. The subsequent tutorial, [Remotely Control an LED](docs/tutorial-rasp-remoteled.md), has you code your Raspberry Pi to receive Cloud messages to remotely switch on or off the LED. Once you've completed this section you'll have the essential building blocks to build a variety of projects and enough coding experience to remotely control and manage them.

1. [Light Emitting Diode (LEDs)](docs/tutorial-rasp-led.md)
1. [Remotely Control an LED](docs/tutorial-rasp-remoteled.md)
1. [Light Emitting Display Bar Graph](docs/tutorial-rasp-ledbar.md)
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