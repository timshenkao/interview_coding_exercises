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

# 28. Implement strStr()  https://leetcode.com/problems/implement-strstr/
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
# and Java's indexOf().
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.


class Solution:
    def _find_brute_force(self, t: str, s: str) -> int:
        """ Time complexity: O(n * m). This solution gives "Time Limit Exceeded" when string is 50 000 characters long
                             and pattern is 10 000 long.
            Space complexity: O(1).
        """
        n, m = len(t), len(s)
        # try every index within t
        for i in range(n - m + 1):
            k=0
            # iterate through pattern string aka "needle"
            while k < m and t[i + k] == s[k]:
                # kth character of pattern matches
                k += 1
            # if we reached the end of pattern, substring t[i: i + m] matches pattern
            if k == m:
                return i
        # nothing found
        return -1

    def _find_boyer_moore(self, t: str, s: str) -> int:
        """ Time complexity: O(n * m). It's worst case scenario; algorithm is much faster in reality as big portions
                             of t are skipped
        Looking-Glass Heuristic: When testing a possible placement of s against t, begin the comparisons from the end
                                 of s and move backward to the front of s.
        Character-Jump Heuristic: During the testing of a possible placement of s within t, a mismatch of text character
                                  t[i]=c with the corresponding pattern character s[k] is handled as follows.
                                  If c is not contained anywhere in s, then shift s completely past t[i] (for it cannot
                                  match any character in s). Otherwise, shift s until an occurrence of character c in s
                                   gets aligned with t[i].
            Space complexity: O(m). Number of distinct alphabet symbols that occur in the pattern, and thus O(m).
        """
        n, m = len(t), len(s)
        if m == 0:
            return 0

        # build ’last’ dictionary
        last = dict()
        for k in range(m):
            # later occurrence overwrites
            last[s[k]] = k

        # t index
        i = m - 1
        # s index
        k = m - 1
        while i < n:
            # a matching character
            if t[i] == s[k]:
                if k == 0:
                    # pattern begins at index i of text
                    return i
                else:
                    # examine previous character of both t and s
                    i -= 1
                    k -= 1
            # make jump
            else:
                # get last position of t[i] in s; if there is no t[i] in s, then -1
                j = last.get(t[i], -1)
                # case analysis for jump step
                i += m - min(k, j + 1)
                # restart at end of pattern
                k = m - 1
        return -1

    def _compute_kmp_fail(self, s: str) -> list:
        """Utility that computes and returns KMP fail list
            Time complexity: O(m).
            Space complexity: O(m).
        """
        m = len(s)
        # by default, presume overlap of 0 everywhere
        fail = [0] * m

        j = 1
        k = 0
        # compute during this pass, if nonzero
        while j < m:
            # k + 1 characters match thus far
            if s[j] == s[k]:
                fail[j] = k + 1
                j += 1
                k += 1
            # k follows a matching prefix
            elif k > 0:
                k = fail[k - 1]
            # no match found starting at j
            else:
                j += 1
        return fail

    def _find_knuth_morris_pratt(self, t: str, s: str) -> int:
        """ Time complexity: O(n + m).
                             The idea of the algorithm is to precompute self-overlaps between portions of the pattern
                             so that when a mismatch occurs at one location, we immediately know the maximum amount to
                             shift the pattern before continuing the search.
                             Failure function f (k) is defined as the length of the longest prefix of P that is a suffix
                             of P[1:k+1] (note that we did not include P[0] here, since we will shift at least one unit)
            Space complexity: O(m). We create 'fail' dictionary.
        """
        n, m = len(t), len(s)
        if m == 0:
            return 0
        fail = self._compute_kmp_fail(s)

        # t index
        i = 0
        # s index
        k = 0
        while i < n:
            # P[0:1+k] matched thus far
            if t[i] == s[k]:
                # match is complete
                if k == m - 1:
                    return i - m + 1
                # go to the next characters
                i += 1
                k += 1
            # mismatch; reuse suffix of P[0:k]
            elif k > 0:
                k = fail[k - 1]
            else:
                i += 1
        # reached end without match
        return -1

    def str_str(self, haystack: str, needle: str) -> int:
        """ Time complexity: O(). This is example of pattern matching.
            Space complexity: O().
        """
        if not needle:
            return 0
        return self._find_knuth_morris_pratt(haystack, needle)
