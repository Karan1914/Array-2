# -*- coding: utf-8 -*-
"""Problem1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sgDKwgWbssSypsu4BSxs5I3HU_mcoxTW
"""

# S30 Big N Problem #30 {Easy}

# Leetcode problem 448 Find All Numbers Disappeared in an Array
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

  n1 = set(nums)

  n = len(nums)

  l = set (range(1,n+1))

  return l-n1