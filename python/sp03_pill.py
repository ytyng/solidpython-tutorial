from solid import *
from openscad_utils import convert_to_stl


def main():
    s1 = translate([-5, 0, 0])(sphere(5, segments=90))
    s2 = translate([5, 0, 0])(sphere(5, segments=90))
    c1 = translate([-5, 0, 0])(
        rotate([0, 90, 0])(cylinder(5, 10, segments=90)))
    convert_to_stl(s1 + s2 + c1, preview=True)


if __name__ == '__main__':
    main()
