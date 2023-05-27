import subprocess


def open(file_name):
    subprocess.Popen(['openscad', file_name])


def convert_to_stl(file_name):
    subprocess.Popen([
        'openscad', '-o', file_name.replace('.scad', '.stl'), file_name])
