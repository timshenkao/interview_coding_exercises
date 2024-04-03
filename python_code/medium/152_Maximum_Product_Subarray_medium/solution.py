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
    def maxProduct(self, nums):
        res, min_pos, max_neg, cur = -float("inf"), float("inf"), -float("inf"), 1
        for num in nums:
            cur *= num
            if cur > res: res = cur
            elif 0 < cur // min_pos > res: res = cur // min_pos
            elif 0 < cur // max_neg > res: res = cur // max_neg
            if cur == 0: min_pos, max_neg, cur = float("inf"), -float("inf"), 1
            elif max_neg < cur < 0: max_neg = cur
            elif 0 < cur < min_pos: min_pos = cur
        return res



Time:O(n)
Space: O(1)
DP 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        dpMin = nums[0]  # the minimum so far
        dpMax = nums[0]  # the maximum so far

        for i in range(1, len(nums)):
            num = nums[i]
            prevMin = dpMin  # dpMin[i - 1]
            prevMax = dpMax  # dpMax[i - 1]
            if num < 0:
                dpMin = min(prevMax * num, num)
                dpMax = max(prevMin * num, num)
            else:
                dpMin = min(prevMin * num, num)
                dpMax = max(prevMax * num, num)

            ans = max(ans, dpMax)

        return ans