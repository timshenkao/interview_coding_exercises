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

from typing import List, Set

# 16. 3Sum Closest  https://leetcode.com/problems/3sum-closest/
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10 ^ 4 <= target <= 10 ^ 4


class Solution:
    def _two_sum(self, arr: List[int], target: int, closest_sum: int, index: int) -> int:
        """ Time complexity: O(N). We iterate through array.
            See python_code/easy/167_Two_Sum_input_array_is_sorted_easy/solution.py
            Space complexity: O(1).
        """
        left_pointer = index + 1
        right_pointer = len(arr) - 1
        # arr is sorted
        while left_pointer < right_pointer and closest_sum != target:
            temp_sum = arr[index] + arr[left_pointer] + arr[right_pointer]
            # try to increase sum
            if temp_sum < target:
                left_pointer += 1
            # try to decrease sum
            elif temp_sum > target:
                right_pointer -= 1
            # triplet found; after updating closest sum, loop exits on the next iteration
            else:
                pass
            # update closest sum
            closest_sum = min(closest_sum, temp_sum, key=lambda x: abs(target - x))
        return closest_sum

    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """ Time complexity: O(N ^ 2).
            Space complexity: O(1) if we use in-place sorting like selection sort; O(n) otherwise
        """
        # initialize with sum of first elements
        closest_sum = nums[0] + nums[1] + nums[2]
        # there is 3 elements at least
        if len(nums) == 3:
            return closest_sum

        nums.sort()
        for i in range(len(nums)):
            # closest sum can decrease only with every function call
            closest_sum = self._two_sum(nums, target, closest_sum, i)

        return closest_sum
