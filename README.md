# neetcode
[neetcode](neetcode.io) map of leetcode problems I am working through

## Map
![neetcode map](/assets/neetcode-map.png)

1. [Arrays & Hashing](##Arrays-&-Hashing)


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