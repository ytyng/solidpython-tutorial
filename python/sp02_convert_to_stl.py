from solid import *
from solid.utils import *
import pathlib
from openscad_utils import convert_to_stl


def main():
    c = cube(10)
    file_path = pathlib.Path(__file__).parent / 'cube.scad'
    scad_render_to_file(c, file_path)
    convert_to_stl(file_path)


if __name__ == '__main__':
    main()
