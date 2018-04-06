AWS ESP32 Lanyard Micropython Support Library
=============================================

`aws.py` is a work in progress library to give simple support for the functionality of the AWS 2017 Re:invent ESP32
Lanyards.

Turns out these devices are bascially stock ESP32, so they can run stock Micropython. :-)

So once you have micropython installed you can copy across `aws.py` to get support for some of the fun things on the
lanyard button thingy.


LEDRing
-------

The ``LEDRing`` class p[rovides a simple interface to the 6 RGB LEDs around the edge of the device.

.. code-block:: python

    from aws import LEDRing

    ring = LEDRing()
    red = 0
    green = 0
    blue = 128
    brightness = 255
    ring.set_pixel(0, red, green, blue, brightness)  # Set pixel 0 to blue
    ring.write()  # Write changes to the LEDs
    ring.rotate()  # Rotate all the pixel definition 1 step clockwise and write the update
    ring.on()  # Turn all LEDs on (white, full brightness)
    ring.off()  # Turn off all the LEDs


The pixels are all individually addressable on index 0 - 5.
