## Manually Configuring Raspbian for pi-topPULSE

**Note:** This document was moved here from the github project wiki.
**Note:** This is definitely the long way round to get the pi-topPULSE working, and is provided only for interest. If you are running pi-topOS, you do not need to worry about this - everything is already included! If you are running Raspbian, please consult the `readme.md` file [here](https://github.com/pi-top/pi-topPULSE/blob/master/README.md) for the simpler method of enabling the pulse.

### Enabling I2C

I2C is required to communicate with the function-enabling IC as part of initialisation.

The simplest way to do this is by running `raspi-config`, selecting `Interfacing Options` → `I2C` → Select "Yes" to enabling I2C.

### Enabling UART/serial for LEDs and Microphone

The included version of Pyserial on Raspbian on Python 3 does not support custom baud rates, which is required for LEDs to work. Run the `upgrade-python3-pyserial` script in the [manual-install](/manual-install/@master) folder to update to the latest version of Pyserial.

You will also need to enable UART. The simplest way to do this is by running `raspi-config`, selecting `Interfacing Options` → `Serial` → Select "No" to enabling a login shell accessible over serial  → Select "Yes" for enabling serial port hardware.

### Configuring Audio Output (Speaker)

##### Enabling HDMI to I2S on the pi-top v2

The new pi-top supports an HDMI to I2S audio conversion system which eliminates the need for reconfiguring the operating system to use I2S and then rebooting. To enable this requires communicating with the hub. This can be by installing the following library:

    sudo apt install python3-pt-common

Now save the following script to a file, e.g. `/tmp/pt-hdmi-to-i2s`:

    #!/usr/bin/python3

    # Script to configure the new pi-top hub, enabling or disabling the
    # HDMI to I2S audio conversion.

    from ptcommon.i2c_device import I2CDevice
    import sys

    AUD__CONFIG = 0xC0
    AUD__CONFIG__HDMI = 0x01
    AUD__CONFIG__HPDET = 0x02

    if (len(sys.argv) != 2):
        print("Usage: " + sys.argv[0] + " <enable|disable>")
        sys.exit(1)
    elif (sys.argv[1] == "enable" or sys.argv[1] == "disable"):
        print("Usage: " + sys.argv[0] + " <enable|disable>")
        sys.exit(1)

    try:
        hub = I2CDevice("/dev/i2c-1", 0x10)
        hub.connect()

        audio_control = hub.read_unsigned_byte(AUD__CONFIG)

        if (sys.argv[1] == "enable"):
            hub.write_byte(AUD__CONFIG, audio_settings | AUD__CONFIG__HDMI)
        elif (sys.argv[1] == "disable"):
            hub.write_byte(AUD__CONFIG, audio_settings & (~AUD__CONFIG__HDMI & 0xFF))

    except Exception as e:

        print("Error communicating with hub: " + str(e))

Make this file executable by running:

    sudo chmod +x /tmp/pt-hdmi-to-i2s

Then run the script as follows:

    sudo /tmp/pt-hdmi-to-i2s enable

**Note:** This will be replaced with a formal method soon!

##### Configuring I2S on the original pi-top (v1) and pi-topCEED

I2S enabling/disabling and volume control configuration form part of the [general pi-top device management system](https://github.com/pi-top/Device-Management), however can be configured manually via the following commands, followed by a reboot, using [pt-i2s](https://github.com/pi-top/Device-Management/blob/master/src/i2s/pt-i2s):

    pt-i2s enable
    pt-i2s disable

Volume control for pi-topPULSE can be enabled by loading soundcard device information with the following command (with a pi-topPULSE connected, and with I2S enabled), followed by a reboot, using [hifiberry-alsactl.restore](https://github.com/pi-top/Device-Management/blob/master/src/i2s/hifiberry-alsactl.restore):

    /usr/sbin/alsactl -f /etc/pi-top/.i2s-vol/hifiberry-alsactl.restore restore

### Making the `ptpulse` Python library accessible

The easiest way to get the pi-topPULSE library is to install the debian package directly:

    sudo apt install python3-pt-pulse

You can also download the library files from this repository and use them locally.

## Using the software library to manually initialise pi-topPULSE

Once you have installed the library, you can now initialise the device yourself using the included `configuration.py`. For example:


    from ptpulse import configuration as ptpulsecfg

    # The pulse library needs to know what hardware it is running on.
    # For the pi-top v2 use 4, for all other platforms use 1
    host_device_type = 1

    ptpulsecfg.initialise(host_device_type):
    enabled, reboot_required, v2_hub_hdmi_to_i2s_required = ptpulsecfg.enable_device()

    if (reboot_required):
        print("Reboot required")
    elif (v2_hub_hdmi_to_i2s_required):
        print("HDMI to I2S required")
    elif (enabled):
        print("Successfully enabled pi-topPULSE")
    else:
        print("Failed to enable pi-topPULSE")


## Using pi-topPULSE in projects

You are now ready to use the pi-topPULSE! Check out the [examples](/examples@master) folder to get some inspiration of how you can use it.
