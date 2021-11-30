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

# 66. Plus One https://leetcode.com/problems/plus-one/
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit
# of the integer. The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        """ Time complexity: O(n). We iterate through the array once.
            Space complexity: O(n). In the worst scenario, we would need to allocate an intermediate space to hold
            the result, which contains the N+1 elements.
        """
        transfer = 1
        for i in reversed(range(len(digits))):
            temp = digits[i] + transfer
            if temp >= 10:
                digits[i] = temp - 10
                transfer = 1
            else:
                digits[i] = temp
                transfer = 0
        if transfer:
            # new list allocation under the hood
            digits.insert(0, 1)
        return digits

    def plus_one_in_place(self, digits: List[int]) -> List[int]:
        """ Time complexity: O(n). We iterate through the array once.
            Space complexity: O(1). We append 1 to the end of the array and then iterate backwards to move 1 t
                                    to the first position
        """
        transfer = 1
        for i in reversed(range(len(digits))):
            temp = digits[i] + transfer
            if temp >= 10:
                digits[i] = temp - 10
                transfer = 1
            else:
                digits[i] = temp
                transfer = 0
        if transfer:
            # NO new list allocation under the hood
            digits.append(1)
            i = len(digits) - 1
            while i > 0:
                digits[i], digits[i - 1] = digits[i - 1], digits[i]
                i -= 1
        return digits
