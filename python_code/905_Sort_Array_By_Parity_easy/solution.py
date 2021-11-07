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

# 905. Sort Array By Parity  https://leetcode.com/problems/sort-array-by-parity/
# Given an integer array arr, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.


class Solution:
    def sort_array_by_parity(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(n). We iterate through the list
            Space complexity: O(1).
        """
        odd_index = 0
        even_index = 0

        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                even_index += 1
            else:
                arr[odd_index], arr[even_index] = arr[even_index], arr[odd_index]
                odd_index += 1
                even_index += 1
        return arr
