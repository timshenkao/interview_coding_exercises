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

class Solution:
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stack and (nums[stack[-1]] < nums[i]): res[stack.pop()] = nums[i]
                if j == 1 and not stack: break
                stack += i,
        return res
    
Time: O(n)
Space:
O(n)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
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