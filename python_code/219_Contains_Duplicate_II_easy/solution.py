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

# 219. Contains Duplicate II https://leetcode.com/problems/contains-duplicate-ii/
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(min(n, k)). The extra space required depends on the number of items stored in the hash
                              table, which is the size of the sliding window, min(n,k).
        """
        # if there is less than 2 elements, then there is no duplicates
        if len(nums) < 2:
            return False

        # keep dictionary as a counter
        table = dict()
        for i in range(len(nums)):
            # keep list of indices per each value
            _ = table.setdefault(nums[i], [])
            table[nums[i]].append(i)
            # return immediately if 2 last indices, i.e. closest indices, within distance k
            if len(table[nums[i]]) > 1 and table[nums[i]][-1] - table[nums[i]][-2] <= k:
                return True
        return False

    def contains_nearby_duplicate_optimized(self, nums: List[int], k: int) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(min(n, k)). The extra space required depends on the number of items stored in the hash
                              table, which is the size of the sliding window, min(n,k).
        """
        # if there is less than 2 elements, then there is no duplicates
        if len(nums) < 2:
            return False
        # keep dictionary as a counter
        table = dict()
        for i in range(len(nums)):
            # keep just 1 (last) indice per value
            if nums[i] in table:
                if i - table[nums[i]] <= k:
                    return True
            table[nums[i]] = i
        return False
