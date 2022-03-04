#!/usr/bin/python
"""Update LeetCode solution stats"""

import os

# Get list of solved problems
path = "Solutions/"
directories = [_ for _ in os.listdir(path) if os.path.isdir(path + _)]

# Massage list of solved problems into sorted dictionary
problems = [_.split('. ') for _ in directories]
problems = {int(_[0]): _[1] for _ in problems}
problems = {k: f"{k}-{v.lower().replace(' ', '-')}" for k, v in problems.items()}
problems = {k: v for k, v in sorted(problems.items(), key=lambda item: item[0])}

# Build HTML table
row = []
rows = []
cells_per_row = 15
max_problem = max(problems.keys())
dummy_cell = '<td>   </td>'
for i in range(1, max_problem + 1):
    if i in problems:
        cell = f'<td align="center"><a href="#{problems[i]}">{i}</a></td>'
    else:
        cell = dummy_cell
    row.append(cell)
    if i % cells_per_row == 0:
        row_HTML = f"    <tr>{''.join(row)}</tr>"
        if 'a href' in row_HTML:
            rows.append(row_HTML)
        row = []
    elif i == max_problem:
        if 'a href' in ''.join(row):
            dummy_cells = [dummy_cell] * (cells_per_row - len(row))
            row += dummy_cells
            row_HTML = f"    <tr>{''.join(row)}</tr>"
            rows.append(row_HTML)

rows_HTML = '\n'.join(rows)
table = f'<table>\n{rows_HTML}\n</table>'

# Update README with table
with open('README.md', 'r', encoding='utf-8') as file:
    data = file.read()

data = data.split('<!-- Auto-generated content -->')
data = [_.strip() for _ in data]
data[1] = f'\n<!-- Auto-generated content -->\n{table}\n<!-- Auto-generated content -->\n'

with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
    file.write('\n'.join(data) + '\n')
