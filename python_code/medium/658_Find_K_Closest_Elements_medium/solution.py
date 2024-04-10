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

# 658. Find K Closest Elements https://leetcode.com/problems/find-k-closest-elements/
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
# should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
#       |a - x| < |b - x|, or
#       |a - x| == |b - x| and a < b
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order
# -10^4 <= arr[i], x <= 10^4


class Solution:
    def find_closest_elements(self, arr, k, x):
        """ Time complexity: O(log(n−k)+k).
            Space complexity: O(k).
        """
        l = 0
        r = len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] <= arr[m + k] - x:
                r = m
            else:
                l = m + 1
        return arr[l:l + k]
