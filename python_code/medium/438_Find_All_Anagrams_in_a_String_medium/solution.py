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

from collections import Counter

# 438. Find All Anagrams in a String https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.


class Solution:
    def find_anagrams(self, s, p):
        """ Time complexity: O(n).
            Space complexity: O(26) = O(1).
        """
        out = list()
        s_counter, p_counter = Counter(s[:len(p)-1]), Counter(p)
        for i in range(len(p)-1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                out.append(i-len(p)+1)
            s_counter[s[i-len(p)+1]] -= 1
            if s_counter[s[i-len(p)+1]] == 0:
                del s_counter[s[i-len(p)+1]]
        return out

    def find_anagrams2(self, s, p):
        """ Time complexity: O(n).
            Space complexity: O(26) = O(1).
        """
        ans = []
        count = Counter(p)
        required = len(p)
        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                required -= 1
            if r >= len(p):
                count[s[r - len(p)]] += 1
                if count[s[r - len(p)]] > 0:
                    required += 1
            if required == 0:
                ans.append(r - len(p) + 1)

        return ans
