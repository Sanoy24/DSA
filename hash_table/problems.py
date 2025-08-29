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
