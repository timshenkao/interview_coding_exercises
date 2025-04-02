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

class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
        return dp2

    def numDecodings2(self, s: str) -> int:
        """Dynamic Programming
        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(s)
        # dp[i] := the number of ways to decode s[i..n)
        dp = [0] * n + [1]

        def isValid(a: str, b=None) -> bool:
            if b:
                return a == '1' or a == '2' and b < '7'
            return a != '0'

        if isValid(s[-1]):
            dp[n - 1] = 1

        for i in reversed(range(n - 1)):
            if isValid(s[i]):
                dp[i] += dp[i + 1]
            if isValid(s[i], s[i + 1]):
                dp[i] += dp[i + 2]

        return dp[0]