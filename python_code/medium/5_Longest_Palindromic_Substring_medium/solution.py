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

from typing import Tuple

# 5. Longest Palindromic Substring https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longest_palindrome(self, s: str) -> str:
        """ Time complexity: O(n^2).
            Space complexity: O(n).
        """
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals, key=len)[-1] if pals else ""

    def longest_palindrome2(self, s: str) -> str:
        """ Time complexity: O(n^2).
            Space complexity: O(n).
        """
        def extend(s: str, i: int, j: int) -> Tuple[int, int]:
            """
            Returns the (start, end) indices of the longest palindrome extended from
            the substring s[i..j].
            """
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return i + 1, j - 1

        if not s:
            return ""
        # (start, end) indices of the longest palindrome in s
        indices = [0, 0]
        for i in range(len(s)):
            l1, r1 = extend(s, i, i)
            if r1 - l1 > indices[1] - indices[0]:
                indices = l1, r1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                l2, r2 = extend(s, i, i + 1)
                if r2 - l2 > indices[1] - indices[0]:
                    indices = l2, r2
        return s[indices[0]:indices[1] + 1]

    def longest_palindrome3(self, s: str) -> str:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        # '@' and '$' signs serve as sentinels appended to each end to avoid bounds
        # checking.
        t = '#'.join('@' + s + '$')
        n = len(t)
        # t[i - max_extends[i]..i) ==
        # t[i + 1..i + max_extends[i]]
        max_extends = [0] * n
        center = 0
        for i in range(1, n - 1):
            right_boundary = center + max_extends[center]
            mirror_index = center - (i - center)
            max_extends[i] = right_boundary > i and min(right_boundary - i, max_extends[mirror_index])

            # Attempt to expand the palindrome centered at i.
            while t[i + 1 + max_extends[i]] == t[i - 1 - max_extends[i]]:
                max_extends[i] += 1

            # If a palindrome centered at i expand past `right_boundary`, adjust
            # center based on expanded palindrome.
            if i + max_extends[i] > right_boundary:
                center = i

        # Find `max_extend` and `best_center`.
        max_extend, best_center = max((extend, i) for i, extend in enumerate(max_extends))
        return s[(best_center - max_extend) // 2:(best_center + max_extend) // 2]
