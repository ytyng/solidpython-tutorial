from solid import *
from solid.utils import *
import pathlib


def main():
    c = cube(10)
    file_path = pathlib.Path(__file__).parent / 'sp01_create_cube.scad'
    scad_render_to_file(c, file_path)


if __name__ == '__main__':
    main()
