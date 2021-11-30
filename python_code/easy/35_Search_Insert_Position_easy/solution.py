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

# 35. Search Insert Position https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        """ Time complexity: O(log n).
            Space complexity: O(1).
        """
        # use binary search
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif left == right:
                if nums[middle] < target:
                    return middle + 1
                else:
                    return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
