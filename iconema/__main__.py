from iconema import Iconema
from color import Color
import logging
import argparse
import sys


def create_argument_parser():
    parser = argparse.ArgumentParser(description='Color Matching Program')
    parser.add_argument('-i', '--image', required=True,
                        help='Path to the input image that will be analyzed')

    # Need a list of colors
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--base', action='store_true',
                       help='Create base 16 colorscheme')
    group.add_argument('-c', '--colors', nargs='+',
                       help='List of colors to match in the image')

    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase verbosity level")
    parser.add_argument('-d',
                        '--downsample',
                        action='store_true',
                        help='Downsample the image for efficiency')
    # parser.add_argument('-h', '--help', action='store_true',
    #                     help='Print help message')

    return parser


def main():
    parser = create_argument_parser()
    args = parser.parse_args()
    # Set up verbosity
    if args.verbose:
        log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
        log_level = log_levels[min(args.verbose, 2)]
        logging.getLogger().setLevel(log_level)

    if args.base:
        color_list = ["000000", "ff3333", "33ff33", "ffff33",
                      "3333ff", "ff33ff", "33ffff", "a8a8a8",
                      "545454", "ff8080", "80ff80", "ffff80",
                      "8080ff", "ff80ff", "80ffff", "ffffff"]
    else:
        color_arg = args.colors[0].split() if len(args.colors) == 1 else args.colors
        try:
            color_list = [Color.hex_valid(color) for color in color_arg]
        except ValueError as e:
            logging.error(f"ValueError: {e}")
            sys.exit(1)

    image = Iconema(args.image, args.downsample)
    color_matches = [Color.rgb_hex(image.get_match(Color.hex_rgb(theme_color)))
                     for theme_color in color_list]
    print(color_matches)


if __name__ == "__main__":
    main()