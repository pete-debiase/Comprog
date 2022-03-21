#!/usr/bin/python
"""Update main README"""

from airium import Airium
from utilities import build_solution_metadata_dict


def generate_html_problem_table(solution_metadata):
    """Generate HTML problem table."""
    num_columns = 15
    links = [f'''<a href="{solution_metadata[k]['anchor']}">{k}</a>''' for k in solution_metadata]
    links_chunked = [links[i:i + num_columns] for i in range(0, len(links), num_columns)]
    links_chunked[-1] += [''] * (num_columns - len(links_chunked[-1])) # Pad last chunk if necessary

    a = Airium()
    with a.table():
        for chunk in links_chunked:
            with a.tr():
                [a.td(align='center', _t=link) for link in chunk]
    table = str(a)

    insert_into_main_readme('<!-- Auto-aggregated sub-READMEs -->', table)


def aggregate_readmes(solution_metadata):
    """Aggregate READMEs for each problem into main README."""
    subreadme_filenames = [solution_metadata[k]['root'] + '/README.md' for k in solution_metadata]

    subreadmes = []
    for filename in subreadme_filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            subreadme = file.read()
        subreadme = subreadme.replace('###', '####') # Change Markdown heading level for inclusion in main README
        subreadmes.append(subreadme)

    subreadmes = '\n'.join(subreadmes)
    insert_into_main_readme('<!-- Auto-aggregated sub-READMEs -->', subreadmes)


def insert_into_main_readme(marker, text_to_insert):
    """Insert `text_to_insert` into main README at position indicated by 'marker`."""
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_main = file.read()

    readme_main = readme_main.split(marker)
    readme_main[1] = f'{marker}\n{text_to_insert}\n{marker}'

    with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
        file.write(''.join(readme_main))


if __name__ == '__main__':
    solutions = build_solution_metadata_dict()
    generate_html_problem_table(solutions)
    aggregate_readmes(solutions)
