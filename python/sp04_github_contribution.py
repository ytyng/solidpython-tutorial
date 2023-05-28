# https://github.com/ytyng

from solid.utils import *

from github_utils import get_github_contribution_cells

from openscad_utils import open_openscad


def list_chunk(items, chunk_size):
    return (items[i:i + chunk_size] for i in range(0, len(items), chunk_size))


def main():
    # Settings
    # Replace it with your github user name
    github_user_name = 'ytyng'

    # Object size settings
    max_tower_z = 20
    padding = 2
    cell_size = 5
    tower_size = 4
    plate_z_size = 2
    text_plate_y_size = 10

    # Get github contributions by my github_utils
    contribution_cells = get_github_contribution_cells(github_user_name)

    max_contribution_count = max(max(
        cell.contribution_count for cell in contribution_cells), 1)

    print(f'max_contribution_count: {max_contribution_count}')

    # create base plate
    plate_x_size = ceil(len(contribution_cells) / 7) * cell_size + padding * 2
    plate = cube([
        plate_x_size,
        7 * cell_size + padding * 2,
        plate_z_size
    ])

    tower_margin = (cell_size - tower_size) / 2

    objects = [plate]

    # Create github contribution towers and add to objects
    for row_number, row in enumerate(list_chunk(contribution_cells, 7)):
        for col_number, cell in enumerate(row):
            print('{} {} {} {}'.format(
                row_number, col_number, cell.date_str,
                cell.contribution_count))

            z = max_tower_z * cell.contribution_count / max_contribution_count
            cell_tower = cube([tower_size, tower_size, z])
            cell_tower = translate([
                row_number * cell_size + padding + tower_margin,
                (7 * cell_size + padding * 2) - (
                    (col_number + 1) * cell_size + padding) - tower_margin,
                plate_z_size]
            )(cell_tower)
            objects.append(cell_tower)

    # Create text plate and add to objects
    text_plate = translate([0, -text_plate_y_size, 0])(
        cube([plate_x_size, text_plate_y_size, plate_z_size]))

    objects.append(text_plate)

    _text_str = "{}'s contribution, {} - {}".format(
        github_user_name,
        contribution_cells[0].date_str,
        contribution_cells[-1].date_str
    )
    print(_text_str)
    t = text(_text_str, size=6, halign='center', valign='bottom', font='Arial')
    objects.append(translate([
        plate_x_size / 2 + padding,
        -text_plate_y_size + padding / 2,
        plate_z_size
    ])(linear_extrude(2)(t)))

    # render
    open_openscad(sum(objects))


if __name__ == '__main__':
    main()
