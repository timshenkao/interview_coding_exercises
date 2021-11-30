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

# 1089. Duplicate Zeros https://leetcode.com/problems/duplicate-zeros/
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the
# right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.


class Solution:
    def duplicate_zeros_brute(self, arr: List[int]) -> None:
        """ Time complexity: O(n). We iterate 2 times
            Space complexity: O(n). We use additional array
        """
        i = 0
        j = 0
        temp = []
        while (i < len(arr)) and (j < len(arr)):
            if arr[i] != 0:
                temp.append(arr[i])
                i += 1
                j += 1
            else:
                temp.append(arr[i]) # i.e. 0
                temp.append(arr[i]) # i.e. 0
                i += 1
                j += 2
        for i in range(len(arr)):
            arr[i] = temp[i]

    def duplicate_zeros_optimal(self, arr: List[int]) -> None:
        """ Time complexity: O(n). We iterate 2 times
            Space complexity: O(1).
        """
        num_zeros = 0
        arr_last_index = len(arr) - 1
        flag = 0

        # Find number of zeros to duplicate
        for i in range(len(arr)):
            # there is no sense to iterate further as all the rest array's elements should be discarded
            if i > arr_last_index - num_zeros:
                break
            # the flag signals whether the last element to copy is zero and there is no space for its duplicate
            elif i == arr_last_index - num_zeros:
                flag = 1
                break
            if arr[i] == 0:
                num_zeros += 1

        # Start copying backwards from the last element
        last_to_copy = arr_last_index - num_zeros

        # We copy zero twice, and non zero once.
        for i in reversed(range(last_to_copy + 1)):
            # if we handle last_to_copy element and it's zero and flag is set,
            # i.e when we have no space to duplicate last zero element and we just copy it
            if arr[i] == 0 and flag and i == last_to_copy:
                arr[i + num_zeros] = 0
                flag = 0
            elif arr[i] == 0:
                arr[i + num_zeros] = 0
                num_zeros -= 1
                arr[i + num_zeros] = 0
            else:
                arr[i + num_zeros] = arr[i]
