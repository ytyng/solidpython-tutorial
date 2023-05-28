import pathlib
import subprocess
import sys

from solid import OpenSCADObject, scad_render_to_file


def save_openscad(o: OpenSCADObject):
    file_path = sys.argv[0].replace('.py', '.scad')
    scad_render_to_file(o, file_path)
    return file_path


def file_name_or_object_to_file_name(
    file_name_or_object: OpenSCADObject | str | pathlib.Path
):
    if isinstance(file_name_or_object, OpenSCADObject):
        return save_openscad(file_name_or_object)
    elif isinstance(file_name_or_object, pathlib.Path):
        return file_name_or_object.as_posix()
    else:
        return file_name_or_object


def open_openscad(file_name_or_object: OpenSCADObject | str | pathlib.Path):
    file_name = file_name_or_object_to_file_name(file_name_or_object)
    process = subprocess.Popen(['open', '-a', 'OpenSCAD', file_name])
    process.wait()


def convert_to_stl(
    file_name_or_object: OpenSCADObject | str | pathlib.Path, *,
    preview: bool = False
):
    file_name = file_name_or_object_to_file_name(file_name_or_object)

    stl_file_name = file_name.replace('.scad', '.stl')
    command = [
        'open', '-a', 'OpenSCAD', '--hardwarnings', '-o', stl_file_name,
        file_name]
    process = subprocess.Popen(command)
    process.wait()
    if preview:
        subprocess.Popen(['open', '-a', 'Preview', stl_file_name])
