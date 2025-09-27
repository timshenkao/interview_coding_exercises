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

from math import log2

# 338. Counting Bits https://leetcode.com/problems/counting-bits/
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number
# of 1's in the binary representation of i.
# 0 <= n <= 10^5
# Follow up:
# - It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and
#       possibly in a single pass?
# - Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


class Solution:
    def countBits(self, n: int):
        """ Time complexity: O(n). iterate from 0 to `n` (n+1 iterations), and for each `i`, we perform O(1) operations
            Space complexity: O(n).
        """
        # for i > 0, the number of 1’s in i can be computed from i >> 1 (i.e., i // 2) plus the least significant bit
        # (LSB) of i.
        ans = [0] * (n + 1)
        for i in range(n + 1):
            # Dynamic Programming: re-use the result of previous subtask
            # applying mask to check the rightmost bit
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
