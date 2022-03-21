#!/usr/bin/python
"""Helper utilities.py"""

import os


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
