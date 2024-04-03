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
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        def dfs(l, r, cnt):
            if (l, r, cnt) in memo:
                return memo[(l, r, cnt)]
            if l >= r:
                return True
            elif s[l] != s[r]:
                cnt += 1
                if cnt > 1:
                    memo[(l, r, cnt)] = False
                    return False
                elif (s[l + 1] == s[r] and dfs(l + 1, r, cnt + 1)) or (s[l] == s[r - 1] and dfs(l, r - 1, cnt + 1)):
                    memo[(l, r, cnt)] = True
                    return True
                else:
                    memo[(l, r, cnt)] = False
                    return False
            else:
                memo[(l, r, cnt)] = dfs(l + 1, r - 1, cnt)
                return memo[(l, r, cnt)]
        return dfs(0, len(s) - 1, 0)


Time: O(n)
Space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindrome(l: int, r: int) -> bool:
            return all(s[i] == s[r - i + l] for i in range(l, (l + r) // 2 + 1))

        n = len(s)

        for i in range(n // 2):
            if s[i] != s[~i]:
                return validPalindrome(i + 1, n - 1 - i) or validPalindrome(i, n - 2 - i)

        return True