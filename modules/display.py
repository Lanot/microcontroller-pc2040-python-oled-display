import machine
from libs.ssd1306 import SSD1306_I2C
from modules.config import Config


class Display:
    def __init__(self, config: Config):
        self.config = config
        self.sda = machine.Pin(self.config.get_display_i2c_sda())
        self.scl = machine.Pin(self.config.get_display_i2c_scl())
        self.i2c = machine.I2C(0,sda=self.sda, scl=self.scl, freq=400000)

        self.device = SSD1306_I2C(self.config.get_display_width(), self.config.get_display_height(), self.i2c)

        self.display_letter_size = 8
        self.max_line_number = (self.config.get_display_height() / self.display_letter_size) - 1
        self.max_line_symbols = (self.config.get_display_width() / self.display_letter_size)

    def clear(self):
        self.device.fill(0)

        return self

    # 8 pixels per symbol
    # 8 lines, 16 symbols per line if 128x64
    # 4 lines, 16 symbols per line if 128x32
    def line(self, s: str, line: int):
        if line < 0:
            raise ValueError('Expected 0 or positive line number.')

        if line > self.max_line_number:
            raise ValueError('Expected line number should be less or equal than {}.'.format(self.max_line_number))

        if len(s) > self.max_line_symbols:
            raise ValueError('Expected string length should be less or equal than {}.'.format(self.max_line_symbols))

        self.device.text(s, 0, line * self.display_letter_size, 1)
        self.device.show()

        return self
