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
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals, key = len)[-1] if pals else ""

Approach 1: Naive
Time: O(n^2)
Space: O(n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # (start, end) indices of the longest palindrome in s
        indices = [0, 0]

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

        for i in range(len(s)):
            l1, r1 = extend(s, i, i)
            if r1 - l1 > indices[1] - indices[0]:
                indices = l1, r1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                l2, r2 = extend(s, i, i + 1)
                if r2 - l2 > indices[1] - indices[0]:
                    indices = l2, r2

        return s[indices[0]:indices[1] + 1]


Approach 2:
Time: O(n)
Space: O(n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # '@' and '$' signs serve as sentinels appended to each end to avoid bounds
        # checking.
        t = '#'.join('@' + s + '$')
        n = len(t)
        # t[i - maxExtends[i]..i) ==
        # t[i + 1..i + maxExtends[i]]
        maxExtends = [0] * n
        center = 0

        for i in range(1, n - 1):
            rightBoundary = center + maxExtends[center]
            mirrorIndex = center - (i - center)
            maxExtends[i] = rightBoundary > i and \
                            min(rightBoundary - i, maxExtends[mirrorIndex])

            # Attempt to expand the palindrome centered at i.
            while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
                maxExtends[i] += 1

            # If a palindrome centered at i expand past `rightBoundary`, adjust
            # center based on expanded palindrome.
            if i + maxExtends[i] > rightBoundary:
                center = i

        # Find `maxExtend` and `bestCenter`.
        maxExtend, bestCenter = max((extend, i)
                                    for i, extend in enumerate(maxExtends))
        return s[(bestCenter - maxExtend) // 2:(bestCenter + maxExtend) // 2]