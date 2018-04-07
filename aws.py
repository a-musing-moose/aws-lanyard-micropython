from machine import Pin, SPI, TouchPad


class LEDRing(object):

    MAX_BRIGHTNESS = 0xff

    def __init__(self):
        self.num_pixels = 6
        self.leds = [[self.MAX_BRIGHTNESS, 0x00, 0x00, 0x00] for _ in range(self.num_pixels)]
        self.spi = SPI(sck=Pin(14), mosi=Pin(16), miso=Pin(12)) # setup SPI

    def set_pixel(self, index, red, green, blue, brightness=MAX_BRIGHTNESS):
        if index < 0 or index > self.num_pixels - 1:
            raise Exception("index out of range")

        if red < 0 or green > 0xff:
            raise Exception("red value out of range")

        if green < 0 or green > 0xff:
            raise Exception("green value out of range")

        if blue < 0 or blue > 0xff:
            raise Exception("blue value out of range")

        if brightness < 0 or brightness > 0xff:
            raise Exception("brightness value out of range")

        self.leds[index] = [brightness, blue, green, red]

    def write(self):
        self.spi.write(b'\x00\x00\x00\x00')
        for led in self.leds:
            self.spi.write(bytearray(led))
        self.spi.write(b'\xff\xff\xff\xff')

    def off(self):
        for i in range(6):
            self.set_pixel(i, 0x00, 0x00, 0x00, self.MAX_BRIGHTNESS)
        self.write()

    def on(self):
        for i in range(6):
            self.set_pixel(i, 0xff, 0xff, 0xff, self.MAX_BRIGHTNESS)
        self.write()

    def rotate(self):
        self.leds = self.leds[-1:] + self.leds[:-1]
        self.write()


def get_touchpad():
    return TouchPad(Pin(2))
