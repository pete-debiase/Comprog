# LeetCode
Many devs complain about how technical interviews are so focused on quasi-esoteric LeetCode-style data structures and algorithms problems, but personally I think it's great. How wonderful to have such a big component of interviewing be such a well-defined little minigame :) .

I also happen to LOVE quasi-esoteric little life minigames, with Japanese (language) and [stenography](dummy_link) being two of my other favorites. Therefore, my new hobby and (tentative, maybe insane) goal is to solve ALL of the LeetCode problems.

I use Anki to manage my LeetCode study schedule and ensure that I remember how to solve past problems.

Here is a link to my [LeetCode profile](https://leetcode.com/pete-debiase/)!

## Contents
<!-- MarkdownTOC levels="1,2" -->

- [Solution Records](#solution-records)
- [Solution Details / Notes](#solution-details--notes)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Solution Records
|    Date     | Total Problems Solved | Total Problems Available |
|:-----------:|:---------------------:|:------------------------:|
| 2022/01/08  |           0           |           2142           |
| 2022/02/24  |           9           |           2184           |

## Solution Details / Notes
### [1. Two Sum](https://leetcode.com/problems/two-sum/)
Solutions that are O(n^2) and O(1) in time and space, respectively, can often be improved to be O(n) in both time and space. In most cases, space is cheap, while time is precious.

1. 2022-01-20 – Initial solution (Python)
2. 2022-01-20 – Solution time = 2:02 (Python)
3. 2022-01-23 – Solution time = 4:03 (Python)
4. 2022-01-31 – Solution time = 1:59 (Python)
5. 2022-02-22 – Solution time = 10:00+ (Python)

### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

1. 2022-02-23 – Initial solution (Python)
2. 2022-02-24 – Solution time = 3:25 (Python)


### [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
- Transpose + reflect approach is nice because it uses standard matrix operations.
- numpy-based solution is surprisingly slow.

1. 2022-01-22 – Initial solution (Python)
2. 2022-01-23 – Solution time = 3:48 (Python)
3. 2022-01-29 – No solution (Python)
4. 2022-01-30 – Solution time = 3:21 (Python)
5. 2022-02-02 – Solution time = 3:18 (Python)
6. 2022-02-11 – Solution time = 1:59 (Python)

### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
Very similar to 121.

1. 2022-01-30 – Initial solution (Python)
2. 2022-01-31 – Solution time = 2:41 (Python)
3. 2022-02-04 – Solution time = 3:01 (Python)
4. 2022-02-22 – Solution time = 5:15 (Python)

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- `min()` and `max()` introduce quite a bit of overhead, even when called on a collection of just two items.

1. 2022-01-23 – Initial solution (Python)
2. 2022-01-24 – Solution time = 2:31 (Python)
3. 2022-01-29 – Solution time = 3:54 (Python)
4. 2022-02-05 – Solution time = 4:09 (Python)

### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

1. 2022-02-01 – Initial solution (Python)
2. 2022-02-02 – Solution time = 4:56 (Python)
3. 2022-02-05 – Solution time = 3:12 (Python)
4. 2022/02/22 – No solution (Python)

### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
Real-world performance can be different from what Big-O notation says. Big-O notation is most applicable for "sufficiently large input", but if n is not sufficiently large, an algorithm with worse Big-O time complexity might actually outperform one with better Big-O time complexity.

1. 2022-01-20 – Initial solution (Python)
2. 2022-01-22 – Solution time = 1:18 (Python)
3. 2022-01-29 – Solution time = 1:29 (Python)
4. 2022-02-22 – Solution time = 1:59 (Python)

### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

1. 2022-01-27 – Initial solution (Python)
2. 2022-01-29 – No solution (Python)
3. 2022-01-30 – Solution time = 3:14 (Python)
4. 2022-02-02 – Solution time = 3:30 (Python)
5. 2022-02-11 – Solution time = 6:09 (Python)

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- In Python:
    + `collections.defaultdict` is a special dictionary that automatically initializes a value the first time a key is encountered.
    + `collections.Counter` object can be used to solve this problem in one line.

1. 2022-02-07 – Initial solution (Python)
2. 2022-02-22 – Solution time = 2:29 (Python)
