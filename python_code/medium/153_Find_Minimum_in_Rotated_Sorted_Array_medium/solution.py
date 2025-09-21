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

# 153. Find Minimum in Rotated Sorted Array https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the
# array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


class Solution:
    def find_min(self, nums):
        """ Time complexity: O(log n).
            Space complexity: O(1).
        """
        l = 0
        r = len(nums) - 1

        # binary search
        # In a rotated sorted array, one half (left or right of mid) is always sorted, and the minimum lies in the
        # unsorted half  or at the pivot.
        while l < r:
            m = (l + r) // 2
            # middle element is greater than right-most element, i.e. unrotated part and minimum element
            # are to the right of middle element
            if nums[m] > nums[r]:
                l = m + 1
            # vice versa
            else:
                r = m

        return nums[l]
