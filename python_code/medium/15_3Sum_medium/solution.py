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

# 15. 3Sum https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# 0 <= nums.length <= 3000
# -10 ^ 5 <= nums[i] <= 10 ^ 5


class Solution:
    def _two_sum(self, arr: List[int], result: List[List[int]], index: int) -> None:
        """ Time complexity: O(N). We iterate through array.
            See python_code/easy/167_Two_Sum_input_array_is_sorted_easy/solution.py
            Space complexity: O(1).
        """
        left_pointer = index + 1
        right_pointer = len(arr) - 1
        # arr is sorted
        while left_pointer < right_pointer:
            temp_sum = arr[index] + arr[left_pointer] + arr[right_pointer]
            # try to increase sum
            if temp_sum < 0:
                left_pointer += 1
            # try to decrease sum
            elif temp_sum > 0:
                right_pointer -= 1
            # triplet found
            else:
                result.append([arr[index], arr[left_pointer], arr[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
                # skip the same elements
                while left_pointer < right_pointer and arr[left_pointer] == arr[left_pointer - 1]:
                    left_pointer += 1

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """ Time complexity: O(N ^ 2). We call auxiliary function N times. Auxiliary function's time complexity is O(n).
            Space complexity: O(N). We create output array. Sorting also may require space O(n).
        """
        result = list()
        # empty list
        if not nums:
            return result

        nums.sort()
        for i in range(len(nums)):
            # no sense to continue the loop as sum will be > 0
            if nums[i] > 0:
                break
            # we pass result list, so we don't create additional list every time
            if i == 0 or nums[i - 1] != nums[i]:
                self._two_sum(nums, result, i)

        return result

    def three_sum_no_sort(self, nums: List[int]) -> List[List[int]]:
        """ Time complexity: O(N ^ 2). We have 2 nested loops.
            Space complexity: O(N). We create output array, sets, dictionary.
        """
        result = set()
        no_duplicates = set()
        seen = dict()
        # empty list
        if not nums:
            return list()

        for i in range(len(nums)):
            # skip duplicate element
            if nums[i] not in no_duplicates:
                no_duplicates.add(nums[i])
                for j in range(len(nums[i+1:])):
                    target = -nums[i] - nums[j]
                    if target in seen and seen[target] == i:
                        result.add(tuple(sorted((nums[i], nums[j], target))))
                    seen[nums[j]] = i
        return [list(elem) for elem in result]

    def three_sum3(self, nums):
        """ Time complexity: O(N ^ 2).
            Space complexity: O(N).
        """
        if len(nums) < 3:
            return []
        ans = []
        nums.sort() # TC (n log n) SC O(1)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Choose nums[i] as the first number in the triplet, then search the
            # remaining numbers in [i + 1, n - 1].
            l = i + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif summ < 0:
                    l += 1
                else:
                    r -= 1
        return ans
