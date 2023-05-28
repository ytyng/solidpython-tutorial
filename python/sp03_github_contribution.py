# https://github.com/ytyng
import re
from functools import cached_property

import requests
from bs4 import BeautifulSoup
from solid import *
from solid.utils import *

from github_utils import get_github_contribution_cells

from openscad_utils import convert_to_stl, open_openscad

def list_chunk(items, chunk_size):
    return (items[i:i + chunk_size] for i in range(0, len(items), chunk_size))


github_user_name = 'ytyng'

contribution_cells = get_github_contribution_cells(github_user_name)

max_contribution_count = max(max(
    cell.contribution_count for cell in contribution_cells), 1)


print(max_contribution_count)


max_height = 20

plate = cube([53 * 5, 7 * 5, 2])

open_openscad(plate)

for row_number, row in enumerate(list_chunk(contribution_cells, 7)):
    for col_number, cell in enumerate(row):
        print('{} {} {} {}'.format(row_number, col_number, cell.date_str, cell.contribution_count))

        z = max_height * cell.contribution_count / max_contribution_count
        cell_cube = cube([4, 4, z])
