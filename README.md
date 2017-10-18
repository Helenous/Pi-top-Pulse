# pi-topPULSE

![Image of pi-topPULSE addon board](https://static.pi-top.com/images/pulse-small.png "Image of pi-topPULSE addon board")

Visit the [pi-topPULSE product page](https://pi-top.com/products/pulse) on the pi-top website for more information.

## Table of Contents
* [Quick Start](#quick-start)
* [Hardware](#hardware)
* [Software](#software)
    * [pi-topPULSE on pi-topOS](#software-pt-os)
    * [pi-topPULSE on Raspbian](#software-raspbian)
    * [How it works - 'under the hood'](#software-how-it-works)
* [Using pi-topPULSE](#using)
	* [Amazon's Alexa Voice Service](#using-avs)
	* [Using a custom Python script](#using-script)
* [Documentation & Support](#support)
    * [Links](#support-links)
    * [Troubleshooting](#support-troubleshooting)

## <a name="quick-start"></a> Quick Start
#### pi-topPULSE on pi-topOS
* Boot into pi-topOS (released on or after 12-07-2017)
* Plug in pi-topPULSE
* Follow on-screen instructions, if necessary
    * Instructions will appear in pi-topDASHBOARD and in a messagebox on the desktop, and will typically ask the user to reboot. If no messages appear and the red LED on the underside turns off shortly after being plugged in, the hardware should be ready to use.
* Enjoy - check out the [examples](https://github.com/pi-top/pi-topPULSE/tree/master/examples) to see what you can do! And try asking Alexa questions via pi-topDASHBOARD! (Note: you will need to be logged in for this)

---

#### pi-topPULSE on Raspbian
* Run the following commands in the terminal (with an internet connection):

```
sudo apt update
sudo apt install pt-pulse
```

* Plug in pi-topPULSE
* Follow on-screen instructions, if necessary
    * Instructions will appear in pi-topDASHBOARD and in a messagebox on the desktop, and will typically ask the user to reboot. If no messages appear and the red LED on the underside turns off shortly after being plugged in, the hardware should be ready to use.
* Enjoy - check out the [examples](https://github.com/pi-top/pi-topPULSE/tree/master/examples) to see what you can do! See [here](https://github.com/pi-top/Alexa-Voice-Service-Integration) for more on using pi-top's Alexa Voice Service integration.

## <a name="hardware"></a> Hardware

pi-topPULSE is a 7x7 LED grid, speaker and microphone combined into a single device that can be used as a HAT or pi-top addon. Additionally the device features ambient lights which reflect the state of the LED array, four around the speaker, and three on the underside. The speaker has an output of 2W, and the microphone has 200Hz to 11KHz response and automatic gain control (AGC).

pi-topPULSE uses a variety of interfaces to communicate with the Raspberry Pi: the speaker uses I2S, and the LEDs and microphone use serial (UART), Tx and Rx respectively.

For information on the pi-topPULSE's GPIO pinout, see [here](https://pinout.xyz/pinout/pi_toppulse).

#### Resources used by the pi-topPULSE

pi-topPULSE uses the following resources:

* GPIO pins 3 and 5 for I2C communication and control.
* GPIO pins 8 and 10 for UART (serial) communication.
* GPIO pins 12, 35 and 40 for I2S
* The device controller is exposed on I2C address 0x24

_Note: GPIO pins are references by their physical number_

For a full pinout of the pi-topPULSE, see this [GPIO Pinout](https://pinout.xyz/pinout/pi_toppulse)


## <a name="software"></a> Software
#### <a name="software-pt-os"></a> pi-topPULSE on pi-topOS

All pi-topPULSE software and libraries are included and configured 'out-of-the-box' as standard on pi-topOS (released on or after 12-07-2017). Simply connect a pi-topPULSE to your pi-top, reboot if instructed to do so, and it will be automatically initialised and ready to produce light, capture and play audio. Volume control is handled by the operating system.

Download the latest version of pi-topOS [here](https://pi-top.com/products/os#download).

As mentioned in the [Hardware](#hardware), the speaker on the pi-topPULSE uses I2S. This has the following implications:

* On an original pi-top or pi-topCEED I2S must be enabled, which will require a reboot from a typical Raspbian configuration (using the default sound drivers). This is also true in reverse: if you have previously configured a pi-topPULSE and you wish to use the standard HDMI or 3.5mm sound outputs, this will also require a reboot.

* On a new pi-top, the hub has the capability to convert HDMI audio to I2S before sending it to the pi-topPULSE. As a result, enabling I2S and rebooting is no longer required. 

* In both the above cases, the very first time a pi-topPULSE is connected, a reboot may still be required to enable UART. You will be prompted to reboot if so.

##### Technical information
Automatic initialisation is performed by the software contained in the package called `pt-device-manager`. This installs a program called `pt-device-manager`, which runs in the background and scans for newly connected devices. If a device is detected (and its supporing library is installed), it will be initialised and enabled automatically.

When the `pt-pulse` package is installed, `pt-device-manager` will also be installed as dependency, thus starting the background process. Depending on whether running on an original pi-top or a new pi-top the user will be notified if a reboot is required. If a reboot is not required, the device will be initialised and ready to use.

For more information about pt-device-manager, see [this repository](https://github.com/pi-top/Device-Management).

#### <a name="software-raspbian"></a> pi-topPULSE on Raspbian
The pi-topPULSE software can be found on the Raspbian software repositories. To install it, simply run the following commands at the terminal and then reboot:


```
sudo apt update
sudo apt install pt-pulse
```

This will install the ptpulse Python library, as well as its dependencies, including pt-device-manager (see above).

If you prefer to manually install the packages or want to install a specific set of packages see the [Manual Configuration and Installation](https://github.com/pi-top/pi-topPULSE/wiki/Manual-Configuration-and-Installation) page on the wiki.

#### <a name="software-how-it-works"></a> How it works - 'under the hood'
For more information on how to use the library files, take a look at the [initialisation section of the 'Manual Configuration and Installation'](https://github.com/pi-top/pi-topPULSE/wiki/Manual-Configuration-and-Installation#using-the-software-library-to-manually-initialise-pi-toppulse) page on the wiki.
Also check out the [examples](https://github.com/pi-top/pi-topPULSE/tree/master/examples) folder for guidance of what the library is capable of.

## <a name="using"></a> Using pi-topPULSE

#### <a name="using-avs"></a> Amazon's Alexa Voice Service

As the pi-topPULSE has the capability to both record and playback audio, it can be used to interact with voice assistants such as Amazon Alexa. We have integrated Alexa into pi-topOS, and created an open source repository to show how to make use of this yourself. See [here](https://github.com/pi-top/Alexa-Voice-Service-Integration) for more on using pi-top's Alexa Voice Service integration. Note: this implementation requires a pi-top account.

#### <a name="using-script"></a> Using a custom Python script

Once installed, pi-topPULSE can be used in Python3 by importing the modules in the `ptpulse` library: `configuration`, `microphone` and `ledmatrix`. In the future we aim to produce some formal documentation for this library, but for the time being there is some sample code in the [examples](https://github.com/pi-top/pi-topPULSE/tree/master/examples) folder of this repository. 

Note that using the `ptpulse` Python module requires root access to function. If you are running a script, make sure that you are running it with root access. You can do this with the "sudo" command:

	sudo python3 my_cool_pulse_script.py

Alternatively, if you are running Python in `IDLE`, please make sure you start LXTerminal and run idle or idle3 with the "sudo" command, like so:

    sudo idle3

## <a name="support"></a> Documentation & Support
#### <a name="support-links"></a> Links
* [Device Management (pt-device-manager)](https://github.com/pi-top/Device-Management)
* [GPIO Pinout](https://pinout.xyz/pinout/pi_toppulse)
* [Support](https://support.pi-top.com/)

#### <a name="support-troubleshooting"></a> Troubleshooting
##### Why is my pi-topPULSE not working?

* Currently, **pi-topPULSE is only supported on Raspberry Pi 3**. This is due to problems setting the UART clock speed on earlier Raspberry Pi models. It might be possible to get this to work on earlier versions, but this is not currently supported.

##### I have installed pi-topPULSE software manually...
* If you are running Linux kernel version 4.9.x previous to 4.9.35, pi-topPULSE [may not be fully functional](https://github.com/raspberrypi/linux/issues/1855). In particular, this issue prevents the pi-topPULSE LEDs from working. If you are experiencing this issue, please check your kernel version by typing `uname -r` at the terminal. You can update your kernel version to the latest by running `sudo apt install raspberrypi-kernel`.

* If you are attempting to use Python 3, and have installed manually, you need to ensure that you have the latest version of the PySerial module. Take a look at [the script](manual-install/upgrade-python3-pyserial) in the `manual-install` directory for how to do this.

##### The red LED on the underside of my pi-topPULSE is on - what does this mean?
* This LED indicates that the sampling rate of the microphone is set to 16kHz. By default, when plugged in, you will see that this LED is switched on, and can be used as a guide to show that it has not yet been initialised. Once initialised, the default sample rate is 22050Hz (~22KHz), and this is why the red LED is switched off. *Note: [pi-top's Amazon Alexa Voice Service integration](https://github.com/pi-top/Alexa-Voice-Service-Integration) uses 16kHz, which is denoted with the red LED being on. In this context, the red LED can be considered as an indicator that the pi-topPULSE is capturing audio.*

##### Why can't I get my Bluetooth working after connecting a pi-topPULSE?
* This is a known issue, and we are evaluating the best user experience for resolving this issue. In the meantime, this issue is captured [here](https://github.com/pi-top/pi-topPULSE/issues/4) - follow the instructions to re-enable Bluetooth.
