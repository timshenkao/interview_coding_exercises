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

# 1539. Kth Missing Positive Number https://leetcode.com/problems/kth-missing-positive-number/
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

class Solution:
    def find_kth_positive(self, arr, k):
        """ Binary Search
        Time complexity: O(log n).
        Space complexity: O(1).
        """
        l = 0
        r = len(arr)
        while (l < r):
            m = (l + r) // 2
            if (arr[m] - m - 1 >= k):
                r = m
            else:
                l = m + 1

        # The k-th missing positive
        return l + k
