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


# 392. Is Subsequence  https://leetcode.com/problems/is-subsequence/
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """ Time complexity: O(n). We iterate once through string t.
            Space complexity: O(1).
        """
        # empty string is substring of any string
        if not s:
            return True

        s_length = len(s)
        t_length = len(t)
        i = 0
        j = 0
        # iterate through string
        while i < t_length:
            # if characters are equal, increase counter for substring
            # i.e. we found one more element from substring
            if j < s_length and t[i] == s[j]:
                j += 1
            if j == s_length:
                return True
            i += 1

        return False

    def is_subsequence_recursion(self, s: str, t: str) -> bool:
        """ Time complexity: O(n). We go through string t.
                             At each recursive step, we consume one character from the string t and
                             optionally one character from string s.
            Space complexity: O(n). Recursion stack.
        """
        # empty string is substring of any string
        if not s:
            return True

        # either:
        #   string is empty and substring is non-empty or
        #   string is exhausted and substring is non-empty
        if s and not t:
            return False

        if s[0] == t[0]:
            return self.is_subsequence_recursion(s[1:], t[1:])
        else:
            return self.is_subsequence_recursion(s, t[1:])

    def is_subsequence_dynamic_programming(self, s: str, t: str) -> bool:
        """ Time complexity: O(n * m). We build dynamic programming matrix with cardinality n * m.
                             The dynamic programming solution tries to calculate the solutions for all combinations
                             of prefixes between the string t and substring s.
            Space complexity: O(n * m). We build dynamic programming matrix with cardinality n * m.
        """
        # empty string is substring of any string
        if not s:
            return True

        s_length = len(s)
        t_length = len(t)

        # matrix to store the history of matches/deletions
        dp_matrix = [[0] * (t_length + 1) for _ in range(s_length + 1)]

        # DP compute, we fill the matrix column by column, bottom up
        for col in range(1, t_length + 1):
            for row in range(1, s_length + 1):
                # we found match
                if s[row - 1] == t[col - 1]:
                    dp_matrix[row][col] = dp_matrix[row - 1][col - 1] + 1
                else:
                    # retrieve the maximal result from previous prefixes
                    dp_matrix[row][col] = max(dp_matrix[row][col - 1], dp_matrix[row - 1][col])

            # check if we can consume the entire source string,  with the current prefix of the target string.
            if dp_matrix[s_length][col] == s_length:
                return True
        return False
