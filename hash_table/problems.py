"""
Write a function item_in_common(list1, list2) that takes
two lists as input and returns True if there is at least
one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that
creates an O(n) time complexity.
"""


def items_in_common(list1: list, list2: list) -> bool:
    container = {}
    for i in list1:
        container[i] = True
    for j in list2:
        if j in container:
            return True
    return False


list1 = [1, 2, 6]
list2 = [3, 4, 5]
print(items_in_common(list1, list2))

"""
find_duplicates()
Problem: Given an array of integers nums,find all the
duplicates in the array using a hash table (dictionary).
Input:
A list of integers nums.
Output:
A list of integers representing the numbers in the input
array nums that appear more than once. If no duplicates 
are found in the input array, return an empty list [].
Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in
the input array.
"""


def find_duplicates(nums: list):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = []
    for key, count in num_counts.items():
        if count > 1:
            duplicates.append(key)
    return duplicates


dup = find_duplicates([1, 2, 3, 4, 5, 6, 6, 7, 7, 4, 3])
print(dup)


"""
HT First Non-Repeating Character ( Interview Question)
Instructions
You have been given a string of lowercase letters.
Write a function called first_non_repeating_char(string) that
finds the first non-repeating character in the given string using a
hash table (dictionary). If there is no non-repeating character in
the string, the function should return None.
For example, if the input string is "leetcode", the function should
return "l" because "l" is the first character that appears only once
in the string. Similarly, if the input string is "hello", the function
should return "h" because "h" is the first non-repeating character in
the string.
"""


def first_non_repeating_character(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None


print(first_non_repeating_character("hello"))

"""
004 HT Group Anagrams ( Interview Question)
Instructions
You have been given an array of strings, where each string may
contain only lowercase English letters. You need to write a 
function group_anagrams(strings) that groups the anagrams in
the array together using a hash table (dictionary). The function
should return a list of lists, where each inner list contains a
group of anagrams.
For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"]
the function should return [["eat","tea","ate"],["tan","nat"],["bat"]]
because the first three strings are anagrams of each other, the next two
strings are anagrams of each other, and the last string has no anagrams in the input array.
You need to implement the group_anagrams(strings) function and return a list of lists,
where each inner list contains a group of anagrams according to the above requirements.
"""


def group_anagrams(string: list):
    container = {}
    for word in string:
        sorted_word = "".join(sorted(word))
        if sorted_word in container:
            container[sorted_word].append(word)
        else:
            container[sorted_word] = [word]
    return list(container.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

"""
HT Two Sum ( Interview Question)
Instructions
two_sum()
Problem:
Given an array of integers nums and a target integer target,
find the indices of two numbers in the array that add up to the target.
The main challenge here is to implement this function in one pass
through the array. This means you should not iterate over the array
more than once. Therefore, your solution should have a time
complexity of O(n), where n is the number of elements in nums
"""


def two_sum(nums: list[int], target: int):
    container = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in container:
            return [container[complement], index]
        container[value] = index
    return []


def subarray_sum(nums: list[int], target: int) -> list[int]:
    prefix_sums = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        complement = current_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement] + 1, i]
        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = i
    return []


print(two_sum([1, 2, 3, 4, 5, 6], 4))
print(subarray_sum([1, 2, 3, 4, 5], 9))


"""
Set Remove Duplicates ( Interview Question)
Instructions
You have been given a list my_list with some duplicate values.
Your task is to write a Python program that removes all the
duplicates from the list using a set and then prints the updated list.
You need to implement a function remove_duplicates(my_list) that takes
in the input list my_list as a parameter and returns a new list with no
duplicates.
Your function should not modify the original list, instead, it should 
create a new list with unique values and return it.
Example:
Input:
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Note:
The order of the elements in the updated list may be different
from the original list, as sets are unordered.
"""


def remove_duplicates(my_list: list) -> list[int | str]:
    updated_list = list(set(my_list))
    return updated_list


print(remove_duplicates([1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]))

"""
Set Has Unique Chars ( Interview Question)
Instructions
Write a function called has_unique_chars that takes a string
as input and returns True if all the characters in the string
are unique, and False otherwise.
For example, has_unique_chars('abcdefg') should return True,
while has_unique_chars('hello') should return False
"""


def has_unique_chars(string: str):
    return len(set(string)) == len(string)


print(has_unique_chars("hello"))


"""
Set Find Pairs ( Interview Question)
Instructions
You are given two lists of integers, arr1 and arr2, and a target
integer value, target. Your task is to find all pairs of numbers
(one from arr1 and one from arr2) whose sum equals target.
Write a function called find_pairs that takes in three arguments:
arr1, arr2, and target, and returns a list of all such pairs.
Assume that each array does not contain duplicate values.
The tests for this exercise assume that arr1 is the list being
converted to a set.
Input
Your function should take in the following inputs:
arr1: a list of integers
arr2: a list of integers
target: an integer
Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.
Example 1:
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9
pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Expected output: [(3, 6)]
# Explanation: There's only one pair that adds up to 9: 3
# from arr1 and 6 from arr2.
"""


def find_pairs(arr1: list[int], arr2: list[int], target: int) -> list[tuple[int, int]]:
    set1 = set(arr1)
    my_list = []
    for num in arr2:
        comlement = target - num
        if comlement in set1:
            my_list.append((comlement, num))
    return my_list


arr1 = [0, 1, 2]
arr2 = [7, 8, 9]
target = 10

print(find_pairs(arr1, arr2, target))

"""
Set Longest Consecutive Sequence ( Interview Question)
Instructions
Given an unsorted array of integers, write a function that finds the
length of the  longest_consecutive_sequence (i.e., sequence of integers
in which each element is one greater than the previous element).
Use sets to optimize the runtime of your solution.
Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence
in nums.
Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input 
array is [4, 3, 2, 1], and its length is 4.
"""


def longest_consecutive_sequence(nums: list[int]) -> list[int]:
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums=nums))

"""
Find Common Elements Between Two Arrays
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively.
Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

 

Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]
"""


class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = 0
        for num in nums1:
            if num in set2:
                answer1 += 1
        answer2 = 0
        for num in nums2:
            if num in set1:
                answer2 += 1
        return [answer1, answer2]


sol = Solution()
print(sol.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))

"""
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the
total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count
