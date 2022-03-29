#!/usr/bin/env python3
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
pause = input("Setup complete. Press any key to start solution timer... ")
start_time = time.time()
print(f"\nStarted at {datetime.fromtimestamp(start_time):%H:%M:%S}")
solution_flag = input("Enter solution result ('done' or 'none'): ")
end_time = time.time()

delta = round(end_time - start_time)
m, s = divmod(delta, 60)
solution_time = f'{m:d}:{s:02d}'

if solution_flag == 'done': print(f'Solution Result: Done in {solution_time} \n')
if solution_flag == 'none': print(f'Solution Result: No solution after {solution_time} \n')

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
comment = "Nice work :) ." if solution_flag == 'done' else "Keep at it :) ."
done = input(f"{comment} Press any key to update main README and quit... ")
update_readme.update_main_readme()
