#Iconema
## What is iconema?
This is a script and library that takes a list of colors as input and finds the
closest match to them in an image. It can be used as a utility to generate
color palettes for customization purposes, and that's what it has been created
for.

## How does it work?
This program analyzes the given image and organizes all its unique color values
into a k-d tree data structure. This k-d tree is then utilized to efficiently
find the closest matching color for each distinct input color value.

## Default base palette
The `-b` command option, tries to match the following 16 colors in order to
create a "Base16" color palette with colors that are different enough that you
can use as a colorscheme in a terminal emulator. This option is great with
images that have a specific color theme or use a limited color palette, AKA
most wallpapers.

```
color0  = #000000
color1  = #ff3333
color2  = #33ff33
color3  = #ffff33
color4  = #3333ff
color5  = #ff33ff
color6  = #33ffff
color7  = #a8a8a8
color8  = #545454
color9  = #ff8080
color10 = #80ff80
color11 = #ffff80
color12 = #8080ff
color13 = #ff80ff
color14 = #80ffff
color15 = #ffffff
```
## TODO
- [ ] Clean up code.
- [x] Create argument parser.
- [ ] Transparency support. Implement by converting all RGB colors to RGBA and
      then returning the apprpriate value, depending on if the user requested
      alpha matching
- [x] Option where user provides colors and program outputs closest match in an
      image.
