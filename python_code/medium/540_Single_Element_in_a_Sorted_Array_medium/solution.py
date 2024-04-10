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

# 540. Single Element in a Sorted Array https://leetcode.com/problems/single-element-in-a-sorted-array/
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
# element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5


class Solution:
    def single_non_duplicate(self, nums):
        """ Time complexity: O(logn).
            Space complexity: O(1).
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 <len(nums) and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

    def single_non_duplicate2(self, nums):
        """ Time complexity: O(logn).
            Space complexity: O(1).
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[l]
