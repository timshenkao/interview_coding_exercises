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

# 154. Find Minimum in Rotated Sorted Array II https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
# nums = [0,1,4,4,5,6,7] might become:
#   [4,5,6,7,0,1,4] if it was rotated 4 times.
#   [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]].
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
# You must decrease the overall operation steps as much as possible.
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
# This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates.
# Would this affect the runtime complexity? How and why?


class Solution:
    def find_min(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        l, r, res = 0, len(nums) - 1, nums and nums[0]
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r, res = mid - 1, min(res, nums[mid])
        return res

    def find_min2(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == nums[r]:
                r -= 1
            elif nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
