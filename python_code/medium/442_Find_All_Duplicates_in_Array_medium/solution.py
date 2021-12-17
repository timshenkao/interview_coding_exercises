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

# 442. Find All Duplicates in an Array https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer
# appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
# n == nums.length
# 1 <= n <= 10 ^ 5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.

DUMMY_NUMBER = 0

class Solution:
    def find_duplicates_cycle_sort(self, nums: List[int]) -> List[int]:
        """ Time complexity: O(n).
            Space complexity: O(1) if we don't consider output list; O(n) otherwise.
        """
        result = list()
        i = 0
        is_sorted = True
        while i < len(nums):
            # either element on its place (do nothing) or ignore placeholder
            if nums[i] == i + 1 or nums[i] == DUMMY_NUMBER:
                pass
            # duplicate found, replace one occurence with placeholder
            elif nums[i] == nums[nums[i] - 1] and nums[i] != DUMMY_NUMBER:
                result.append(nums[i])
                nums[i] = DUMMY_NUMBER
            # element is not on its place, swap elements and unset flag
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                is_sorted = False
            i += 1
            # if end of the array reached and array is not sorted, start over again
            if i == len(nums) and not is_sorted:
                i = 0
                is_sorted = True
        return result

    def find_duplicates_optimal(self, nums: List[int]) -> List[int]:
        """ Time complexity: O(n).
                             See python_code/easy/448_Find_All_Numbers_Disappeared_in_an_Array_easy/solution.py
            Space complexity: O(1) if we don't consider output list; O(n) otherwise.
        """
        result = list()
        # the idea is not to sort the array but to mark positions in the original array
        # by inverting the sign (multiplying by -1)
        for i in range(len(nums)):
            # seen before
            if nums[abs(nums[i]) - 1] < 0:
                result.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
        return result
