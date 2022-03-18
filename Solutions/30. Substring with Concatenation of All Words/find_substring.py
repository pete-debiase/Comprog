#!/usr/bin/python
"""https://leetcode.com/problems/substring-with-concatenation-of-all-words/"""

import timeit
from collections import Counter

class SolutionInitial:
    # Time / Space: bigger than is worth figuring out
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        start_indices = []
        n, len_word = len(words), len(words[0])
        counter_words = Counter(words)

        l, r = 0, n * len_word
        while r <= len(s):
            substrings = [s[l + i * len_word : l + (i + 1) * len_word] for i in range(n)]
            counter_substrings = Counter(substrings)
            if counter_words == counter_substrings: start_indices.append(l)
            l += 1
            r += 1

        return start_indices

class SolutionPreferred:
    # Time / Space: O(nk) / O(k) where n = len(s) - R, k = R / len(words[0])
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        start_indices = []
        num_words, word_len = len(words), len(words[0])
        counter_orig = Counter(words)
        L, R = 0, num_words * word_len

        while R <= len(s):
            l, r = L, L + word_len
            trigger = s[l:r]

            if trigger in counter_orig:
                counter_temp = Counter()
                matches_needed = len(counter_orig)

                while r <= R:
                    substring = s[l:r]
                    counter_temp[substring] += 1
                    count_temp, count_orig = counter_temp[substring], counter_orig[substring]

                    if count_temp > count_orig: break
                    if count_temp == count_orig: matches_needed -= 1
                    if matches_needed == 0: start_indices.append(L)

                    l += word_len
                    r += word_len
            L += 1
            R += 1

        return start_indices


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [0, 9])
    s, words = 'barfoothefoobarman', ['foo', 'bar']
    print(solution_initial.findSubstring(s, words))
    print(solution_preferred.findSubstring(s, words))

    # Example 2 (Expected Output: [])
    s, words = 'wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']
    print(solution_initial.findSubstring(s, words))
    print(solution_preferred.findSubstring(s, words))

    # Example 3 (Expected Output: [6, 9, 12])
    s, words = 'barfoofoobarthefoobarman', ['bar', 'foo', 'the']
    print(solution_initial.findSubstring(s, words))
    print(solution_preferred.findSubstring(s, words))

    # Benchmarking
    number = 10_000
    s, words = 'barfoofoobarthefoobarman', ['bar', 'foo', 'the']
    print(timeit.timeit(lambda: solution_initial.findSubstring(s, words), number=number))
    print(timeit.timeit(lambda: solution_preferred.findSubstring(s, words), number=number))
