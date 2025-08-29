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


print(two_sum([1, 2, 3, 4, 5, 6], 4))
