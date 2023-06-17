import logging
import re


class Color:

    @staticmethod
    def hex_valid(hex_code, prefix=None):

        # Remove prefix # for simpler code
        hex_code = hex_code.lstrip('#')
        hex_short_re = r'^([A-Fa-f0-9]{3})$'
        hex_long_re = r'^([A-Fa-f0-9]{6})$'

        if re.match(hex_short_re, hex_code):
            r = hex_code[0]
            g = hex_code[1]
            b = hex_code[2]
            hex_code = f"{r}{r}{g}{g}{b}{b}"
        elif not re.match(hex_long_re, hex_code):
            raise ValueError("Invalid HEX color code!\
                              Proper format is #xxx[xxx] or XXX[XXX].")
            return None

        if prefix is True:
            hex_code = f"#{hex_code}"

        return hex_code

    @staticmethod
    def hex_rgb(hex_code):
        # logging.debug(f"hex_code: {hex_code}")
        try:
            hex = Color.hex_valid(hex_code)
        except ValueError as e:
            logging.error(f"ValueError: {e}")
            return (0, 0, 0)
        # logging.debug(f"hex_code: {hex_code}")
        # logging.debug(f"hex: {hex}")
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        return (r, g, b)

    @staticmethod
    def rgb_hex(rgb, prefix=None):
        prefix = False if prefix is False else True
        numsign = "#" if prefix is True else ""
        r, g, b = rgb
        return f"{numsign}{r:02x}{g:02x}{b:02x}"
