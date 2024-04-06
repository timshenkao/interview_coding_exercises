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

# 249. Group Shifted Strings https://leetcode.com/problems/group-shifted-strings/
# We can shift a string by shifting each of its letters to its successive letter.
# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.
# You may return the answer in any order.
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.


class Solution:
    # def group_strings(self, strings):
    #     """ Time complexity: O(Σ∣strings[i]∣).
    #         Space complexity: O(Σ∣strings[i]∣).
    #     """
    #     table = collections.defaultdict(list)
    #     for w in strings:
    #         pattern = ""
    #         for i in range(1, len(w)):
    #             if ord(w[i]) - ord(w[i - 1]) >= 0:
    #                 pattern += str(ord(w[i]) - ord(w[i - 1]))
    #             else:
    #                 pattern += str(ord(w[i]) - ord(w[i - 1]) + 26)
    #         table[pattern].append(w)
    #     return [table[pattern] for pattern in table]

    def group_strings2(self, strings):
        """ Time complexity: O(Σ∣strings[i]∣).
            Space complexity: O(Σ∣strings[i]∣).
        """
        def _get_key(s: str) -> str:
            """
            Returns the key of 's' by pairwise calculation of differences.
            e.g. _get_key("abc") -> "1,1" because diff(a, b) = 1 and diff(b, c) = 1.
            """
            diffs = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                diffs.append(str(diff))
            return ",".join(diffs)

        key_to_strings = collections.defaultdict(list)
        for s in strings:
            key_to_strings[_get_key(s)].append(s)
        return key_to_strings.values()
