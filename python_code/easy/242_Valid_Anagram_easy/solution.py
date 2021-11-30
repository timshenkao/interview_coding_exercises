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

# 242. Valid Anagram  https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """ Time complexity: O(N).
            Space complexity: O(1) because table's size stays constant no matter how large n is.
        """
        # no anagram if strings of different length
        if len(t) != len(s):
            return False

        # keep track how many times each character appears
        table = dict()
        for i in range(len(s)):
            if not s[i] in table:
                table[s[i]] = [1, 0]
            else:
                table[s[i]][0] += 1

            if not t[i] in table:
                table[t[i]] = [0, 1]
            else:
                table[t[i]][1] += 1

        # first element - number of times in the first string
        # second element - number of times in the second string
        for _, v in table.items():
            if v[0] != v[1]:
                return False

        return True
