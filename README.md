# LeetCode
Many devs complain about how technical interviews are so focused on quasi-esoteric LeetCode-style data structures and algorithms problems, but personally I think it's great. How wonderful to have such a big component of interviewing be such a well-defined little minigame :) .

I also happen to LOVE quasi-esoteric little life minigames, with Japanese (language) and [stenography](dummy_link) being two of my other favorites. Therefore, my new hobby and (tentative, maybe insane) goal is to solve ALL of the LeetCode problems.

I use Anki to manage my LeetCode study schedule and ensure that I remember how to solve past problems.

Here is a link to my [LeetCode profile](https://leetcode.com/pete-debiase/)!

## Contents
<!-- MarkdownTOC levels="1,2" -->

- [Solution Stats](#solution-stats)
- [Solution Records / Notes](#solution-records--notes)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Solution Stats
|    Date    | Total Solved | Total Available |   Rank   |
|:----------:|:------------:|:---------------:|:--------:|
| 2022/01/08 |      0       |      2142       |   ???    |
| 2022/02/24 |      9       |      2184       | ≈100,000 |

## Solution Records / Notes
Note: Initial solutions marked with 😊 indicate that I was able to implement at least one solution independently.

### [1. Two Sum](https://leetcode.com/problems/two-sum/)
Solutions that are O(n^2) and O(1) in time and space, respectively, can often be improved to be O(n) in both time and space. In most cases, space is cheap, while time is precious.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/20 | Initial solution |  Python  |
| 2022/01/20 |       2:02       |  Python  |
| 2022/01/23 |       4:03       |  Python  |
| 2022/01/31 |       1:59       |  Python  |
| 2022/02/22 |      10:00+      |  Python  |

### [15. 3Sum](https://leetcode.com/problems/3sum/)
I don't like this problem :( .

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/27 | Initial solution |  Python  |
| 2022/02/28 |      10:00+      |  Python  |
| 2022/03/02 |      10:00+      |  Python  |

### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/23 | Initial solution |  Python  |
| 2022/02/24 |       3:25       |  Python  |
| 2022/02/27 |       2:05       |  Python  |

### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
First time actually implementing binary search. Was difficult.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/03/02 | Initial solution |  Python  |
| 2022/03/02 |      10:00+      |  Python  |

### [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
- Transpose + reflect approach is nice because it uses standard matrix operations.
- numpy-based solution is surprisingly slow.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/22 | Initial solution |  Python  |
| 2022/01/23 |       3:48       |  Python  |
| 2022/01/29 |   No solution    |  Python  |
| 2022/01/30 |       3:21       |  Python  |
| 2022/02/02 |       3:18       |  Python  |
| 2022/02/11 |       1:59       |  Python  |
| 2022/02/26 |       2:24       |  Python  |

### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- In Python, use `collections.defaultdict` whenever you encounter a situation like this problem (building a hashmap where it is super convenient to have a default value automatically initialized for each key encountered).

|    Date    |   Solution Time    | Language |
|:----------:|:------------------:|:--------:|
| 2022/02/28 | Initial solution 😊 |  Python  |
| 2022/02/28 |        5:19        |  Python  |

### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
Very similar to 121.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/30 | Initial solution |  Python  |
| 2022/01/31 |       2:41       |  Python  |
| 2022/02/04 |       3:01       |  Python  |
| 2022/02/22 |       5:15       |  Python  |

### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/28 | Initial solution |  Python  |
| 2022/03/01 |       5:50       |  Python  |

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- `min()` and `max()` introduce quite a bit of overhead, even when called on a collection of just two items.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/23 | Initial solution |  Python  |
| 2022/01/24 |       2:31       |  Python  |
| 2022/01/29 |       3:54       |  Python  |
| 2022/02/05 |       4:09       |  Python  |
| 2022/02/26 |       3:53       |  Python  |

### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/01 | Initial solution |  Python  |
| 2022/02/02 |       4:56       |  Python  |
| 2022/02/05 |       3:12       |  Python  |
| 2022/02/22 |   No solution    |  Python  |

### [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
Use two-pointer solution to take advantage of input array already being sorted.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/27 | Initial solution |  Python  |
| 2022/02/28 |       4:51       |  Python  |
| 2022/03/02 |       4:27       |  Python  |

### [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
A classic :) . Kind of hurts my brain though.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/03/02 | Initial solution |  Python  |
| 2022/03/02 |       5:21       |  Python  |

### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
Real-world performance can be different from what Big-O notation says. Big-O notation is most applicable for "sufficiently large input", but if n is not sufficiently large, an algorithm with worse Big-O time complexity might actually outperform one with better Big-O time complexity.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/20 | Initial solution |  Python  |
| 2022/01/22 |       1:18       |  Python  |
| 2022/01/29 |       1:29       |  Python  |
| 2022/02/22 |       1:59       |  Python  |

### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/01/27 | Initial solution |  Python  |
| 2022/01/29 |   No solution    |  Python  |
| 2022/01/30 |       3:14       |  Python  |
| 2022/02/02 |       3:30       |  Python  |
| 2022/02/11 |       6:09       |  Python  |
| 2022/02/26 |       4:25       |  Python  |

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- In Python:
    + `collections.defaultdict` is a special dictionary that automatically initializes a value the first time a key is encountered.
    + `collections.Counter` object can be used to solve this problem in one line.

|    Date    |  Solution Time   | Language |
|:----------:|:----------------:|:--------:|
| 2022/02/07 | Initial solution |  Python  |
| 2022/02/22 |       2:29       |  Python  |
