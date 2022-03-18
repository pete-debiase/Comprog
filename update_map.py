#!/usr/bin/python
"""Update LeetCode solution stats"""

import os

from airium import Airium
from jinja2 import Template

# Get list of solved problems
path = "Solutions/"
directories = [_ for _ in os.listdir(path) if os.path.isdir(path + _)]

# Massage list of solved problems into sorted dictionary
problems = [_.split('. ') for _ in directories]
problems = {int(_[0]): _[1] for _ in problems}
problems = {k: f"{k}-{v.lower().replace(' ', '-')}" for k, v in problems.items()}
problems = {k: v for k, v in sorted(problems.items(), key=lambda item: item[0])}

# Build HTML problem table (airium)
num_columns = 15
links = [f'<a href="#{problems[k]}">{k}</a>' for k in problems]
links_chunked = [links[i:i + num_columns] for i in range(0, len(links), num_columns)]
links_chunked = [_ + [''] * (num_columns - len(_)) for _ in links_chunked] # Add padding

a = Airium()
with a.table():
    for chunk in links_chunked:
        with a.tr():
            for link in chunk:
                a.td(align='center', _t=link)
table = str(a)

# Build HTML problem table (Jinja)
template = """<table>
{% for chunk in links_chunked %}
  <tr>
    {% for link in chunk %}
      <td align="center">{{ link }}</td>
    {% endfor %}
  </tr>
{% endfor %}
</table>
"""
HTML_table = Template(template).render(links_chunked=links_chunked, trim_blocks=True, lstrip_blocks=True)

with open('test2.md', 'w+', encoding='utf-8') as file:
    file.write(HTML_table)

# Insert HTML problem table into README
with open('README.md', 'r', encoding='utf-8') as file:
    data = file.read()

data = data.split('<!-- Auto-generated table -->')
data = [_.strip() for _ in data]
data[1] = f'\n<!-- Auto-generated table -->\n{table}\n<!-- Auto-generated table -->\n'

with open('README.md', 'w+', newline='\n', encoding='utf-8') as file:
    file.write('\n'.join(data) + '\n')
