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

# 88. Merge Sorted Array  https://leetcode.com/problems/merge-sorted-array/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ Do not return anything, modify nums1 in-place instead.
            Time complexity: O(n + m).
            Space complexity: O(1).
        """
        # Set pointers to the end of arrays
        i = m - 1
        j = n - 1

        # iterate from right to left
        # and write values both from nums1 and nums2 in decreasing order
        for k in range(n + m - 1, -1, -1):
            # there is nothing to copy from nums2
            # leave the remaining left part of nums1 as is
            if j < 0:
                break

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # either nothing left in the left part of nums1
            # or integer in nums2 is greater
            else:
                nums1[k] = nums2[j]
                j -= 1
