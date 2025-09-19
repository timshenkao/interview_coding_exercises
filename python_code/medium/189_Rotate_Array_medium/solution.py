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

# 189. Rotate Array https://leetcode.com/problems/rotate-array/
# Given an integer array nums, rotate the array to the right by k steps, where
# k is NON-negative.
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

class Solution:
    def reverse(self, arr, start, end):
        """Helper function to reverse elements in nums from start to end indices.
            TC O(N)
            SC O(1)
        """
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        n = len(nums)
        if n <= 1 or k == 0:
            return  # No rotation needed for length <= 1 or k = 0

        # Normalize k to handle cases where k > n
        # new_k < n
        new_k = k % n

        # Each element is swapped at most twice (once in full reverse, once in partial reverse).
        # Reverse the entire array
        # last k elements take place in the beginning of array in reverse order
        self.reverse(nums, 0, n - 1)
        # Reverse the first k elements
        # last k elements take place in the beginning of array in correct order
        self.reverse(nums, 0, new_k - 1)
        # Reverse the last n - k elements
        self.reverse(nums, new_k, n - 1)
