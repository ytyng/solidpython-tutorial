import re
from functools import cached_property

import requests
from bs4 import BeautifulSoup


class ContributionCell:
    """
    Github contribution per day
    """
    def __init__(self, rect_element):
        self.rect_element = rect_element

    def __str__(self):
        return '{} contribution on {}'.format(
            self.contribution_count, self.date_str)

    @cached_property
    def date_str(self) -> str:
        return self.rect_element['data-date']

    @cached_property
    def contribution_level(self) -> int:
        return int(self.rect_element['data-level'])

    re_contribution_count_str = re.compile(r'(\d+) contribution')

    @cached_property
    def contribution_count(self) -> int:
        if match := self.re_contribution_count_str.search(
            self.rect_element.text
        ):
            return int(match.group(1))
        return 0


def get_github_contribution_cells(
    github_user_name: str
) -> list[ContributionCell]:
    """
    Get github contribution cells from SVG element in github user page
    """
    response = requests.get(f'https://github.com/{github_user_name}')

    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    return [
        ContributionCell(element) for element
        in soup.find_all('rect', {'class': 'ContributionCalendar-day'})
        if element.get('data-date')]
