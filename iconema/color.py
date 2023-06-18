import logging
import sys
import re


class Color:

    @staticmethod
    def hex_valid(hex_code):

        # Remove prefix # for simpler code
        hex_code = hex_code.lstrip('#')
        hex_s_re = r'^([A-Fa-f0-9]{3})[A-Fa-f0-9]?$'
        hex_l_re = r'^([A-Fa-f0-9]{6})([A-Fa-f0-9]{2})?$'

        if re.match(hex_s_re, hex_code):
            r = hex_code[0]
            g = hex_code[1]
            b = hex_code[2]
            if len(hex_code) == 4:
                a = hex_code[3]
            else:
                a = "f"
            hex_code = f"{r}{r}{g}{g}{b}{b}{a}{a}"

        elif not re.match(hex_l_re, hex_code):
            raise ValueError("Invalid HEX color code! "
                             "Proper format is #xxx[xxx] or XXX[XXX].")
            return None

        if len(hex_code) != 8:
            hex_code = f"{hex_code}ff"

        return hex_code

    @staticmethod
    def hex_rgba(hex_code):
        # logging.debug(f"hex_code: {hex_code}")
        try:
            hex = Color.hex_valid(hex_code)
        except ValueError as e:
            logging.error(f"ValueError: {e}")
            sys.exit(1)
        # logging.debug(f"hex_code: {hex_code}")
        # logging.debug(f"hex: {hex}")
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        a = int(hex[6:8], 16)
        return (r, g, b, a)

    @staticmethod
    def rgba_hex(rgba):
        r, g, b, a = rgba
        return f"{r:02x}{g:02x}{b:02x}{a:02x}"

    @staticmethod
    def rgb_rgba(rgb):
        rgb_l = len(rgb)
        if rgb_l == 3:
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            return (r, g, b, 255)
        elif rgb_l == 4:
            return rgb
        else:
            logging.error("rgb_rgba: invalid rgb value of neither 3 or 4 length")
            sys.exit(1)
