#!/usr/bin/python
"""Update main README"""

import os
from airium import Airium


def build_solution_metadata_dict():
    """Build a sorted dictionary of solution metadata."""
    solutions_root, solutions = r'Solutions/', {}
    for root, dirs, files in os.walk(solutions_root):
        if root == solutions_root: continue # Skip first (parent) entry from os.walk

        problem_title = os.path.basename(root)
        problem_id, title_text = problem_title.split('. ')
        anchor = f"#{problem_id}-{title_text.lower().replace(' ', '-')}"

        problem = {'root': root,
                        'title': problem_title,
                        'anchor': anchor,
                        'files': files}
        solutions[int(problem_id)] = problem

    solutions = {k: solutions[k] for k in sorted(solutions)}
    return solutions


def generate_html_problem_table(solutions):
    """Generate HTML problem table."""
    num_columns = 15
    links = [f'''<a href="{solutions[k]['anchor']}">{k}</a>''' for k in solutions]
    links_chunked = [links[i:i + num_columns] for i in range(0, len(links), num_columns)]
    links_chunked[-1] += [''] * (num_columns - len(links_chunked[-1])) # Pad last chunk if necessary

    a = Airium()
    with a.table():
        for chunk in links_chunked:
            with a.tr():
                [a.td(align='center', _t=link) for link in chunk]
    table = str(a)

    # Insert HTML problem table into main README
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_main = file.read()

    marker = '<!-- Auto-generated table -->'
    readme_main = readme_main.split(marker)
    readme_main[1] = f'{marker}\n{table}\n{marker}'

    with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
        file.write(''.join(readme_main))


def aggregate_readmes(solutions):
    """Aggregate READMEs for each problem into main README."""
    subreadme_filenames = [solutions[k]['root'] + '/README.md' for k in solutions]

    subreadmes = []
    for filename in subreadme_filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            subreadme = file.read()
        subreadmes.append(subreadme)

    subreadmes = '\n'.join(subreadmes)

    # Insert subreadmes into main README
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_main = file.read()

    marker = '<!-- Auto-aggregated sub-READMEs -->'
    readme_main = readme_main.split(marker)
    readme_main[1] = f'{marker}\n{subreadmes}\n{marker}'

    with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
        file.write(''.join(readme_main))


if __name__ == '__main__':
    solutions = build_solution_metadata_dict()
    generate_html_problem_table(solutions)
    aggregate_readmes(solutions)
