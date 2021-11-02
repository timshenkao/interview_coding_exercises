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

# 744. Find Smallest Letter Greater Than Target  https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Given a characters array letters that is sorted in non-decreasing order and a character target,
# return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
#     For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


class Solution:
    def next_greatest_letter(self, letters: List[str], target: str) -> str:
        """ Time complexity: O(log N).
            Straightforward solution is to iterate through array and reuires O(n).
            Space complexity: O(1).
        """
        # handle 'wrap around' situation
        if target > letters[-1]:
            return letters[0]

        left = 0
        right = len(letters) - 1
        # modification of binary search
        while left <= right:
            middle = left + (right - left) // 2
            # we found target in array; define the next element
            # skip the same elements
            if letters[middle] == target:
                while middle < len(letters) and letters[middle] == target:
                    middle += 1
                # handle 'wrap around' situation, just return the 1st element
                if middle >= len(letters):
                    return letters[0]
                # we found the element, don't iterate anymore
                break
            # search in right half
            elif letters[middle] < target:
                left = middle + 1
            # search in left half
            elif letters[middle] > target:
                right = middle - 1
        # if there is target in array, we return the next element
        # if there is no target in array, we have subtle situation:
        # return the next element if target greater than "middle" / pivot element
        # or the very "middle" / pivot element otherwise
        return letters[middle + 1] if letters[middle] <= target else letters[middle]
