from PIL import Image
from scipy.spatial import KDTree
from color import Color
import numpy as np
import os
import logging


class Iconema:
    def __init__(self, image_path, dosc):
        try:
            self.open(image_path)
        except Exception as e:
            logging.error(f"Exception occurred: {e}")
        if dosc == 1:
            file_ext = os.path.splitext(image_path)[1]
            self.set_ds_path(f"/tmp/chromade-ds{file_ext}")
            self.downscale()
            self.file = Image.open(self.ds_path)
        self.set_palette()
        self.set_palette_kd()

    def open(self, path):
        if os.path.exists(path):
            self.file = Image.open(path)
        else:
            raise FileNotFoundError(f"File {path} doesn't exist.")

    def set_palette(self):
        pixels = self.file.getcolors(self.file.size[0] * self.file.size[1])
        palette = {Color.rgb_rgba(color[1]) for color in pixels}
        self.palette = palette

    def get_palette(self):
        return self.palette

    def set_palette_kd(self):
        palette_array = np.array(list(self.palette))
        print(f"{palette_array}")
        self.palette_kd = KDTree(palette_array)

    def get_palette_kd(self):
        return self.palette_kd

    def set_ds_path(self, ds_path):
        self.ds_path = ds_path

    def downscale(self):
        target_size = (1000, 1000)
        resized_image = self.file.resize(target_size, Image.LANCZOS)
        resized_image.save(self.ds_path)

    def get_match(self, color_target):
        # Find the nearest neighbor
        _, index = self.palette_kd.query(color_target)
        # Retrieve the closest color
        color_match = list(self.palette)[index]
        return color_match
