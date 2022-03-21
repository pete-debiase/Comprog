#!/usr/bin/python
"""Review a previously solved LeetCode problem"""

from datetime import datetime
import time

import update_readme
from utilities import build_solution_metadata_dict

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Initialization
# └─────────────────────────────────────────────────────────────────────────────
solution_metadata = build_solution_metadata_dict()
problem = int(input("Problem ID: "))
root_dir = solution_metadata[problem]['root']

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Create new Python file for review code
# └─────────────────────────────────────────────────────────────────────────────
# Prepare filename
python_files = [file for file in solution_metadata[problem]['files'] if '.py' in file]
basename = min(python_files)

today = datetime.today()
filename = basename.replace('.py', f'_{today:%Y-%m-%d}.py')

# Get boilerplate code from most recent solution
recentest_solution = f'{root_dir}/{python_files[-1]}'
with open(recentest_solution, 'r', encoding='utf-8') as file:
    code = [line.strip() for line in file]

heading = '\n'.join(code[:2])
function_signature = [line for line in code if 'def' in line][0]

boilerplate = f'{heading}\n\nclass Solution:\n    {function_signature}\n        pass\n'

with open(f'{root_dir}/{filename}', 'w+', newline='\n', encoding='utf-8') as file:
    file.write(boilerplate)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Time solution
# └─────────────────────────────────────────────────────────────────────────────
start_time = time.time()
solution_flag = input("Enter solution result ('done' or 'none'): ")
end_time = time.time()

if solution_flag == 'none': solution_time = 'No solution'
else:
    delta = round(end_time - start_time)
    m, s = divmod(delta, 60)
    solution_time = f'{m:02d}:{s:02d}'
print(f'Solution Time: {solution_time}\n')

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Update problem README
# └─────────────────────────────────────────────────────────────────────────────
date = f'{today:%Y/%m/%d}'
problem_title = solution_metadata[problem]['title'].replace(' ', '%20')
URL = f'https://github.com/pete-debiase/Comprog/blob/main/Solutions/{problem_title}/{filename}'

table_entry = f'|{today:%Y/%m/%d}|{solution_time}|[Python]({URL})|'

with open(f'{root_dir}/README.md', 'a', encoding='utf-8') as file:
    file.write(table_entry + '\n')

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Update main README
# └─────────────────────────────────────────────────────────────────────────────
done = input("Nice work :) . Press any key to quit... ")
update_readme.update_main_readme()
