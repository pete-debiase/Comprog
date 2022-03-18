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

# Build HTML problem table (compact)
row, rows = [], []
cells_per_row = 15
n = len(problems)
dummy_cell = '<td>   </td>'
for i, k in enumerate(problems):
    cell = f'<td align="center"><a href="#{problems[k]}">{k}</a></td>'
    row.append(cell)
    if (i + 1) % cells_per_row == 0:
        row_HTML = '\n    '.join(row)
        rows.append(f"  <tr>\n    {row_HTML}\n  </tr>")
        row.clear()
    elif i == n - 1:
        dummy_cells = [dummy_cell] * (cells_per_row - len(row))
        row += dummy_cells
        row_HTML = '\n    '.join(row)
        rows.append(f"  <tr>\n    {row_HTML}\n  </tr>")

rows_HTML = '\n'.join(rows)
table = f'<table>\n{rows_HTML}\n</table>'

# Insert HTML problem table into README
with open('README.md', 'r', encoding='utf-8') as file:
    data = file.read()

data = data.split('<!-- Auto-generated table -->')
data = [_.strip() for _ in data]
data[1] = f'\n<!-- Auto-generated table -->\n{table}\n<!-- Auto-generated table -->\n'

with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
    file.write('\n'.join(data) + '\n')
