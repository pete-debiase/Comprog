#!/usr/bin/python
"""URL"""

import timeit

class SolutionInitial:
    # Time / Space Complexity:
    def function(self) -> None:
        pass

class SolutionPreferred:
    # Time / Space Complexity:
    def function(self) -> None:
        pass


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: )
    my_input = None
    print(solution_initial.function(my_input))
    print(solution_preferred.function(my_input))

    # Benchmarking
    number = 10_000
    my_input = None
    print(timeit.timeit(lambda: solution_initial.function(my_input), number=number))
    print(timeit.timeit(lambda: solution_preferred.function(my_input), number=number))
