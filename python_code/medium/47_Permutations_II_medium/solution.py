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

# 47. Permutations II  https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any
# order.
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


class Solution:
    def permute_unique(self, nums):
        """ Time complexity: O(n * n!).
            Space complexity: O(n * n!).
        """
        import itertools
        dic = set()
        for p in itertools.permutations(nums):
            if p not in dic:
                dic.add(p)
        return list(dic)

    def permute_unique2(self, nums):
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
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(num)
                dfs(path)
                path.pop()
                used[i] = False

        ans = []
        used = [False] * len(nums)
        nums.sort()
        dfs([])
        return ans
