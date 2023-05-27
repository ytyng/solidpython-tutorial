// Generated by SolidPython 1.1.3 on 2023-05-27 12:03:14


cube(size = 10);
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *
import pathlib


def main():
    c = cube(10)

    scad_render_to_file(c, pathlib.Path(__file__).parent / 'cube.scad')


if __name__ == '__main__':
    main()
 
 
************************************************/
