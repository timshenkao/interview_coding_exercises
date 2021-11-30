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

from math import inf
from typing import List

# 628. Maximum Product of Three Numbers  https://leetcode.com/problems/maximum-product-of-three-numbers/
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


class Solution:
    # other possible approaches:
    #   a) sort array and use elements nums[0], nums[1], nums[n-3], nums[n-2], nums[n-1]
    #       The best possible time complexity: O(n log n)  (depends on sorting algorithm)
    #       The best possible space complexity: O(1)   (depends on sorting algorithm, if it's in-place)
    #   b) put array's elements into heap and use 2 smallest and 3 largest elements
    #       The best possible time complexity: O(n log n)
    #       The best possible space complexity: O(n)

    def maximum_product(self, nums: List[int]) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        # we keep 2 smallest elements as they can be both negative with large absolute values
        mins = [inf, inf]
        # we keep 3 largest elements as they can be positive
        maxes = [-inf, -inf, -inf]
        # print('1 maxes', maxes)
        for num in nums:
            # iterate through array, update maximum values
            if num > maxes[2]:
                maxes[0], maxes[1], maxes[2] = maxes[1], maxes[2], num
            elif num > maxes[1]:
                maxes[0], maxes[1] = maxes[1], num
            elif num > maxes[0]:
                maxes[0] = num
            # iterate through array, update minimum values
            if num < mins[0]:
                mins[0], mins[1] = num, mins[0]
            elif num < mins[1]:
                mins[1] = num
            # print('2 maxes', maxes)
        # largest product is either:
        #       product of 3 largest elements in array
        #       product of 1 largest element in array and 2 smallest elements (they are both negative)
        return max(maxes[0] * maxes[1] * maxes[2], mins[0] * mins[1] * maxes[2])
