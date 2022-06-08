import json


class ConfigurationFileError(ValueError):
    pass


class ConfigurationValueError(ValueError):
    pass


class ConfigurationKeyError(ValueError):
    pass


class Config:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.load()
        self.validate()

    def load(self) -> dict:
        try:
            with open(self.filename) as content:
                return json.load(content)
        except IOError as io_error:
            raise ConfigurationFileError("Configuration file error") from io_error

    def validate(self) -> bool:
        try:
            if type(self.data["display"]["size"]["width"]) != int or self.data["display"]["size"]["width"] < 0:
                raise ConfigurationValueError("display -> size -> width")

        except KeyError as key_error:
            raise ConfigurationKeyError("display -> size -> width") from key_error

        try:
            if type(self.data["display"]["size"]["height"]) != int or self.data["display"]["size"]["height"] < 0:
                raise ConfigurationValueError("display -> size -> height")

        except KeyError as key_error:
            raise ConfigurationKeyError("display -> size -> height") from key_error

        try:
            if type(self.data["display"]["i2c"]["sda"]) != int or self.data["display"]["i2c"]["sda"] < 0:
                raise ConfigurationValueError("display -> i2c -> sda")
        except KeyError as key_error:
            raise ConfigurationKeyError("display -> i2c -> sda") from key_error

        try:
            if type(self.data["display"]["i2c"]["scl"]) != int or self.data["display"]["i2c"]["scl"] < 0:
                raise ConfigurationValueError("display -> i2c -> scl")

        except KeyError as key_error:
            raise ConfigurationKeyError("display -> i2c -> scl") from key_error

        try:
            if type(self.data["display"]["i2c"]["addr"]) != str:
                raise ConfigurationValueError("display -> i2c -> addr")

            if type(int(self.data["display"]["i2c"]["addr"])) != int:  # base=16
                raise ConfigurationValueError("display -> i2c -> addr")

        except KeyError as key_error:
            raise ConfigurationKeyError("display -> addr") from key_error
        except ValueError as value_error:
            raise ConfigurationValueError("display -> addr") from value_error

        return True


    def get_display_addr(self) -> int:
        return int(self.data["display"]["addr"], base=16)

    def get_display_width(self) -> int:
        return self.data["display"]["size"]["width"]

    def get_display_height(self) -> int:
        return self.data["display"]["size"]["height"]

    def get_display_i2c_sda(self) -> int:
        return self.data["display"]["i2c"]["sda"]

    def get_display_i2c_scl(self) -> int:
        return self.data["display"]["i2c"]["scl"]

    def get_display_i2c_addr(self) -> int:
        return int(self.data["display"]["i2c"]["addr"])
