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
    def countSubstrings(self, s):
        res = 0
        for k in range(len(s)):
            i = j = k
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
            i , j =k , k + 1
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
        return res


DP
Time: O(n^2)
Space: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        def extendPalindromes(l: int, r: int) -> int:
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        ans = 0

        for i in range(len(s)):
            ans += extendPalindromes(i, i)
            ans += extendPalindromes(i, i + 1)

        return ans