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
import string

# 791. Custom Sort String https://leetcode.com/problems/custom-sort-string/
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order
# previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
# occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.


class Solution:
    def custom_sort_string(self, order, s):
        """ Time complexity: O(∣order∣+∣s∣).
            Space complexity: O(∣order∣+∣s∣).
        """
        t = set(s)
        t2 = set(order)
        c = collections.Counter(s)
        s = [char * c[char] for char in order if char in t]
        add = [char * c[char] for char in t - t2]
        return "".join(s + add)

    def custom_sort_string_unoptimal(self, order: str, s: str) -> str:
        """ Time complexity: O(∣order∣+∣s∣).
            Space complexity: O(∣order∣^2 + |s|).
        """
        ans = ""
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in order:
            while count[ord(c) - ord('a')] > 0:
                # as Python strings are immutable, here we generate all substrings of order
                ans += c
                count[ord(c) - ord('a')] -= 1

        for c in string.ascii_lowercase:
            for k in range(count[ord(c) - ord('a')]):
                # as Python strings are immutable, here we generate up to |s| additional substrings
                ans += c
        return ans
