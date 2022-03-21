#!/usr/bin/python
"""Set up to learn a new problem"""

from datetime import datetime
import os
import re
import time

import pyperclip

import update_readme

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Get problem info
# └─────────────────────────────────────────────────────────────────────────────
today = datetime.today()
problem_title = input("Problem title: ")
problem_URL = input("URL: ")
basename = input("File basename: ")

function_signature = input("Function signature: ")
function_signature = function_signature.replace("List", "list")
function_name = re.search(r'def (.*)\(', function_signature).group(1)

done_flag = False
example_inputs, example_outputs = [], []
while not done_flag:
    example_input = input("Example input: ")
    example_output = input("Example output: ")

    if example_input == 'done' or example_output == 'done':
        done_flag = True
    else:
        example_inputs.append(example_input.replace(',', ', '))
        example_outputs.append(example_output.replace(',', ', '))

        input_symbols = example_input.split('=')[0].strip()

i, examples = 1, []
for example_input, example_output in zip(example_inputs, example_outputs):
    example = f"""    # Example {i} (Expected Output: {example_output})
    {example_input}
    print(solution_initial.{function_name}({input_symbols}))
    print(solution_preferred.{function_name}({input_symbols}))
    """
    examples.append(example)
    i += 1
examples = '\n'.join(examples)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Prepare file system
# └─────────────────────────────────────────────────────────────────────────────
root = f'Solutions/{problem_title}'
os.makedirs(root, exist_ok=True)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Prepare solution template
# └─────────────────────────────────────────────────────────────────────────────
solution_template = f'''#!/usr/bin/python
"""{problem_URL}"""

import timeit

class SolutionInitial:
    # Time / Space:
    {function_signature}
        pass

class SolutionPreferred:
    # Time / Space:
    {function_signature}
        pass


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

{examples}
    # Benchmarking
    number = 10_000
    {example_inputs[-1]}
    print(timeit.timeit(lambda: solution_initial.{function_name}({input_symbols}), number=number))
    print(timeit.timeit(lambda: solution_preferred.{function_name}({input_symbols}), number=number))
'''

filename = f'{root}/{basename}'
with open(filename, 'w+', newline='\n', encoding='utf-8') as file:
    file.write(solution_template)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Prepare README
# └─────────────────────────────────────────────────────────────────────────────
solutions_URL = f'https://github.com/pete-debiase/Comprog/blob/main/Solutions/{problem_title}'.replace(' ', '%20')
solution_URL = f'{solutions_URL}/{basename}'
readme_template = f'''### [{problem_title}]({problem_URL}) ([solutions]({solutions_URL}))

|       Date       |  Solution Time   |         Language         |
|:----------------:|:----------------:|:------------------------:|
| {today:%Y/%m/%d} | Initial solution | [Python]({solution_URL}) |
'''

with open(f'{root}/README.md', 'w+', newline='\n', encoding='utf-8') as file:
    file.write(readme_template)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Prepare Anki card
# └─────────────────────────────────────────────────────────────────────────────
Anki_HTML = f'LeetCode<br><br><a href="{problem_URL}">{problem_title}</a>'
pyperclip.copy(Anki_HTML)
print("Anki HTML on clipboard :) .\n")

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Time solution
# └─────────────────────────────────────────────────────────────────────────────
start_time = time.time()
solution_flag = input("Enter 'done' when done: ")
end_time = time.time()

delta = round(end_time - start_time)
m, s = divmod(delta, 60)
solution_time = f'{m:02d}:{s:02d}'
print(f'Solution Time: {solution_time}\n')

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Update main README
# └─────────────────────────────────────────────────────────────────────────────
done = input("Nice work :) . Press any key to quit... ")
update_readme.update_main_readme()
