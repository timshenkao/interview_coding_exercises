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

# 1060. Missing Element in Sorted Array  https://leetcode.com/problems/missing-element-in-sorted-array/
# Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also
# an integer k, return the kth missing number starting from the leftmost number of the array.
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^7
# nums is sorted in ascending order, and all the elements are unique.
# 1 <= k <= 10^8


class Solution:
    def missing_element(self, nums: List[int], k: int) -> int:
        """ Time complexity: O(log N). Binary Search
            Space complexity: O(1).
        """
        cur = nums[0]
        for num in nums[1:]:
            if num - cur - 1 >= k:
                break
            else:
                k -= num - cur - 1
            cur = num
        return cur + k
