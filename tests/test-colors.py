import unittest
from iconema import color

class RGBhex_Test(unittest.TestCase):

    def test_rgb_to_hex(self):
        for r in range(256):
            for g in range(256):
                for b in range(256):
                    expected_hex = f"{r:02x}{g:02x}{b:02x}" 
                    self.assertEqual(Color.rgb_hex((r,g,b)), expected_hex)


class HEXrgb_Test(unittest.TestCase):
    def test_hex_to_rgb(self):
        for r in range(256):
            for g in range(256):
                for b in range(256):
                    hex_prefix = f"#{r:02x}{g:02x}{b:02x}" 
                    hex = f"#{r:02x}{g:02x}{b:02x}" 
                    Color.hex_rgb()

def test_hex_validator():
