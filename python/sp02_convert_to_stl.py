from solid.utils import *
from openscad_utils import convert_to_stl  # open_openscad,


def main():
    c = cylinder(5, 10, segments=180)
    # open_openscad(c)
    convert_to_stl(c, preview=True)


if __name__ == '__main__':
    main()
