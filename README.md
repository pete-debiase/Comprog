# LeetCode
Many devs bemoan the fact that technical interviews are so focused on quasi-esoteric LeetCode-style data structures and algorithms coding problems, but I think it's great. How wonderful to have such a big component of interviewing be such a well-defined little minigame :) .

Also, I LOVE quasi-esoteric pursuits like LeetCode, with Japanese (language) and stenography being two of my other favorites!

My (tentative, maybe insane) goal is to complete ALL of the LeetCode problems (2142 as of 2022/01/18).

Here is a link to my [LeetCode profile](https://leetcode.com/pete-debiase/)!

## Notes / Solution Records
### Contents
<!-- MarkdownTOC -->

- [1. Two Sum](#1-two-sum)
- [48. Rotate Image](#48-rotate-image)
- [53. Maximum Subarray](#53-maximum-subarray)
- [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
- [217. Contains Duplicate](#217-contains-duplicate)
- [238. Product of Array Except Self](#238-product-of-array-except-self)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

#### [1. Two Sum](https://leetcode.com/problems/two-sum/)
Solutions that are O(n^2) and O(1) in time and space, respectively, can often be improved to be O(n) in both time and space. In most cases, space is cheap, while time is precious.

1. 2022-01-20 – Initial solution (Python)
2. 2022-01-20 – Solution time = 2:02 (Python)
3. 2022-01-23 – Solution time = 4:03 (Python)

#### [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
- Transpose + reflect approach is nice because it uses standard matrix operations.
- numpy-based solution is surprisingly slow.

1. 2022-01-22 – Initial solution (Python)
2. 2022-01-23 – Solution time = 3:48 (Python)
3. 2022-01-29 – No solution (Python)
4. 2022-01-30 – Solution time = 3:21 (Python)

#### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
Very similar to 121.

1. 2022-01-30 – Initial solution (Python)

#### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- `min()` and `max()` introduce quite a bit of overhead, even when called on a collection of just two items.

1. 2022-01-23 – Initial solution (Python)
2. 2022-01-24 – Solution time = 2:31 (Python)
3. 2022-01-29 – Solution time = 3:54 (Python)

#### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
Real-world performance can be different from what Big-O notation says. Big-O notation is most applicable for "sufficiently large input", but if n is not sufficiently large, an algorithm with worse Big-O time complexity might actually outperform one with better Big-O time complexity.

1. 2022-01-20 – Initial solution (Python)
2. 2022-01-22 – Solution time = 1:18 (Python)
3. 2022-01-29 – Solution time = 1:29 (Python)

#### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

1. 2022-01-27 – Initial solution (Python)
2. 2022-01-29 – No solution (Python)
3. 2022-01-30 – Solution time = 3:14 (Python)
