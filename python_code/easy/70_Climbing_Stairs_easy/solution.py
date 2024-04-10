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

# 70. Climbing Stairs https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= n <= 45


class Solution:
    def climb_stairs(self, n: int) -> int:
        """ Time complexity: O(n log n) ???. Recursive
            Space complexity: O(n).
        """
        memo = {}
        def dfs(i):
            if i >= n:
                return 1 if i == n else 0
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)

    def climb_stairs2(self, n: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        # dp[i] := the number of ways to climb to the i-th stair
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climb_stairs3(self, n: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        prev1 = 1  # dp[i - 1]
        prev2 = 1  # dp[i - 2]
        for _ in range(2, n + 1):
            dp = prev1 + prev2
            prev2 = prev1
            prev1 = dp
        return prev1
