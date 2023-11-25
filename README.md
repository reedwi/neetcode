# neetcode
[neetcode](neetcode.io) map of leetcode problems I am working through

## Map
![neetcode map](/assets/neetcode-map.png)

1. [Arrays & Hashing](##Arrays-&-Hashing)
2. [Two Pointers](##Two-Pointers)


## Arrays & Hashing
### Contains Duplicate
[leetcode](https://leetcode.com/problems/contains-duplicate/)
```
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
```

My first approach using built-in python functionality to complete. This will work fine, but is not super memory efficient as I am creating a set on top of the list that is passed. It is very fast though.
```python
from typing import List
class Solution:
    def contains_duplicate_set(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False
```

Second approach uses a set that I add to as I iterate. If the number is in the set then we know it is a duplicate, if not in the set we add the number to the set
```python
    def contains_duplicate_hashset(self, nums: List[int]) -> bool:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums.add(num)
```

### Valid Anagram
[leetcode](https://leetcode.com/problems/valid-anagram/)
```
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
```

My first approach again leverages python built-in features. This clears, but will be a better way using a different approach
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_t == sorted_s:
            return True
```

Second approach uses a hash to count the occurences of characters and then checks to see if the characters counts are equakl between the 2
```python
    def isAnagramHash(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            char_count[char] -= 1

        for count in char_count.values():
            if count != 0:
                return False
        
        return True
```
Third approach uses a built-in python object I was not familiar with "Counter". The Counter class will essentially do a very similar implementation to what I am doing in the prior attempt. It will make keys of all the items in the iterable and then count how many times they appear as the value of the dict.
```python
    def isAnagramCounter(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if s_counter == t_counter:
            return True
```

### Two Sum
[leetcode](https://leetcode.com/problems/two-sum/)
```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
```
Using a hash map to collect the value and index of numbers. We look for the number needed to get to the target number. If the number needed is in our map, then we return the current index and get the index from the hash map of the number needed
```python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i, num in enumerate(nums):
            num_to_search = target - num
            if num_to_search in seen_map:
                return [i, seen_map[num_to_search]]
            seen_map[num] = i
```
### Group Anagrams
[leetcode](https://leetcode.com/problems/group-anagrams/)
```
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
```
First pass is taking similar approach to the first anagram problem. Keeping a seen map, but instead of a singular value with a key, it is now a list of values with the key
```python
from typing import List
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = defaultdict(list)
        for str in strs:
            sorted_str = tuple(sorted(str))
            seen_map[sorted_str].append(str)
        return list(seen_map.values())

```

### Top K Frequent Elements
[leetcode](https://leetcode.com/problems/top-k-frequent-elements/)
```
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
```
First go that is bvery efficient is a full python built-in way using Counter and OrderedDict. It works well
```python
from typing import List
from collections import Counter, OrderedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = OrderedDict(counter.most_common(k))
        return list(sorted_counter.keys())
```
A way that shows actual understanding of what's going on underneath, but would go full Python in an actual implementation. This uses a hash map again to get the values, then sorts and gets the necessary values
```python
    def topKFrequentForce(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        sorted_values = sorted(count_map.values(), reverse=True)
        target_counts = sorted_values[0:k]
        return_list = []
        for num, count in count_map.items():
            if count in target_counts:
                return_list.append(num)
                target_counts.remove(count)
                if not target_counts:
                    return return_list
```
### Product of Array Except Self
[leetcode](https://leetcode.com/problems/product-of-array-except-self/)
```
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```
Used a prefix and postfix solution. Loops through and calucalte the product of all elements to the left of i.

Then loop through in reverse and calculate the product of all elements to the right of i and multiply by the value retrieved from left of i.
```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer
```

### Valid Sudoku
```
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```
Took me awhile, but figured out how to do in one sweep. Used a defaultdict with a set as a value.
1. Iterate through every number
2. If not a number continue on
3. Based on the number and position, check to see if it is in my dictionary. I.e. on position (0, 2) for rows it will look for a dict key of 0 and check to see if the set contains the num. Does the same for columns
4. Then determine the square it is in using floor division. Can generate square it is in and do the same set calculation

```python
from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if board[row][col] == '.':
                    continue

                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)

                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)

                square_section = (row // 3, col // 3)
                if num in squares[square_section]:
                    return False
                else:
                    squares[square_section].add(num)
        return True
```
### Encode and Decode Strings
```
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
```

```python
    def encode(self, strs):
        encoded = ''
        for s in strs:
            if s != ':':
                encoded += s + ':;'
            else:
                encoded += ':' + s + ':;'
        return encoded


    def decode(self, str):
        # write your code here
        result = []
        buf = ''
        skip = False

        for s in range(len(str)):
            if skip:
                skip = False
                continue

            if str[s] != ':':
                buf += str[s]
            elif str[s] == ':' and str[s+1] == ';':
                result.append(buf)
                buf = ''
                skip = True
            elif str[s] == ':' and str[s+1] == ':':
                buf += ':'
                skip = True
        return result
```

### Longest Consecutive Sequence
[leetcode](https://leetcode.com/problems/longest-consecutive-sequence/)
```
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```
1. Made a set to remove duplicates. 
2. Converted back to a list so it could then be ordered. 
3. Loop through list and check to see if the next value in the list is equal to the current value + 1. 
4. if it is then add to current_count, if not mark it to end the current streak
5. If current_count > longest streak, then set longest to current_count
6. If it is marked to end then set current_count back to 1

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums:
            longest = 1
        else:
            longest = 0
        current_count = 1
        end = False

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                current_count += 1
            else:
                end = True

            if current_count > longest:
                longest = current_count
            
            if end:
                current_count = 1
                end = False
        return longest
```

## Two Pointers
### Valid Palindrome
[leetcode](https://leetcode.com/problems/valid-palindrome/)
```
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

### Two Sum Input Array is Sorted
```
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
```

### 3 Sum
```
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

### Container with Most Water
```
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
```

### Trapping Rain Water
```
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
```