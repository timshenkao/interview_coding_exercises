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

# 503. Next Greater Element II https://leetcode.com/problems/next-greater-element-ii/
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next
# greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which
# means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9


class Solution:
    def next_greater_elements(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        stack, res = [], [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stack and (nums[stack[-1]] < nums[i]):
                    res[stack.pop()] = nums[i]
                if j == 1 and not stack:
                    break
                stack += i,
        return res
    
    def next_greater_elements2(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        n = len(nums)
        ans = [-1] * n
        stack = []  # a decreasing stack storing indices

        for i in range(n * 2):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if i < n:
                stack.append(i)
        return ans
