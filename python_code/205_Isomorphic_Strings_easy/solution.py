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

# 205 Isomorphic Strings  https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        """ Time complexity: O(N). We iterate through both strings once.
            Space complexity: O(1) if consider that size of the ASCII character set is fixed and the keys in
                              substitution tables are all valid ASCII characters.
        """
        # strings of different size are not isomorphic
        if len(s) != len(t):
            return False

        # populate substitution table while iterating
        s_subst_table = dict()
        t_subst_table = dict()
        for i in range(len(s)):
            if not s[i] in s_subst_table and not t[i] in t_subst_table:
                s_subst_table[s[i]] = t[i]
                t_subst_table[t[i]] = s[i]
            elif (s[i] in s_subst_table) and s_subst_table[s[i]] != t[i] \
                    or (t[i] in t_subst_table) and t_subst_table[t[i]] != s[i]:
                return False
        return True
