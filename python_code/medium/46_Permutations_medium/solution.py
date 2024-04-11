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

# 46. Permutations  https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any
# order.
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


class Solution:
    def permute(self, nums):
        """ Time complexity: O(n * n!).
            Space complexity: O(n * n!).
        """
        import itertools
        return list(itertools.permutations(nums))

    def permute2(self, nums):
        """ Time complexity: O(n * n!).
            Space complexity: O(n * n!).
        """
        def dfs(path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                dfs(path)
                path.pop()
                used[i] = False

        ans = []
        used = [False] * len(nums)
        dfs([])
        return ans
