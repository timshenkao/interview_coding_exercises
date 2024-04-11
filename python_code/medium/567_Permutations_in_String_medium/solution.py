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

import collections

# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.


class Solution:
    def check_inclusion(self, s1, s2):
        """ Time complexity: O(|s1| + |s2|).
            Space complexity: O(128) = 1.
        """
        if len(s1) > len(s2):
            return False

        dic = collections.defaultdict(int)
        for i in range(len(s1)):
            dic[s1[i]] += 1
            if dic[s1[i]] == 0:
                del dic[s1[i]]
            dic[s2[i]] -= 1
            if dic[s2[i]] == 0:
                del dic[s2[i]]
        i = 0
        for j in range(len(s1), len(s2)):
            if not dic:
                return True
            dic[s2[j]] -= 1
            if dic[s2[j]] == 0:
                del dic[s2[j]]
            dic[s2[i]] += 1
            if dic[s2[i]] == 0:
                del dic[s2[i]]
            i += 1
        return not dic

    def check_inclusion2(self, s1, s2):
        """ Time complexity: O(|s1| + |s2|).
            Space complexity: O(128) = 1.
        """
        count = collections.Counter(s1)
        required = len(s1)

        for r, c in enumerate(s2):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            if r >= len(s1):  # The window is oversized.
                count[s2[r - len(s1)]] += 1
                if count[s2[r - len(s1)]] > 0:
                    required += 1
            if required == 0:
                return True
        return False
