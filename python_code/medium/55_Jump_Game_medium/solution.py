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

# 55. Jump Game  https://leetcode.com/problems/jump-game/
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
# array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5


class Solution:
    def can_jump(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        i = mx = 0
        while i < len(nums) and i <= mx:
            if nums[i] + i >= len(nums) - 1:
                return True
            mx, i = max(mx, i + nums[i]), i + 1
        return False
