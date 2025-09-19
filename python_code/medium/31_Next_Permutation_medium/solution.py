# Copyright (c) 2021 - present, Timur Shenkao
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

from typing import List

# 31. Next Permutation https://leetcode.com/problems/next-permutation/
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1],
# [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that follows it in the sorted container.
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger
# rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


class Solution:
    def next_permutation(self, nums):
        """ Time complexity: O(N log N). We sort the array.
            Space complexity: O(1).
        """
        perm, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1
            while l < r and nums[r] <= nums[l]:
                r -= 1
            if r <= l:
                l -= 1
            else:
                # sorting
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        if not perm:
            # sorting
            nums.sort()

    def next_permutation_optimal(self, nums: List[int]) -> None:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        n = len(nums)
        # From back to front, find the first numb[i] < nums[i + 1] (find pivot)
        # TC O(n) SC O(1)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # From back to front, find the first num[j] > nums[i], swap it with nums[i].
        # exchange rightmost greater element with pivot
        # TC O(n) SC O(1)
        if i >= 0:
            for j in range(n - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        # Reverse suffix nums[i + 1..n - 1]. Suffix is the whole array if i = -1
        # TC O(n) SC O(1)
        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
