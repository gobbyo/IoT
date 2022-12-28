---
title: Light up an LED
description: #Required; article description that is displayed in search results. 
author: jbeman@hotmail.com
---

<!--
Remove all the comments in this template before you sign-off or merge to the 
main branch.
-->

<!--
This template provides the basic structure of a tutorial article.
See the [tutorial guidance](contribute-how-to-mvc-tutorial.md) in the contributor guide.

To provide feedback on this template contact 
[the templates workgroup](mailto:templateswg@microsoft.com).
-->

<!-- 1. H1 
Required. Start with "Tutorial: ". Make the first word following "Tutorial: " a 
verb.
-->

# Tutorial: Light up an LED 

<!-- 2. Introductory paragraph 
Required. Lead with a light intro that describes, in customer-friendly language, 
what the customer will learn, or do, or accomplish. Answer the fundamental “why 
would I want to do this?” question. Keep it short.
-->

[Add your introductory paragraph]

<!-- 3. Tutorial outline 
Required. Use the format provided in the list below.
-->

In this tutorial, you learn how to:

> [!div class="checklist"]
> * All tutorials include a list summarizing the steps to completion
> * Each of these bullet points align to a key H2
> * Use these green checkboxes in a tutorial

<!-- 4. Prerequisites 
Required. First prerequisite is a link to a free trial account if one exists. If there 
are no prerequisites, state that no prerequisites are needed for this tutorial.
-->

## Prerequisites

- An Azure account with an active subscription. [Create an account for free]
  (https://azure.microsoft.com/free/?WT.mc_id=A261C142F).
- Completed the tutorial to Configure your Windows Machine
- <!-- prerequisite n -->

<!-- 5. H2s
Required. Give each H2 a heading that sets expectations for the content that follows. 
Follow the H2 headings with a sentence about how the section contributes to the whole.
-->

## Wire Your Raspberry Pi with an LED

Use the following diagram.

1. From the Raspberry Pi, connect GPIO17 (BCM), PIN 13 (BOARD), to a lead on the 220Ω resistor.  GPIO17 used in this example isn't special, as you can use any GPIO pin, e.g. GPIO2, GPIO12, etc.
1. Connect the positive lead on the LED (the longest lead) to the 220Ω resistor.
1. Connect the negative lead on the LED (the shorter lead) to Ground on the Raspberry Pi

    ![lnk_raspled]

## Create Code to Turn the LED on and off
<!-- Introduction paragraph -->
1. Connect Visual Studio Code to your Raspberry Pi.
1. Create a file `led.py` in your github directory.
1. Copy and paste the following import statement

    ```python
    import RPi.GPIO as GPIO
    ```

1. Copy and paste the following method to obtain basic information about your Raspberry Pi. [todo] explain this!

    ```python
    def main():
        LED_channel = 17
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_channel, GPIO.OUT)
        GPIO.output(LED_channel, GPIO.LOW)
    
        print("Press Ctrl-C to quit'")
    
        try:
            while True:
                s = input("Type 'On', 'Off', or 'Info': ")
                if s == 'On':
                    GPIO.output(LED_channel, GPIO.HIGH)
                    print("On")
                else:
                    GPIO.output(LED_channel, GPIO.LOW)
                    print("Off")
                print("-----")
        except KeyboardInterrupt:
            print("Program shut down by user")
        finally:
            GPIO.cleanup()
            print("Cleaning up and shutting down")
    
    if __name__ == "__main__":
        main()
    ```

## Run It!
<!-- Introduction paragraph -->
1. <!-- Step 1 -->
1. <!-- Step 2 -->
1. <!-- Step n -->

<!-- 6. Clean up resources
Required. If resources were created during the tutorial. If no resources were created, 
state that there are no resources to clean up in this section.
-->

## Clean up resources

If you're not going to continue to use this application, delete
<resources> with the following steps:

1. From the left-hand menu...
1. ...click Delete, type...and then click Delete

<!-- 7. Next steps
Required: A single link in the blue box format. Point to the next logical tutorial 
in a series, or, if there are no other tutorials, to some other cool thing the 
customer can do. 
-->

## Next steps

Advance to the next article to learn how to create...
> [!div class="nextstepaction"]
> [Next steps button](contribute-how-to-mvc-tutorial.md)

<!--images-->

[lnk_raspled]: media/tutorial-rasp-led/rasp-led.png
