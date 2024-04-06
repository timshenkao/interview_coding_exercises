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

# 647. Palindromic Substrings https://leetcode.com/problems/palindromic-substrings/
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


class Solution:
    def count_sub_strings(self, s):
        """ Time complexity: O(N ^ 2).
            Space complexity: O(1).
        """
        res = 0
        for k in range(len(s)):
            i = j = k
            while 0 <= i and j < len(s):
                if s[i] == s[j]:
                    res += 1
                else:
                    break
                i, j = i - 1, j + 1

            i, j = k, k + 1

            while 0 <= i and j < len(s):
                if s[i] == s[j]:
                    res += 1
                else:
                    break
                i, j = i - 1, j + 1
        return res

    def count_sub_strings2(self, s: str) -> int:
        """ Time complexity: O(N ^ 2). The same approach but with subroutine.
            Space complexity: O(1).
        """
        def _check_palindromes(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += _check_palindromes(i, i)
            ans += _check_palindromes(i, i + 1)
        return ans
