#!/usr/bin/python
"""https://leetcode.com/problems/group-anagrams/"""

from collections import defaultdict
import timeit

class SolutionInitial:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        hashmap = {}
        for string in strings:
            string_sorted = ''.join(sorted(string))
            if string_sorted in hashmap:
                hashmap[string_sorted].append(string)
            else:
                hashmap[string_sorted] = [string]
        anagrams = list(hashmap.values())
        return anagrams

class SolutionPreferred:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for string in strings:
            string_sorted = ''.join(sorted(string))
            hashmap[string_sorted].append(string)
        anagrams = list(hashmap.values())
        return anagrams


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution_initial.groupAnagrams(strings))
    print(solution_preferred.groupAnagrams(strings))

    # Example 2 (Expected Output: [[""]])
    strings = [""]
    print(solution_initial.groupAnagrams(strings))
    print(solution_preferred.groupAnagrams(strings))

    # Example 2 (Expected Output: [["a"]])
    strings = ["a"]
    print(solution_initial.groupAnagrams(strings))
    print(solution_preferred.groupAnagrams(strings))

    # Benchmarking
    number = 10000
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(timeit.timeit(lambda: solution_initial.groupAnagrams(strings), number=number))
    print(timeit.timeit(lambda: solution_preferred.groupAnagrams(strings), number=number))
